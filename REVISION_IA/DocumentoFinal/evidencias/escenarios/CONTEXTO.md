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

Ruta: `DocumentoFinal/evidencias/escenarios/contraejemplos.csv` · Bytes: 1915 · SHA-256: `f9d4fbc2df1ddb6754df1d333f2a58437edc6cb33ee2aa6a72232c2fe4aa1ea4`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## contraejemplos.json

Ruta: `DocumentoFinal/evidencias/escenarios/contraejemplos.json` · Bytes: 3670 · SHA-256: `38843bf9711f5443e2c9e80caea013a76cd119026f35e9b31362dc31d6866c2a`

````text
[
  {
    "id_juego": 1335,
    "titulo": "Resident Evil 4: Wii Edition",
    "real": "bajo",
    "prediccion": "alto",
    "acierto": false,
    "probabilidad_maxima": 0.8962994150630624,
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
      "alto": 0.8962994150630624,
      "bajo": 0.0377525676158464,
      "medio": 0.06594801732109117
    }
  },
  {
    "id_juego": 1054,
    "titulo": "Pokémon Unite",
    "real": "bajo",
    "prediccion": "bajo",
    "acierto": true,
    "probabilidad_maxima": 0.9502326177365681,
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
      "alto": 0.000697734096383338,
      "bajo": 0.9502326177365681,
      "medio": 0.049069648167048376
    }
  },
  {
    "id_juego": 1137,
    "titulo": "Back 4 Blood",
    "real": "medio",
    "prediccion": "bajo",
    "acierto": false,
    "probabilidad_maxima": 0.8567213802407476,
    "Plays": 2900.0,
    "Wishlist": 335.0,
    "Backlogs": 489.0,
    "indice": 0.41704035874439466,
    "generos": [
      "Shooter"
    ],
    "estudio": [
      "Warner Bros. Interactive Entertainment",
      "Turtle Rock Studios"
    ],
    "decada": 2020,
    "Rating": 2.5,
    "Metacritic": 77.0,
    "probabilidades": {
      "alto": 0.011548234160186344,
      "bajo": 0.8567213802407476,
      "medio": 0.13173038559906602
    }
  },
  {
    "id_juego": 1050,
    "titulo": "Pokémon Red",
    "real": "medio",
    "prediccion": "medio",
    "acierto": true,
    "probabilidad_maxima": 0.8081365688044989,
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
      "alto": 0.1133384435190292,
      "bajo": 0.07852498767647191,
      "medio": 0.8081365688044989
    }
  },
  {
    "id_juego": 111,
    "titulo": "Doki Doki Literature Club!",
    "real": "alto",
    "prediccion": "medio",
    "acierto": false,
    "probabilidad_maxima": 0.7968512917026201,
    "Plays": 14000.0,
    "Wishlist": 460.0,
    "Backlogs": 1500.0,
    "indice": 0.7389760837070254,
    "generos": [
      "Adventure",
      "Indie",
      "Visual Novel"
    ],
    "estudio": [
      "Team Salvato"
    ],
    "decada": 2010,
    "Rating": 3.3,
    "Metacritic": 78.0,
    "probabilidades": {
      "alto": 0.08912285683093057,
      "bajo": 0.11402585146644932,
      "medio": 0.7968512917026201
    }
  },
  {
    "id_juego": 78,
    "titulo": "The Last of Us",
    "real": "alto",
    "prediccion": "alto",
    "acierto": true,
    "probabilidad_maxima": 0.974551664282916,
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
      "alto": 0.974551664282916,
      "bajo": 0.0072490383463705635,
      "medio": 0.018199297370713435
    }
  }
]
````

## hipoteticos.csv

Ruta: `DocumentoFinal/evidencias/escenarios/hipoteticos.csv` · Bytes: 1152 · SHA-256: `672f66943f8c5a18311b6bb6a6e6b0cdc9ced4606de7409f572ea4383e3d128a`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

## hipoteticos.json

Ruta: `DocumentoFinal/evidencias/escenarios/hipoteticos.json` · Bytes: 2838 · SHA-256: `5308e852cdfe812cd83164e1bb96c4b2191429bac71b328e870e8b21b5334a28`

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
    "p_alto": 0.024709216246924653,
    "p_bajo": 0.7856088712884108,
    "p_medio": 0.18968191246466454
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
    "prediccion": "medio",
    "p_alto": 0.3642178402326618,
    "p_bajo": 0.16670624906177417,
    "p_medio": 0.46907591070556415
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
    "p_alto": 0.011175747745535702,
    "p_bajo": 0.6337399671898403,
    "p_medio": 0.3550842850646239
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
    "prediccion": "bajo",
    "p_alto": 0.0804394838533213,
    "p_bajo": 0.56597282925134,
    "p_medio": 0.3535876868953387
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
    "p_alto": 0.1800233838641886,
    "p_bajo": 0.6161544573148573,
    "p_medio": 0.2038221588209541
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
    "p_alto": 0.65647546113451,
    "p_bajo": 0.050318432284600395,
    "p_medio": 0.29320610658088964
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
    "prediccion": "medio",
    "p_alto": 0.38674478235785464,
    "p_bajo": 0.22648014163816976,
    "p_medio": 0.38677507600397565
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
    "p_alto": 0.4141998066856576,
    "p_bajo": 0.20879069754399057,
    "p_medio": 0.37700949577035187
  }
]
````

## rejilla.csv

Ruta: `DocumentoFinal/evidencias/escenarios/rejilla.csv` · Bytes: 1842 · SHA-256: `973e0354ee882fc9f44375e1600daa669ee4fbc8d7cfc7caedda0cf61016369e`

Contenido no textual o tabla de datos: consultar el original para inspección visual o recálculo.

