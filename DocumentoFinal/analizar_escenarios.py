"""Escenarios hipotéticos y contraejemplos de prueba sin reentrenar el modelo.

Ejecutar desde la raíz con Final/.venv/bin/python DocumentoFinal/analizar_escenarios.py.
"""
from pathlib import Path
import sys,json,os
D=Path(__file__).resolve().parent;F=D.parent/'Final';sys.path.insert(0,str(F))
import joblib,numpy as np,pandas as pd
cache=D/'revision/cache_matplotlib';cache.mkdir(parents=True,exist_ok=True)
os.environ['MPLCONFIGDIR']=str(cache)
os.environ['XDG_CACHE_HOME']=str(cache)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from src.inferencia import predecir_formulario
from src.features import lista_cruda
from src.objetivo import aplicar_referencia
from src.config import FEATURES
m=joblib.load(F/'models/modelo_popularidad.joblib');meta=json.loads((F/'models/metadata.json').read_text())
out=D/'evidencias/escenarios';out.mkdir(exist_ok=True)
casos=[('S1','Notas bajas',['Adventure','RPG'],['Otro'],2020,45,1.0),('S2','Notas altas',['Adventure','RPG'],['Otro'],2020,99,4.8),('S3','Usuarios altos y prensa baja',['Adventure','RPG'],['Otro'],2020,45,4.8),('S4','Usuarios bajos y prensa alta',['Adventure','RPG'],['Otro'],2020,99,1.0),('S5','Usuarios altos sin prensa',['Adventure','RPG'],['Otro'],2020,None,4.8),('S6','Cambio de organización',['Adventure','RPG'],['Nintendo'],2020,99,4.8),('S7','Cambio de década',['Adventure','RPG'],['Otro'],1980,99,4.8),('S8','Cambio de género',['Shooter'],['Otro'],2020,99,4.8)]
filas=[]
for id,nombre,gs,org,d,crit,rating in casos:
 f,c,p=predecir_formulario(m,gs,org,d,crit,rating)
 filas.append(dict(id=id,escenario=nombre,generos=gs,organizaciones=org,decada=d,metacritic=crit,rating=rating,prediccion=c,**{f'p_{k}':v for k,v in p.items()}))
(out/'hipoteticos.json').write_text(json.dumps(filas,ensure_ascii=False,indent=2));pd.DataFrame(filas).to_csv(out/'hipoteticos.csv',index=False)
rejilla=[]
for rating in [1,2,3,4,4.8]:
 for crit in [45,60,80,99,None]:
  _,c,p=predecir_formulario(m,['Adventure','RPG'],['Otro'],2020,crit,rating)
  rejilla.append(dict(rating=rating,metacritic=crit,prediccion=c,**p))
pd.DataFrame(rejilla).to_csv(out/'rejilla.csv',index=False)
fig,ax=plt.subplots(figsize=(8,5));z=np.array([r['alto'] for r in rejilla]).reshape(5,5)
im=ax.imshow(z,vmin=0,vmax=1,cmap='Blues');ax.set_xticks(range(5),['45','60','80','99','Sin nota']);ax.set_yticks(range(5),['1.0','2.0','3.0','4.0','4.8']);ax.set_xlabel('Metacritic Rating');ax.set_ylabel('Rating de usuarios');ax.set_title('Sensibilidad del modelo con los demás atributos fijos')
for i in range(5):
 for j in range(5):
  r=rejilla[i*5+j];ax.text(j,i,f"{r['prediccion']}\n{r['alto']:.2f}",ha='center',va='center',fontsize=9,color='white' if z[i,j]>.55 else 'black')
fig.colorbar(im,ax=ax,label='Probabilidad no calibrada de alto');fig.tight_layout();fig.savefig(D/'figuras/sensibilidad_escenarios.png',dpi=180);plt.close(fig)
datos=pd.read_csv(F/'data/clean/juegos_modelo.csv');test=datos.loc[datos.particion.eq('prueba')].copy()
for c in ['generos','estudio']:test[c]=test[c].map(lista_cruda)
p=m.predict_proba(test[FEATURES]);test['prediccion']=m.predict(test[FEATURES]);test['probabilidad_maxima']=p.max(axis=1)
assert np.array_equal(aplicar_referencia(test,meta['definicion_objetivo']).nivel_popularidad,test.nivel_popularidad)
# La selección usa resultados de prueba ya observados; es ilustración posterior, no validación nueva.
seleccion=[]
for clase in ['bajo','medio','alto']:
 for acierto in [False,True]:
  sub=test.loc[test.nivel_popularidad.eq(clase)&test.prediccion.eq(test.nivel_popularidad).eq(acierto)].sort_values('probabilidad_maxima',ascending=False)
  f=sub.iloc[0];idx=test.index.get_loc(f.name)
  seleccion.append(dict(id_juego=int(f.id_juego),titulo=f.Title,real=clase,prediccion=f.prediccion,acierto=acierto,probabilidad_maxima=float(f.probabilidad_maxima),Plays=float(f.Plays),Wishlist=float(f.Wishlist),Backlogs=float(f.Backlogs),indice=float(f.popularidad_indice),generos=f.generos,estudio=f.estudio,decada=None if pd.isna(f.decada) else int(f.decada),Rating=None if pd.isna(f.Rating) else float(f.Rating),Metacritic=None if pd.isna(f['Metacritic Rating']) else float(f['Metacritic Rating']),probabilidades=dict(zip(m.classes_,map(float,p[idx])))))
(out/'contraejemplos.json').write_text(json.dumps(seleccion,ensure_ascii=False,indent=2));pd.DataFrame(seleccion).to_csv(out/'contraejemplos.csv',index=False)
print(pd.DataFrame(filas)[['id','prediccion','p_alto','p_medio','p_bajo']].to_string(index=False))
print(pd.DataFrame(seleccion)[['titulo','real','prediccion','acierto','probabilidad_maxima']].to_string(index=False))

tablas = F / 'reports/tables'
pd.DataFrame(filas).to_csv(tablas / 'escenarios_prediccion.csv', index=False)
pd.DataFrame(seleccion).to_csv(tablas / 'contraejemplos_prediccion.csv', index=False)
calibracion = pd.read_csv(tablas / 'calibracion.csv')
fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')
ax.plot([0, 1], [0, 1], color='#50545e', linestyle=':', label='Referencia ideal')
for (clase, grupo), color in zip(calibracion.groupby('clase'), ['#116e78', '#563b8a', '#a54a2a']):
    ax.plot(grupo.probabilidad_media, grupo.fraccion_observada, 'o-', label=clase.title(), color=color)
ax.set(xlabel='Probabilidad media estimada', ylabel='Fracción observada',
       xlim=(0, 1), ylim=(0, 1))
ax.legend()
fig.savefig(D / 'figuras/fiabilidad_rf.png', dpi=180)
plt.close(fig)
