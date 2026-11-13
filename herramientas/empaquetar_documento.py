"""Reúne la entrega LaTeX y verifica sus hashes sin modificar resultados."""
from pathlib import Path
import hashlib
import json
import zipfile

RAIZ = Path(__file__).resolve().parents[1]
DOCUMENTO = RAIZ / 'DocumentoFinal'


def main():
    nombres = ['main.tex', 'main.pdf', 'Portada.tex', 'referencias.bib',
               'informe.tex', 'cifras_informe.tex',
               'README.md', 'ajustar_formato_redaccion.py',
               'analizar_escenarios.py', 'BITACORA_UNIFICADA.md',
               'revision/verificacion.json']
    archivos = [DOCUMENTO / n for n in nombres]
    for carpeta in ['figuras', 'tablas', 'evidencias', 'portada_img', 'revision']:
        archivos.extend(a for a in (DOCUMENTO / carpeta).rglob('*')
                        if a.is_file() and not any(p.startswith('.') for p in a.relative_to(DOCUMENTO).parts)
                        and (carpeta != 'revision' or a.name == 'BITACORA_UNIFICADA.md'))
    manifiesto = {a.relative_to(DOCUMENTO).as_posix():
                  hashlib.sha256(a.read_bytes()).hexdigest() for a in sorted(archivos)}
    (DOCUMENTO / 'MANIFIESTO.json').write_text(json.dumps(manifiesto, ensure_ascii=False, indent=2) + '\n')
    archivos.append(DOCUMENTO / 'MANIFIESTO.json')
    paquete = DOCUMENTO / 'ProyectoMineriaDatos_LaTeX.zip'
    with zipfile.ZipFile(paquete, 'w', zipfile.ZIP_DEFLATED) as z:
        for archivo in archivos:
            z.write(archivo, Path('DocumentoFinal') / archivo.relative_to(DOCUMENTO))
    with zipfile.ZipFile(paquete) as z:
        assert z.testzip() is None
        for nombre, huella in manifiesto.items():
            assert hashlib.sha256(z.read('DocumentoFinal/' + nombre)).hexdigest() == huella
    print(f'Entrega LaTeX: {len(archivos)} archivos; ZIP y hashes verificados.')


if __name__ == '__main__':
    main()
