# Antecedente histórico inmutable

Copia local de Proyecto/docs/games_actualizado_metacritic.csv, 1,512 registros CSV y 20 columnas. No sustituye al maestro designado data/raw/games_curated.csv.

La reconstrucción y los hashes están en reports/trazabilidad_historica.json. No usar wc -l como cuenta de registros por el texto multilínea. src/procedencia.py reproduce la regla first para auditarla, sin aprobarla ni volver a sobrescribir el maestro.
