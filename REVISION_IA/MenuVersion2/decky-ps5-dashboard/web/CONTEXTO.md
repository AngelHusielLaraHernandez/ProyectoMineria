# Carpeta: MenuVersion2/decky-ps5-dashboard/web

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## app.js

Ruta: `MenuVersion2/decky-ps5-dashboard/web/app.js` · Bytes: 3644 · SHA-256: `e1d43836efdaa82e708848454cfa4e8fbc9f869479e34f40ff7572413e65c376`

````text
const games = [
  { title: "Spider-Man: Miles Morales", appid: 1817190, played: "Jugado hoy · 42 h jugadas", time: "42 h", progress: "68%", meta: "PS5 · Acción y aventura" },
  { title: "God of War", appid: 1593500, played: "Jugado ayer · 28 h jugadas", time: "28 h", progress: "54%", meta: "PS5 · Acción" },
  { title: "Horizon Forbidden West", appid: 2420110, played: "Jugado hace 3 días · 19 h jugadas", time: "19 h", progress: "35%", meta: "PS5 · RPG" },
  { title: "Returnal", appid: 1649240, played: "Jugado hace 5 días · 16 h jugadas", time: "16 h", progress: "41%", meta: "PS5 · Roguelike" },
  { title: "Ratchet & Clank", appid: 1895880, played: "Jugado hace 1 semana · 11 h jugadas", time: "11 h", progress: "29%", meta: "PS5 · Plataformas" },
];
const cdn = game => `https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/${game.appid}/library_600x900.jpg`;
const hero = game => `https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/${game.appid}/library_hero.jpg`;
let selected = 0;

const $ = selector => document.querySelector(selector);
function toast(message) {
  const el = $("#toast"); el.textContent = message; el.classList.add("show");
  setTimeout(() => el.classList.remove("show"), 1800);
}
function tile(game, index, active = false) {
  const el = document.createElement("button");
  el.className = `tile ${active ? "active" : ""}`;
  el.innerHTML = `<img src="${cdn(game)}" alt=""><span>${game.title}</span>`;
  el.addEventListener("click", () => selectGame(index));
  return el;
}
function selectGame(index) {
  selected = index;
  const game = games[index];
  $("#gameStrip").replaceChildren(...games.map((item, i) => tile(item, i, i === selected)));
  $("#backdrop").style.backgroundImage = `url("${hero(game)}")`;
  $("#gameTitle").textContent = game.title;
  $("#gameMeta").textContent = game.played;
  $("#infoCards").innerHTML = `<div class="info-card"><small>Tiempo jugado</small><strong>${game.time}</strong><small>Últimas 2 semanas: 6 h</small></div><div class="info-card"><small>Progreso</small><strong>${game.progress}</strong><small>Historia principal</small></div><div class="info-card"><small>Reseñas</small><strong>96%</strong><small>Muy positivas</small></div>`;
}
function showTab(tab) {
  document.querySelectorAll(".tab").forEach(button => button.classList.toggle("active", button.dataset.tab === tab));
  document.querySelectorAll(".view").forEach(view => view.classList.remove("active"));
  $(`#${tab}View`).classList.add("active");
}
function initLibrary() {
  $("#libraryGrid").replaceChildren(...games.concat(games).map((game, index) => tile(game, index % games.length)));
  $("#lowerRow").replaceChildren(...games.slice(1, 5).map((game, index) => tile(game, index + 1)));
}
document.querySelectorAll(".tab").forEach(button => button.addEventListener("click", () => showTab(button.dataset.tab)));
$("#playButton").addEventListener("click", () => toast(`Iniciando ${games[selected].title}...`));
$("#moreButton").addEventListener("click", () => toast("Opciones del juego abiertas"));
$("#searchButton").addEventListener("click", () => $("#searchDialog").showModal());
$("#settingsButton").addEventListener("click", () => toast("Ajustes del dashboard"));
$("#profileButton").addEventListener("click", () => toast("Perfil de jugador"));
$("#searchInput").addEventListener("input", event => {
  const query = event.target.value.toLowerCase();
  document.querySelectorAll("#libraryGrid .tile").forEach((el, index) => {
    el.hidden = query && !games[index % games.length].title.toLowerCase().includes(query);
  });
});
selectGame(0);
initLibrary();

````

## index.html

Ruta: `MenuVersion2/decky-ps5-dashboard/web/index.html` · Bytes: 3514 · SHA-256: `e317ee620fc40e14548b8dfcc135da2219f7237dcdf2d77adb41d2794d241c2a`

````text
<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PS5 Dashboard Web</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <main class="dashboard">
      <div class="backdrop" id="backdrop"></div>
      <div class="shade"></div>

      <header class="topbar">
        <nav class="tabs" aria-label="Secciones">
          <button class="tab active" data-tab="games">Juegos</button>
          <button class="tab" data-tab="media">Medios</button>
          <button class="tab" data-tab="library">Biblioteca</button>
        </nav>
        <div class="top-actions">
          <button class="icon-button" id="searchButton" aria-label="Buscar">⌕</button>
          <button class="icon-button" id="settingsButton" aria-label="Ajustes">⚙</button>
          <button class="avatar" id="profileButton" aria-label="Perfil">A</button>
        </div>
      </header>

      <section class="view active" id="gamesView">
        <div class="game-strip" id="gameStrip"></div>
        <div class="hero-content">
          <div class="hero-copy">
            <p class="eyebrow">JUGADO RECIENTEMENTE</p>
            <h1 id="gameTitle"></h1>
            <p class="game-meta" id="gameMeta"></p>
            <div class="hero-actions">
              <button class="play-button" id="playButton">▶ <span>Jugar</span></button>
              <button class="more-button" id="moreButton" aria-label="Más opciones">•••</button>
            </div>
            <div class="cards" id="infoCards"></div>
          </div>
        </div>
        <section class="lower-section">
          <h2>Continuar jugando</h2>
          <div class="lower-row" id="lowerRow"></div>
        </section>
      </section>

      <section class="view" id="mediaView">
        <div class="section-page">
          <p class="eyebrow">EXPLORAR</p>
          <h1>Medios</h1>
          <div class="media-grid">
            <button class="media-card featured">Galería multimedia <span>Capturas y vídeos</span></button>
            <button class="media-card">Tienda <span>Descubre nuevos juegos</span></button>
            <button class="media-card">Amigos <span>Comprueba quién está conectado</span></button>
            <button class="media-card">Descargas <span>Actualizaciones pendientes</span></button>
          </div>
        </div>
      </section>

      <section class="view" id="libraryView">
        <div class="section-page">
          <p class="eyebrow">TU COLECCIÓN</p>
          <h1>Biblioteca de juegos</h1>
          <div class="filters">
            <button class="filter active">Todos</button>
            <button class="filter">Instalados</button>
            <button class="filter">Favoritos</button>
            <button class="filter">Apps</button>
          </div>
          <div class="library-grid" id="libraryGrid"></div>
        </div>
      </section>

      <div class="toast" id="toast" role="status"></div>
      <dialog id="searchDialog">
        <form method="dialog">
          <button class="close" aria-label="Cerrar">×</button>
          <p class="eyebrow">BUSCAR</p>
          <h2>Encuentra un juego</h2>
          <input id="searchInput" type="search" placeholder="Escribe un título..." autofocus />
          <p class="dialog-hint">Prueba con Spider-Man, God of War o Returnal.</p>
        </form>
      </dialog>
    </main>
    <script src="./app.js"></script>
  </body>
</html>

````

## styles.css

Ruta: `MenuVersion2/decky-ps5-dashboard/web/styles.css` · Bytes: 5310 · SHA-256: `55cd7699e5ddec98e828cd874043a5362ff9bb7902b38c8939ee27e1295ea992`

````text
:root {
  color-scheme: dark;
  font-family: Arial, Helvetica, sans-serif;
  --blue: #1976d2;
  --white: #fff;
  --glass: rgba(7, 14, 30, .78);
}
* { box-sizing: border-box; }
body { margin: 0; background: #050914; color: var(--white); overflow: hidden; }
button { font: inherit; color: inherit; border: 0; cursor: pointer; }
.dashboard { min-height: 100vh; position: relative; overflow: hidden; background: #050914; }
.backdrop, .shade { position: absolute; inset: 0; }
.backdrop { background: center / cover no-repeat; transform: scale(1.04); transition: background-image .45s ease, transform .7s ease; }
.shade { background: linear-gradient(180deg, rgba(2, 6, 18, .66) 0%, rgba(3, 8, 20, .1) 34%, #040812 100%), linear-gradient(90deg, rgba(0,0,0,.62), transparent 62%); }
.topbar { position: relative; z-index: 3; display: flex; justify-content: space-between; align-items: center; padding: 34px 5vw 0; }
.tabs { display: flex; gap: 30px; }
.tab { background: transparent; padding: 9px 0; color: #a9b1c2; font-size: 19px; }
.tab.active { color: #fff; font-weight: 700; border-bottom: 3px solid #fff; }
.top-actions { display: flex; gap: 12px; align-items: center; }
.icon-button, .avatar { width: 42px; height: 42px; border-radius: 50%; display: grid; place-items: center; background: rgba(255,255,255,.13); font-size: 22px; }
.icon-button:hover, .avatar:hover { background: #fff; color: #111; }
.avatar { background: var(--blue); font-size: 17px; font-weight: 700; }
.view { position: relative; z-index: 2; min-height: calc(100vh - 85px); display: none; }
.view.active { display: block; }
.game-strip { display: flex; gap: 18px; padding: 58px 5vw 14px; align-items: end; overflow: hidden; }
.tile { flex: 0 0 112px; height: 112px; border-radius: 12px; overflow: hidden; position: relative; background: #17243b; opacity: .73; transition: .2s; outline: 0 solid transparent; }
.tile.active { width: 154px; height: 154px; opacity: 1; outline: 3px solid white; box-shadow: 0 0 24px rgba(255,255,255,.5); }
.tile img { width: 100%; height: 100%; object-fit: cover; }
.tile span { position: absolute; bottom: 0; left: 0; right: 0; padding: 24px 8px 8px; background: linear-gradient(transparent, rgba(0,0,0,.8)); font-size: 12px; }
.hero-content { padding: 18px 5vw 0; min-height: 42vh; display: flex; align-items: end; }
.hero-copy { max-width: 760px; }
.eyebrow { color: #b7c8e5; letter-spacing: 2px; font-size: 11px; font-weight: 700; margin: 0 0 12px; }
h1 { margin: 0; font-size: clamp(36px, 5vw, 72px); letter-spacing: -2px; }
.game-meta { color: #d3dae7; font-size: 16px; }
.hero-actions { display: flex; gap: 14px; margin: 22px 0; }
.play-button, .more-button { border-radius: 24px; padding: 12px 25px; background: white; color: #07101f; font-weight: 700; }
.more-button { width: 50px; padding: 12px 0; background: rgba(255,255,255,.18); color: white; }
.cards { display: flex; gap: 10px; }
.info-card { min-width: 150px; padding: 14px; border-radius: 12px; background: var(--glass); border: 1px solid rgba(255,255,255,.12); }
.info-card strong { display: block; font-size: 19px; margin-top: 8px; }
.info-card small { color: #aab4c8; }
.lower-section { padding: 12px 5vw; }
h2 { font-size: 21px; margin: 0 0 14px; }
.lower-row { display: flex; gap: 14px; overflow: hidden; }
.lower-row .tile { flex-basis: 100px; height: 100px; }
.section-page { padding: 80px 5vw; max-width: 1100px; }
.section-page h1 { margin-bottom: 28px; }
.media-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.media-card { min-height: 180px; border-radius: 15px; padding: 20px; text-align: left; background: rgba(20,33,60,.85); border: 1px solid rgba(255,255,255,.12); font-weight: 700; font-size: 18px; }
.media-card span { display: block; color: #aab4c8; font-size: 13px; font-weight: 400; margin-top: 12px; }
.media-card.featured { background: linear-gradient(135deg, #1464c1, #0b274e); }
.filters { display: flex; gap: 10px; margin-bottom: 22px; }
.filter { border-radius: 20px; padding: 9px 18px; background: rgba(255,255,255,.13); }
.filter.active { background: #fff; color: #08101f; }
.library-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 15px; max-height: 52vh; overflow: auto; }
.library-grid .tile { width: 100%; height: auto; aspect-ratio: 1; }
.toast { position: fixed; z-index: 8; bottom: 32px; left: 50%; transform: translate(-50%, 90px); background: white; color: #07101f; border-radius: 22px; padding: 12px 22px; transition: .25s; }
.toast.show { transform: translate(-50%, 0); }
dialog { background: #101c33; color: white; border: 1px solid #3c5378; border-radius: 16px; padding: 28px; min-width: min(440px, 90vw); }
dialog::backdrop { background: rgba(0,0,0,.7); }
dialog h2 { font-size: 28px; }
dialog input { width: 100%; padding: 13px; border-radius: 9px; border: 1px solid #6c7f9e; background: #07101f; color: white; }
.close { float: right; background: transparent; font-size: 25px; }
.dialog-hint { color: #aab4c8; font-size: 13px; }
@media (max-width: 800px) { .media-grid { grid-template-columns: repeat(2, 1fr); } .library-grid { grid-template-columns: repeat(3, 1fr); } .cards { overflow-x: auto; } .topbar { padding-left: 24px; padding-right: 24px; } .game-strip, .hero-content, .lower-section, .section-page { padding-left: 24px; padding-right: 24px; } }

````

