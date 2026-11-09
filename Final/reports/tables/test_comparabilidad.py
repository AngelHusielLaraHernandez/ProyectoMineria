"""Verificación independiente de métricas, cobertura OOF y evidencia gráfica."""
from pathlib import Path
import json, re
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
B=Path(__file__).resolve().parents[2]; T=B/'reports/tables'; C=['alto','bajo','medio']
def test_predicciones_y_metricas_independientes():
 tabla=pd.read_csv(T/'comparativo_herramientas.csv'); pred=pd.read_csv(T/'comparativo_predicciones_oof.csv')
 assert set(tabla.herramienta)=={'Python','Weka'}
 for (cohorte,modelo),g in pred.groupby(['cohorte','modelo']):
  n={'catalogo_completo':1117,'catalogo_elegible':1114,'enlace_exportacion_weka':892}[cohorte]
  assert len(g)==n and g.fila.nunique()==n
  m=confusion_matrix(g.real,g.predicha,labels=C); tp=np.diag(m)
  den=m.sum(0)+m.sum(1); f=np.divide(2*tp,den,out=np.zeros(3),where=den!=0)
  r=tabla[(tabla.herramienta=='Python')&(tabla.modelo==modelo)&tabla.esquema_evaluacion.str.contains('; '+cohorte+';')].iloc[0]
  assert np.isclose(r.exactitud_pct,100*tp.sum()/n)
  assert np.isclose(r.f1_macro,f.mean()) and np.isclose(r.f1_ponderado,np.average(f,weights=m.sum(1)))
def test_folds_reproducibles_y_dummy():
 folds=pd.read_csv(T/'comparativo_folds.csv'); pred=pd.read_csv(T/'comparativo_predicciones_oof.csv')
 for cohorte,g in folds.groupby('cohorte'):
  g=g.sort_values('fila'); assert g.fila.nunique()==len(g) and g.fold.nunique()==10
  y=g.clase.to_numpy(); esperado=np.zeros(len(g),int)
  for numero,(a,b) in enumerate(StratifiedKFold(10,shuffle=True,random_state=42).split(np.zeros(len(g)),y),1):
   esperado[b]=numero
   clases,cuentas=np.unique(y[a],return_counts=True); mayor=clases[np.argmax(cuentas)]
   p=pred[(pred.cohorte==cohorte)&(pred.modelo=='DummyClassifier')].sort_values('fila')
   assert (p.predicha.to_numpy()[b]==mayor).all()
  assert np.array_equal(g.fold.to_numpy(),esperado)
def test_weka_redondeo_y_capturas():
 tabla=pd.read_csv(T/'comparativo_herramientas.csv'); d=json.loads((T/'comparativo_detalle.json').read_text())
 for nombre in ['ZeroR','NaiveBayes','J48','RandomForest']:
  r=tabla[(tabla.herramienta=='Weka')&(tabla.modelo==nombre)].iloc[0]; evidencia=d['Weka/'+nombre]
  assert np.isclose(r.f1_macro,np.mean(evidencia['f1_clases_usados']))
  assert abs(r.f1_macro-evidencia['macro_desde_matriz_sin_redondeo'])<=.00051
  assert abs(r.f1_ponderado-evidencia['ponderado_desde_matriz_sin_redondeo'])<=.00051
 for nombre in ['ZeroR.png','NaiveBayes.png','J48.png','RandomForest.png','kmeans_resultado.png','dbscan_resultado.png']:
  with Image.open(B/'reports/weka'/nombre) as im: im.verify()
