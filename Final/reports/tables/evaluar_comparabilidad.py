"""Desde Final: .venv/bin/python reports/tables/evaluar_comparabilidad.py."""
from pathlib import Path
import sys, importlib.util, json, re, csv
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import clone
RAIZ=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(RAIZ))
from src.objetivo import aplicar_referencia, CAMPOS_OBJETIVO
from src.features import lista_cruda
from src.config import FEATURES
spec=importlib.util.spec_from_file_location('modelo_original',RAIZ/'src/04_modelo.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
SALIDA=RAIZ/'reports/tables'; W=RAIZ/'reports/weka'; SEMILLA=42
CLASES=['alto','bajo','medio']
def metricas(y,p):
 return {'exactitud_pct':float(accuracy_score(y,p)*100),'f1_macro':float(f1_score(y,p,labels=CLASES,average='macro',zero_division=0)), 'f1_ponderado':float(f1_score(y,p,labels=CLASES,average='weighted',zero_division=0))}
def desde_matriz(m):
 tp=np.diag(m); reales=m.sum(axis=1); predichas=m.sum(axis=0)
 f=np.divide(2*tp,reales+predichas,out=np.zeros(3),where=(reales+predichas)!=0)
 return f,float(f.mean()),float(np.average(f,weights=reales))
def ejecutar():
 meta=json.loads((RAIZ/'models/metadata.json').read_text())
 df=pd.read_csv(RAIZ/'data/clean/dataset_depurado.csv')
 assert not df[CAMPOS_OBJETIVO].isna().any().any(), 'Faltan señales para construir el objetivo sobre todo el dataset.'
 df=df.reset_index(drop=True)
 df['generos']=df.generos.map(lista_cruda); df['estudio']=df.Team.map(lista_cruda)
 y=aplicar_referencia(df,meta['definicion_objetivo']).nivel_popularidad.to_numpy()
 exportado=pd.read_csv(RAIZ/'data/export/clasificacion.csv')
 modelos={'DummyClassifier':DummyClassifier(strategy='most_frequent',random_state=SEMILLA),'GaussianNB':GaussianNB(),'DecisionTreeClassifier':DecisionTreeClassifier(random_state=SEMILLA),'RandomForestClassifier':RandomForestClassifier(n_estimators=100,random_state=SEMILLA,n_jobs=1)}
 filas=[]; folds_guardados=[]; pred_guardadas=[]; detalle={}
 for cohorte,X,etiquetas,crudas in [('catalogo_completo',df[FEATURES],y,True),('catalogo_elegible',df.loc[df.elegible_analisis.eq(True),FEATURES].reset_index(drop=True),y[df.elegible_analisis.eq(True).to_numpy()],True),('enlace_exportacion_weka',exportado.iloc[:,:-1],exportado.iloc[:,-1].to_numpy(),False)]:
  folds=list(StratifiedKFold(n_splits=10,shuffle=True,random_state=SEMILLA).split(X,etiquetas))
  visitas=np.zeros(len(X),int)
  for numero,(a,b) in enumerate(folds,1):
   assert set(a).isdisjoint(b); visitas[b]+=1
   folds_guardados.extend({'cohorte':cohorte,'fila':int(i),'fold':numero,'clase':etiquetas[i]} for i in b)
  assert np.all(visitas==1)
  for nombre,modelo in modelos.items():
   pred=np.empty(len(X),dtype=object); resultados_folds=[]
   for numero,(a,b) in enumerate(folds,1):
    estimador=mod.construir_pipeline(clone(modelo)) if crudas else clone(modelo)
    estimador.fit(X.iloc[a],etiquetas[a]); pred[b]=estimador.predict(X.iloc[b])
    resultados_folds.append({'fold':numero,'n':len(b),**metricas(etiquetas[b],pred[b])})
   valores=metricas(etiquetas,pred); matriz=confusion_matrix(etiquetas,pred,labels=CLASES)
   fs,macro,ponderado=desde_matriz(matriz)
   assert np.isclose(macro,valores['f1_macro']) and np.isclose(ponderado,valores['f1_ponderado'])
   assert matriz.sum()==len(X)
   medias={k:float(np.mean([f[k] for f in resultados_folds])) for k in valores}
   esquema=f'CV estratificada 10 pliegues; shuffle=True; semilla=42; n={len(X)}; {cohorte}; métricas OOF agrupadas'
   notas=('Toda la cohorte elegible, incluidos los casos antes reservados; no modifica la evaluación original de prueba ni el modelo guardado. Etiquetas fijas con referencia existente de entrenamiento; no se redefine el target por fold. Preprocesamiento ajustado dentro de cada fold. ' if crudas else 'Mismos 892 registros, etiquetas y 52 atributos numéricos que Weka; transformaciones previas al CV, sin nuevo ajuste por fold. ')
   notas+=('Incluye los 1117 registros, incluidos los tres conflictos históricos, como evaluación descriptiva solicitada de todo el archivo; no cambia su exclusión en el modelo de producción. ' if cohorte=='catalogo_completo' else '')
   notas+='CV sin agrupación por título, a diferencia de la evaluación original de producción. Las particiones de sklearn y Java no son idénticas; no se conoce la semilla CV de la sesión Weka guardada. GaussianNB y Weka NaiveBayes no garantizan estimadores numéricos idénticos; CART y J48 difieren en algoritmo/poda; RandomForest usa 100 árboles, semilla 42 frente a S=1 en Weka. No se ajustan hiperparámetros en esta comparación.'
   filas.append({'herramienta':'Python','modelo':nombre,'esquema_evaluacion':esquema,**valores,'notas':notas})
   clave=cohorte+'/'+nombre; detalle[clave]={'n':len(X),'clases':CLASES,'matriz':matriz.tolist(),'metricas_oof':valores,'media_metricas_folds':medias,'folds':resultados_folds}
   pred_guardadas.extend({'cohorte':cohorte,'modelo':nombre,'fila':i,'real':etiquetas[i],'predicha':pred[i]} for i in range(len(X)))
   print(cohorte,nombre,valores,flush=True)
 for nombre in ['ZeroR','NaiveBayes','J48','RandomForest']:
  texto=(W/f'{nombre}.txt').read_text(); seccion=texto.split('=== Detailed Accuracy By Class ===')[1].split('=== Confusion Matrix ===')[0]
  matriz=np.array([list(map(int,g)) for g in re.findall(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s*\|',texto.split('=== Confusion Matrix ===')[1],re.M)])
  assert matriz.shape==(3,3) and matriz.sum()==892
  fs,macro_exacto,ponderado_exacto=desde_matriz(matriz)
  valores=[]; soportes=[]; derivados=[]
  for i,clase in enumerate(CLASES):
   linea=next(l for l in seccion.splitlines() if l.strip().endswith(' '+clase)); partes=linea.split(); valor=partes[4]
   if valor=='?': valores.append(float(fs[i])); derivados.append(clase)
   else:
    valores.append(float(valor)); assert abs(float(valor)-fs[i])<=0.00051
  ponderado=seccion.split('Weighted Avg.')[1].split()[4]
  fpond=ponderado_exacto if ponderado=='?' else float(ponderado)
  if ponderado!='?': assert abs(fpond-ponderado_exacto)<=0.00051
  exactitud=float(re.search(r'^Correctly Classified Instances\s+\d+\s+([\d.]+)\s*%',texto,re.M).group(1))
  assert abs(exactitud-np.trace(matriz)/matriz.sum()*100)<=0.000051
  notas='Salida GUI existente; F1 macro = promedio simple de F-Measure por clase mostrado, con redondeo de tres decimales; F1 ponderado tomado de Weighted Avg. Diferencia de población respecto al catálogo completo: Weka usa 892 registros exportados; comparar también con enlace_exportacion_weka de Python. Particiones Java distintas; preprocesamiento anterior al CV.'
  if derivados: notas+=f' F-Measure ? de {derivados} resuelto desde matriz con 2TP/(2TP+FP+FN); no se copia otra herramienta.'
  if ponderado=='?': notas+=' Weighted Avg. original=?; F1 ponderado calculado desde la matriz, no reportado por Weka.'
  filas.append({'herramienta':'Weka','modelo':nombre,'esquema_evaluacion':'CV estratificada 10 pliegues; n=892; GUI 3.8.7; particiones y semilla CV no recuperadas', 'exactitud_pct':exactitud,'f1_macro':float(np.mean(valores)),'f1_ponderado':fpond,'notas':notas})
  detalle['Weka/'+nombre]={'matriz':matriz.tolist(),'f1_clases_usados':valores,'macro_desde_matriz_sin_redondeo':macro_exacto,'ponderado_desde_matriz_sin_redondeo':ponderado_exacto,'ponderado_mostrado':ponderado}
 # El clustering se conserva, sin atribuirle métricas de clasificación.
 for herramienta,nombre in [('Python','KMeans'),('Python','DBSCAN'),('Weka','SimpleKMeans'),('Weka','DBSCAN')]:
  filas.append({'herramienta':herramienta,'modelo':nombre,'esquema_evaluacion':'Clustering descriptivo; n=887; sin validación de clasificación','exactitud_pct':'','f1_macro':'','f1_ponderado':'','notas':'No aplican métricas de clasificación. Resultados existentes en reports/clustering.md (Python) y reports/weka/kmeans.txt o dbscan.txt (Weka); no se reejecutó clustering.'})
 pd.DataFrame(filas,columns=['herramienta','modelo','esquema_evaluacion','exactitud_pct','f1_macro','f1_ponderado','notas']).to_csv(SALIDA/'comparativo_herramientas.csv',index=False)
 pd.DataFrame(folds_guardados).to_csv(SALIDA/'comparativo_folds.csv',index=False)
 pd.DataFrame(pred_guardadas).to_csv(SALIDA/'comparativo_predicciones_oof.csv',index=False)
 (SALIDA/'comparativo_detalle.json').write_text(json.dumps(detalle,ensure_ascii=False,indent=2)+'\n')
 assert set(pd.read_csv(SALIDA/'comparativo_herramientas.csv').herramienta)=={'Python','Weka'}
 print('Verificaciones de matrices, métricas y particiones: correctas.',flush=True)
if __name__=='__main__': ejecutar()
