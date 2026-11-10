# Carpeta: DocumentoFinal/evidencias/escenarios

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## BITACORA_UNIFICADA.md

Ruta: `DocumentoFinal/evidencias/escenarios/BITACORA_UNIFICADA.md` · Bytes: 1538 · SHA-256: `b499805b116a5bb16a7d87810de44b6883fc2b46bf21c34240656ae401ab3af3`

`````text
# Bitácora unificada

Consolidación sin pérdida de los registros de esta carpeta. Cada bloque identifica su archivo de origen y su huella. Las cifras de revisiones anteriores son históricas; no sustituyen los modelos, tablas y reportes vigentes. No se fusionan las salidas originales de Weka ni el log de limpieza requerido por el pipeline.


## Origen: DocumentoFinal/evidencias/escenarios/ejecucion.txt

SHA-256: `70d2061c9f5f99715f674aea3bc4b1cf58ffb04c02020e69ff9deaed92acd824`

````text
Matplotlib is building the font cache; this may take a moment.
id prediccion   p_alto  p_medio   p_bajo
S1       bajo 0.114823 0.285509 0.599668
S2       alto 0.540827 0.250553 0.208620
S3       bajo 0.209113 0.351573 0.439314
S4       alto 0.382456 0.309653 0.307891
S5       bajo 0.277982 0.279957 0.442061
S6       alto 0.587149 0.261432 0.151419
S7       alto 0.571937 0.236142 0.191921
S8       alto 0.496621 0.262776 0.240603
                                titulo  real prediccion  acierto  probabilidad_maxima
          Resident Evil 4: Wii Edition  bajo       alto    False             0.668467
                         Pokémon Unite  bajo       bajo     True             0.771581
Uncharted: The Nathan Drake Collection medio       alto    False             0.698397
                           Pokémon Red medio      medio     True             0.519883
                         Jet Set Radio  alto       bajo    False             0.491528
                        The Last of Us  alto       alto     True             0.823502

````

`````

## contraejemplos.csv

Ruta: `DocumentoFinal/evidencias/escenarios/contraejemplos.csv` · Bytes: 1763 · SHA-256: `06367ca6046ea2e626ecf309f125f71aa9421b9d66b03c58d6900262f657dbdd`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## contraejemplos.json

Ruta: `DocumentoFinal/evidencias/escenarios/contraejemplos.json` · Bytes: 3684 · SHA-256: `931cecb65532e3a1823da15569d6890713b5e82b3d67dc8e3e80086429ef6403`

````text
[
  {
    "id_juego": 1335,
    "titulo": "Resident Evil 4: Wii Edition",
    "real": "bajo",
    "prediccion": "alto",
    "acierto": false,
    "probabilidad_maxima": 0.6684665448473315,
    "Plays": 1100.0,
    "Wishlist": 76.0,
    "Backlogs": 213.0,
    "indice": 0.132660687593423,
    "generos": [
      "Adventure",
      "Shooter"
    ],
    "estudio": [
      "Capcom Production Studio 4",
      "Capcom"
    ],
    "decada": 2000,
    "Rating": 4.4,
    "Metacritic": 91.0,
    "probabilidades": {
      "alto": 0.6684665448473315,
      "bajo": 0.08935785908152606,
      "medio": 0.24217559607114222
    }
  },
  {
    "id_juego": 1054,
    "titulo": "Pokémon Unite",
    "real": "bajo",
    "prediccion": "bajo",
    "acierto": true,
    "probabilidad_maxima": 0.7715811749543512,
    "Plays": 4500.0,
    "Wishlist": 65.0,
    "Backlogs": 184.0,
    "indice": 0.2702416542102641,
    "generos": [
      "MOBA"
    ],
    "estudio": [
      "Timi",
      "The Pokémon Company"
    ],
    "decada": 2020,
    "Rating": 2.7,
    "Metacritic": 70.0,
    "probabilidades": {
      "alto": 0.05151646177093161,
      "bajo": 0.7715811749543512,
      "medio": 0.17690236327471673
    }
  },
  {
    "id_juego": 658,
    "titulo": "Uncharted: The Nathan Drake Collection",
    "real": "medio",
    "prediccion": "alto",
    "acierto": false,
    "probabilidad_maxima": 0.6983971867015208,
    "Plays": 4300.0,
    "Wishlist": 319.0,
    "Backlogs": 1300.0,
    "indice": 0.570814648729447,
    "generos": [
      "Adventure",
      "Platform",
      "Shooter"
    ],
    "estudio": [
      "Naughty Dog",
      "Sony Computer Entertainment, Inc. (SCEI)"
    ],
    "decada": 2010,
    "Rating": 4.1,
    "Metacritic": 86.0,
    "probabilidades": {
      "alto": 0.6983971867015208,
      "bajo": 0.09558917580731595,
      "medio": 0.20601363749116358
    }
  },
  {
    "id_juego": 1050,
    "titulo": "Pokémon Red",
    "real": "medio",
    "prediccion": "medio",
    "acierto": true,
    "probabilidad_maxima": 0.5198829656017434,
    "Plays": 8800.0,
    "Wishlist": 154.0,
    "Backlogs": 425.0,
    "indice": 0.4481502242152466,
    "generos": [
      "Adventure",
      "RPG",
      "Turn Based Strategy"
    ],
    "estudio": [
      "Nintendo",
      "Game Freak"
    ],
    "decada": 1990,
    "Rating": 3.4,
    "Metacritic": null,
    "probabilidades": {
      "alto": 0.25742434866068536,
      "bajo": 0.22269268573757106,
      "medio": 0.5198829656017434
    }
  },
  {
    "id_juego": 1057,
    "titulo": "Jet Set Radio",
    "real": "alto",
    "prediccion": "bajo",
    "acierto": false,
    "probabilidad_maxima": 0.49152792529567263,
    "Plays": 3500.0,
    "Wishlist": 671.0,
    "Backlogs": 1900.0,
    "indice": 0.6787849669015588,
    "generos": [
      "Platform"
    ],
    "estudio": [
      "BlitWorks",
      "Sega"
    ],
    "decada": 2010,
    "Rating": 3.7,
    "Metacritic": 70.0,
    "probabilidades": {
      "alto": 0.13003255527395496,
      "bajo": 0.49152792529567263,
      "medio": 0.3784395194303722
    }
  },
  {
    "id_juego": 78,
    "titulo": "The Last of Us",
    "real": "alto",
    "prediccion": "alto",
    "acierto": true,
    "probabilidad_maxima": 0.8235016355289921,
    "Plays": 17000.0,
    "Wishlist": 1400.0,
    "Backlogs": 2000.0,
    "indice": 0.8959267563527654,
    "generos": [
      "Adventure",
      "Shooter"
    ],
    "estudio": [
      "Naughty Dog",
      "Sony Computer Entertainment"
    ],
    "decada": 2010,
    "Rating": 4.2,
    "Metacritic": 95.0,
    "probabilidades": {
      "alto": 0.8235016355289921,
      "bajo": 0.053934428207451146,
      "medio": 0.12256393626355631
    }
  }
]
````

## hipoteticos.csv

Ruta: `DocumentoFinal/evidencias/escenarios/hipoteticos.csv` · Bytes: 1149 · SHA-256: `d55fc932ca7140456083308af47746a1efb11005d6820791b2434927eff6d117`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## hipoteticos.json

Ruta: `DocumentoFinal/evidencias/escenarios/hipoteticos.json` · Bytes: 2835 · SHA-256: `7c22668556909dace3401d5314190e7c1c257d0a4e99a47c9a3dac96984225bd`

````text
[
  {
    "id": "S1",
    "escenario": "Notas bajas",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 2020,
    "metacritic": 45,
    "rating": 1.0,
    "prediccion": "bajo",
    "p_alto": 0.11482340781897761,
    "p_bajo": 0.5996677783176304,
    "p_medio": 0.28550881386339216
  },
  {
    "id": "S2",
    "escenario": "Notas altas",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 2020,
    "metacritic": 99,
    "rating": 4.8,
    "prediccion": "alto",
    "p_alto": 0.5408269453085124,
    "p_bajo": 0.20861964106899933,
    "p_medio": 0.25055341362248806
  },
  {
    "id": "S3",
    "escenario": "Usuarios altos y prensa baja",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 2020,
    "metacritic": 45,
    "rating": 4.8,
    "prediccion": "bajo",
    "p_alto": 0.20911329702511197,
    "p_bajo": 0.4393136619116028,
    "p_medio": 0.35157304106328496
  },
  {
    "id": "S4",
    "escenario": "Usuarios bajos y prensa alta",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 2020,
    "metacritic": 99,
    "rating": 1.0,
    "prediccion": "alto",
    "p_alto": 0.3824562843459407,
    "p_bajo": 0.30789091633601195,
    "p_medio": 0.30965279931804734
  },
  {
    "id": "S5",
    "escenario": "Usuarios altos sin prensa",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 2020,
    "metacritic": null,
    "rating": 4.8,
    "prediccion": "bajo",
    "p_alto": 0.2779815193893014,
    "p_bajo": 0.44206113209632525,
    "p_medio": 0.27995734851437365
  },
  {
    "id": "S6",
    "escenario": "Cambio de organización",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Nintendo"
    ],
    "decada": 2020,
    "metacritic": 99,
    "rating": 4.8,
    "prediccion": "alto",
    "p_alto": 0.587149162448355,
    "p_bajo": 0.1514191359361513,
    "p_medio": 0.2614317016154936
  },
  {
    "id": "S7",
    "escenario": "Cambio de década",
    "generos": [
      "Adventure",
      "RPG"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 1980,
    "metacritic": 99,
    "rating": 4.8,
    "prediccion": "alto",
    "p_alto": 0.5719369254431956,
    "p_bajo": 0.1919206007241524,
    "p_medio": 0.2361424738326517
  },
  {
    "id": "S8",
    "escenario": "Cambio de género",
    "generos": [
      "Shooter"
    ],
    "organizaciones": [
      "Otro"
    ],
    "decada": 2020,
    "metacritic": 99,
    "rating": 4.8,
    "prediccion": "alto",
    "p_alto": 0.4966212185337543,
    "p_bajo": 0.24060322520525224,
    "p_medio": 0.2627755562609934
  }
]
````

## rejilla.csv

Ruta: `DocumentoFinal/evidencias/escenarios/rejilla.csv` · Bytes: 1835 · SHA-256: `2ce1fadc1cd4b7afdf169e9cdd2ab6813971c4fded353c3a05470277e3baa41f`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

