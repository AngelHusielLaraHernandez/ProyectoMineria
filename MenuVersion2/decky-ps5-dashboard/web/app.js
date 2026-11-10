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
