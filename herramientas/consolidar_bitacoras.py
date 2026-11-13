"""Reúne bitácoras históricas sin alterar código, datos ni salidas originales de Weka.

Ejecutar desde la raíz: python3 herramientas/consolidar_bitacoras.py.
Los bloques conservan nombre, SHA-256 y contenido completo; repetir es seguro.
"""
from pathlib import Path
import hashlib
import json
import os
import re

RAIZ = Path(__file__).resolve().parents[1]
NOMBRE = 'BITACORA_UNIFICADA.md'
EXCLUIDOS = {'.git', '.venv', '.venv314', 'node_modules', '__pycache__',
             '.cache', '.pytest_cache', 'REVISION_IA', 'dist', 'build',
             '.repositorios_locales', '.home', '.preferencias', 'cache_matplotlib'}


def seleccion(archivo):
    relativo = archivo.relative_to(RAIZ)
    if set(relativo.parts) & EXCLUIDOS or archivo.name == NOMBRE:
        return False
    if archivo.suffix == '.log':
        return not archivo.with_suffix('.tex').is_file()
    if archivo.suffix == '.txt':
        return bool(re.search(r'^(pruebas|ejecucion|build_log|compilacion)', archivo.name))
    if archivo.suffix != '.md' or 'reports' not in relativo.parts:
        return False
    return archivo.name in {
        'codex_log.md', 'correcciones_auditoria.md', 'correcciones_auditoria2.md',
        'revision_anteproyecto_v2_rubrica.md', 'revision_graficas.md',
        'tipografia.md', 'verificacion_funcional.md', 'diagnostico_cierres.md',
        'revision_respaldo.md', 'cierre_weka_2026_11_09.md', 'resumen_gui.md',
        'comparativo_herramientas_notas.md',
    }


def main():
    grupos = {}
    for carpeta, subcarpetas, nombres in os.walk(RAIZ):
        subcarpetas[:] = [n for n in subcarpetas if n not in EXCLUIDOS]
        for nombre in nombres:
            archivo = Path(carpeta) / nombre
            if archivo.is_file() and seleccion(archivo):
                grupos.setdefault(archivo.parent, []).append(archivo)
    indice = []
    for carpeta, archivos in sorted(grupos.items()):
        destino = carpeta / NOMBRE
        contenido = destino.read_bytes().decode('utf-8') if destino.exists() else (
            '# Bitácora unificada\n\n'
            'Consolidación sin pérdida de los registros de esta carpeta. '
            'Cada bloque identifica su archivo de origen y su huella. '
            'Las cifras de revisiones anteriores son históricas; no sustituyen '
            'los modelos, tablas y reportes vigentes. No se fusionan las salidas '
            'originales de Weka ni el log de limpieza requerido por el pipeline.\n\n'
        )
        for archivo in sorted(archivos):
            bruto = archivo.read_bytes()
            texto = bruto.decode('utf-8', errors='replace')
            huella = hashlib.sha256(bruto).hexdigest()
            cerca = '`' * max(4, max((len(x) for x in re.findall(r'`+', texto)), default=0) + 1)
            origen = archivo.relative_to(RAIZ).as_posix()
            if f'## Origen: {origen}\n\nSHA-256: `{huella}`' not in contenido or texto not in contenido:
                contenido += f'\n## Origen: {origen}\n\nSHA-256: `{huella}`\n\n{cerca}text\n{texto}\n{cerca}\n'
            indice.append({'origen': origen, 'destino': destino.relative_to(RAIZ).as_posix(), 'sha256': huella})
        destino.write_text(contenido)
        # Verifica la escritura antes de retirar los registros individuales.
        comprobado = destino.read_bytes().decode('utf-8')
        for archivo in archivos:
            assert archivo.read_bytes().decode('utf-8', errors='replace') in comprobado
        for archivo in archivos:
            archivo.unlink()
    registro = RAIZ / 'herramientas/consolidacion.json'
    completo = []
    for carpeta, subcarpetas, nombres in os.walk(RAIZ):
        subcarpetas[:] = [n for n in subcarpetas if n not in EXCLUIDOS]
        if NOMBRE in nombres:
            bitacora = Path(carpeta) / NOMBRE
            for origen, huella in re.findall(r'^## Origen: (.+)\n\nSHA-256: `([a-f0-9]{64})`', bitacora.read_text(), re.M):
                completo.append({'origen': origen, 'destino': bitacora.relative_to(RAIZ).as_posix(), 'sha256': huella})
    registro.write_text(json.dumps(completo, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(indice)} registros reunidos en {len(grupos)} bitácoras; contenido comprobado.')


if __name__ == '__main__':
    main()
