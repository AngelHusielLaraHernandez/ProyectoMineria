"""Audita el modelo vigente y busca mejoras solo en los pliegues de entrenamiento.

Ejecutar desde Final: python src/05_revision_predicciones.py
No sustituye el modelo de producción ni selecciona parámetros con la prueba.
"""
from pathlib import Path
import sys
RAIZ = Path(__file__).resolve().parents[1]
if not __package__:
    sys.path.insert(0, str(RAIZ))
import importlib
import json
import hashlib
import joblib
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, confusion_matrix
from src.config import FEATURES, SEED
from src.features import lista_cruda
from src.objetivo import aplicar_referencia, ajustar_referencia, CLASES, ClasificadorObjetivoLocal


def ejecutar(solo_integridad=False):
    salida = RAIZ / 'reports/revision_predicciones'
    salida.mkdir(exist_ok=True, parents=True)
    datos = pd.read_csv(RAIZ / 'data/clean/juegos_modelo.csv')
    for c in ['generos', 'estudio']:
        datos[c] = datos[c].map(lista_cruda)
    modelo = joblib.load(RAIZ / 'models/modelo_popularidad.joblib')
    meta = json.loads((RAIZ / 'models/metadata.json').read_text())
    tr = datos.loc[datos.particion.eq('entrenamiento')].copy()
    te = datos.loc[datos.particion.eq('prueba')].copy()
    assert set(tr.grupo_titulo).isdisjoint(te.grupo_titulo)
    esperado = aplicar_referencia(datos, meta['definicion_objetivo']).nivel_popularidad
    assert np.array_equal(esperado, datos.nivel_popularidad)
    pred = modelo.predict(te[FEATURES])
    prob = modelo.predict_proba(te[FEATURES])
    assert np.all(np.isfinite(prob)) and np.allclose(prob.sum(axis=1), 1)
    assert np.array_equal(pred, modelo.classes_[prob.argmax(axis=1)])
    archivo_pred = pd.read_csv(RAIZ / 'reports/modelo_predicciones_prueba.csv').set_index('id_juego')
    assert np.array_equal(pred, archivo_pred.loc[te.id_juego, meta['modelo']])
    f1 = f1_score(te.nivel_popularidad, pred, labels=CLASES, average='macro')
    assert np.isclose(f1, meta['metricas']['f1_macro'])
    nn = joblib.load(RAIZ / 'models/vecinos_popularidad.joblib')
    assert set(nn['ids']) == set(tr.id_juego)
    z = modelo.named_steps['preparar'].transform(tr[FEATURES])
    por_id = pd.DataFrame(z, index=tr.id_juego).loc[nn['ids']].to_numpy()
    assert np.allclose(por_id, nn['vecinos']._fit_X)
    ref = ajustar_referencia(tr)
    assert ref['cortes'] == meta['definicion_objetivo']['cortes']
    filas_auditoria = {'modelo': meta['modelo'], 'python': meta['python'], 'n_entrenamiento':len(tr), 'n_prueba':len(te),
        'exactitud_prueba':accuracy_score(te.nivel_popularidad,pred), 'f1_macro_prueba':f1,
        'f1_ponderado_prueba':f1_score(te.nivel_popularidad,pred,average='weighted'),
        'recall_por_clase':dict(zip(CLASES,recall_score(te.nivel_popularidad,pred,labels=CLASES,average=None))),
        'matriz_confusion':confusion_matrix(te.nivel_popularidad,pred,labels=CLASES).tolist(),
        'paridad_predicciones_guardadas':True, 'probabilidades_validas':True,
        'vecinos_solo_entrenamiento_y_mismo_espacio':True, 'objetivo_reproducido':True,
        'sha256_modelo':hashlib.sha256((RAIZ/'models/modelo_popularidad.joblib').read_bytes()).hexdigest()}
    (salida/'auditoria.json').write_text(json.dumps(filas_auditoria,ensure_ascii=False,indent=2))
    print('Auditoría de integridad completada.',flush=True)
    if solo_integridad:
        return filas_auditoria
    modulo = importlib.import_module('src.04_modelo')
    contexto = tr[[*FEATURES, 'Plays','Wishlist','Backlogs','id_juego']].reset_index(drop=True)
    folds = [(np.flatnonzero(tr.fold_validacion.to_numpy()!=n),np.flatnonzero(tr.fold_validacion.to_numpy()==n)) for n in range(1,11)]
    candidatos = {'Vigente':clone(modelo)}
    configuraciones = [
        {'min_samples_leaf':1, 'class_weight':None, 'max_features':'sqrt'},
        {'min_samples_leaf':2, 'class_weight':'balanced_subsample', 'max_features':'sqrt'},
        {'min_samples_leaf':5, 'class_weight':'balanced_subsample', 'max_features':'sqrt'},
        {'min_samples_leaf':10, 'class_weight':'balanced_subsample', 'max_features':'sqrt'},
        {'min_samples_leaf':2, 'class_weight':None, 'max_features':.5},
        {'min_samples_leaf':5, 'class_weight':'balanced_subsample', 'max_features':.5},
        {'min_samples_leaf':10, 'class_weight':None, 'max_features':.5},
    ]
    for n,c in enumerate(configuraciones,1):
        candidatos[f'RF_revision_{n}'] = modulo.construir_pipeline(RandomForestClassifier(n_estimators=200,random_state=SEED,n_jobs=1,**c))
    filas=[]
    for nombre,pipeline in candidatos.items():
        for n,(a,b) in enumerate(folds,1):
            assert set(tr.grupo_titulo.iloc[a]).isdisjoint(tr.grupo_titulo.iloc[b])
            estimador=ClasificadorObjetivoLocal(clone(pipeline)).fit(contexto.iloc[a])
            verdad=aplicar_referencia(contexto.iloc[b],estimador.referencia_).nivel_popularidad
            p=estimador.predict(contexto.iloc[b])
            filas.append({'candidato':nombre,'fold':n,'n_validacion':len(b),
                'f1_macro':f1_score(verdad,p,labels=CLASES,average='macro',zero_division=0),
                'exactitud':accuracy_score(verdad,p),
                'recall_medio':recall_score(verdad,p,labels=['medio'],average=None,zero_division=0)[0]})
        pd.DataFrame(filas).to_csv(salida/'busqueda_folds.csv',index=False)
        print(f'{nombre}: F1 CV={np.mean([f["f1_macro"] for f in filas if f["candidato"]==nombre]):.4f}',flush=True)
    tabla=pd.DataFrame(filas)
    resumen=tabla.groupby('candidato').agg(f1_macro_cv=('f1_macro','mean'),desviacion_cv=('f1_macro','std'),recall_medio_cv=('recall_medio','mean')).sort_values('f1_macro_cv',ascending=False)
    resumen.to_csv(salida/'busqueda_resumen.csv')
    ganador=resumen.index[0]
    base=tabla.loc[tabla.candidato.eq('Vigente')].sort_values('fold').f1_macro.to_numpy()
    nuevo=tabla.loc[tabla.candidato.eq(ganador)].sort_values('fold').f1_macro.to_numpy()
    mejora=float(nuevo.mean()-base.mean())
    promover=bool(ganador!='Vigente' and mejora>=.01 and (nuevo>base).sum()>=6)
    decision={'ganador_cv':ganador,'mejora_f1_cv':mejora,'pliegues_superiores':int((nuevo>base).sum()),
        'criterio_predefinido':'Mejora media de al menos 0.01 F1 macro y superioridad en al menos 6 de 10 pliegues; no es prueba de significancia.',
        'recomienda_promocion':promover,'parametros':candidatos[ganador].named_steps['clasificar'].get_params(),
        'limitacion':'Se reutilizan pliegues de entrenamiento para explorar hiperparámetros; CV no anidada. La prueba existente ya fue observada y no decide la selección. Se requiere validación externa para afirmar mejora prospectiva.'}
    (salida/'decision.json').write_text(json.dumps(decision,ensure_ascii=False,indent=2))
    print(json.dumps(decision,ensure_ascii=False),flush=True)
    return decision


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--solo-integridad', action='store_true')
    ejecutar(parser.parse_args().solo_integridad)
