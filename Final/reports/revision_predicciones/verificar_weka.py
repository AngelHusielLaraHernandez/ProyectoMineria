"""Recalcula aciertos y F1 desde salidas Weka existentes, sin ejecutar Weka."""
from pathlib import Path
import re,json,hashlib,csv
RAIZ=Path(__file__).resolve().parents[2]
resultados=[]
for nombre in ['ZeroR','NaiveBayes','J48','RandomForest']:
    p=RAIZ/'reports/weka'/f'{nombre}.txt'; texto=p.read_text()
    filas=[re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+\|.*?=\s*(\w+)',l) for l in texto.splitlines()]
    filas=[f for f in filas if f]
    matriz=[[int(f[i]) for i in range(1,4)] for f in filas]
    clases=[f[4] for f in filas]
    total=sum(map(sum,matriz));aciertos=sum(matriz[i][i] for i in range(3))
    original=float(re.search(r'Correctly Classified Instances\s+\d+\s+([\d.]+)',texto)[1])
    assert total==892 and abs(original-100*aciertos/total)<.000051
    f1=[];f1_mostrados=[]
    for i,c in enumerate(clases):
        tp=matriz[i][i];den=sum(matriz[i])+sum(f[i] for f in matriz)
        f1.append(2*tp/den if den else 0)
        linea=next(l for l in texto.splitlines() if len(l.split())==9 and l.split()[-1]==c)
        v=linea.split()[4]
        f1_mostrados.append(f1[-1] if v=='?' else float(v))
    ponderado_txt=re.search(r'Weighted Avg\.\s+(.+)',texto)[1].split()[4]
    ponderado=sum(sum(matriz[i])*f1[i] for i in range(3))/total
    resultados.append({'modelo':nombre,'n':total,'aciertos':aciertos,'exactitud_pct':original,
        'f1_macro_promedio_mostrado':sum(f1_mostrados)/3,
        'f1_macro_desde_matriz':sum(f1)/3,'f1_ponderado':ponderado if ponderado_txt=='?' else float(ponderado_txt),
        'ponderado_calculado':ponderado,'ponderado_es_recalculado':ponderado_txt=='?',
        'clases':clases,'matriz':matriz,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(RAIZ/'reports/revision_predicciones/weka_recalculado.json').write_text(json.dumps(resultados,ensure_ascii=False,indent=2))
print('Cuatro matrices Weka verificadas; 892 casos en cada una y exactitudes reproducidas.')
