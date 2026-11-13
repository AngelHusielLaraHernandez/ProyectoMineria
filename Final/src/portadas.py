"""Portadas locales y búsqueda de juegos en la tienda pública de Steam."""
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
import json
import re
import unicodedata
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen


_MOD_VERSION = 'p5-v12-portadas'

PORTADAS_LOCALES = {
    'Halo Infinite': 'halo',
    'God of War Ragnarök': 'god-of-war',
    'The Legend of Zelda: Tears of the Kingdom': 'zelda',
    'Super Mario Odyssey': 'mario',
    'Hogwarts Legacy': 'hogwarts',
    'Bloodborne PSX': 'bloodborne-psx',
    'Wo Long: Fallen Dynasty': 'wo-long',
    'Limbus Company': 'limbus',
    'Citizen Sleeper': 'citizen-sleeper',
    'Serial Experiments Lain': 'lain',
    'System Shock': 'system-shock',
    'Donkey Kong Country': 'donkey-kong',
    'Shin Megami Tensei: Devil Summoner - Soul Hackers': 'soul-hackers',
    'Final Fantasy V': 'final-fantasy-v',
}
PORTADAS_ORIGINALES = frozenset({
    'lain', 'system-shock', 'donkey-kong', 'soul-hackers', 'final-fantasy-v',
})
HOSTS_IMAGEN = {
    'cdn.akamai.steamstatic.com', 'shared.akamai.steamstatic.com',
    'shared.fastly.steamstatic.com', 'cdn.cloudflare.steamstatic.com',
}


def _normalizar(titulo):
    texto = unicodedata.normalize('NFKD', titulo.casefold())
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return ' '.join(re.findall(r'[^\W_]+', texto))


def _consultar(ruta, **parametros):
    url = f'https://store.steampowered.com/api/{ruta}?{urlencode(parametros)}'
    peticion = Request(url, headers={'User-Agent': 'ObservatorioVideojuegos/1.0'})
    with urlopen(peticion, timeout=1.5) as respuesta:
        return json.load(respuesta)


def portada_steam(juego):
    """Acepta una única ficha de juego con título y año coincidentes."""
    titulo, anio = juego
    if not anio:
        return None
    try:
        encontrados = _consultar('storesearch/', term=titulo, l='english', cc='us')
        coincidencias = [
            int(fila['id']) for fila in encontrados.get('items', [])
            if fila.get('type') == 'app' and _normalizar(fila['name']) == _normalizar(titulo)
        ]
        if len(coincidencias) != 1:
            return None
        appid = str(coincidencias[0])
        ficha = _consultar('appdetails', appids=appid, l='english', cc='us').get(appid, {})
        datos = ficha.get('data', {})
        fecha = datos.get('release_date', {}).get('date', '')
        imagen = datos.get('header_image', '')
        url = urlsplit(imagen)
        if (datos.get('type') == 'game' and _normalizar(datos.get('name', '')) == _normalizar(titulo)
                and str(anio) in re.findall(r'\b\d{4}\b', fecha)
                and url.scheme == 'https' and url.netloc in HOSTS_IMAGEN
                and f'/apps/{appid}/' in url.path):
            return imagen
    except (OSError, ValueError, KeyError, TypeError):
        # La consulta externa es opcional. La tarjeta sigue usando datos del catálogo.
        return None
    return None


def buscar_portadas(juegos):
    def descargar(juego):
        imagen = portada_steam(juego)
        if not imagen:
            return None
        try:
            with urlopen(imagen, timeout=1.5) as respuesta:
                contenido = respuesta.read(400_001)
            if contenido.startswith(b'\xff\xd8\xff') and len(contenido) <= 400_000:
                return b64encode(contenido).decode('ascii')
        except OSError:
            pass
        return None

    with ThreadPoolExecutor(max_workers=5) as pool:
        return dict(zip(juegos, pool.map(descargar, juegos)))
