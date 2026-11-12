# Carpeta: Final/assets/css

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## persona5.css

Ruta: `Final/assets/css/persona5.css` · Bytes: 48601 · SHA-256: `8faae316a7871013f0397beae1b7c1de5ba7dcd48aa62296a9ea45f66e2a23fc`

````text
/* ==========================================================================
   PHANTOM’S PERSONA — IDENTIDAD AZUL NEÓN Y MORADO
   ========================================================================== */


:root {
  --p5-black: var(--bg-primary);
  --p5-surface: var(--bg-panel);
  --p5-red: var(--primary);
  --p5-dark-red: var(--bg-chart);
  --p5-white: var(--text-primary);
  --p5-gray: var(--text-secondary);
  --p5-yellow: var(--accent);
  --p5-cyan: var(--secondary);
  --gradient-space: ;
  color-scheme: dark;
  accent-color: var(--p5-red);
}

@supports (background: linear-gradient(in oklab, red, blue)) {
  :root {
    --gradient-space: in oklab;
  }
}

@supports not (accent-color: var(--primary)) {
  input[type="checkbox"],
  input[type="radio"] {
    appearance: none;
    width: 1.1rem;
    height: 1.1rem;
    border: 2px solid var(--p5-red);
    background-color: var(--p5-black);
  }
  input[type="checkbox"]:checked,
  input[type="radio"]:checked {
    background-color: var(--p5-red);
  }
}

/* Base Canvas & Animated Halftone Background */
html, body, [data-testid="stAppViewContainer"], .stApp {
  background-color: var(--p5-black) !important;
  background-image:
    radial-gradient(circle at 18% 22%, rgba(0, 207, 255, 0.10) 0%, transparent 38%),
    radial-gradient(circle at 85% 75%, rgba(23, 13, 55, 0.28) 0%, transparent 44%),
    repeating-linear-gradient(
      -28deg,
      rgba(165, 107, 255, 0.025) 0px,
      rgba(165, 107, 255, 0.025) 18px,
      transparent 18px,
      transparent 44px
    ) !important;
  color: var(--p5-white) !important;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size-adjust: from-font;
  overflow-x: hidden !important;
}

[data-testid="stHeader"] {
  background: rgba(5, 13, 34, 0.82) !important;
  border-bottom: 2px solid var(--p5-red);
  backdrop-filter: blur(4px);
}

.p5-stripe {
  position: fixed;
  right: 0;
  top: 0;
  bottom: 0;
  width: 5px;
  background: var(--text-primary);
  z-index: 90;
  pointer-events: none;
}

.p5-stripe2 {
  position: fixed;
  right: 9px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: rgba(255, 255, 255, 0.22);
  z-index: 90;
  pointer-events: none;
}

/* PAGE TRANSITION OVERLAYS */
@keyframes p5-stripe-sweep {
  0%   { transform: skewX(-16deg) translateY(-120vh); opacity: 1; }
  42%  { transform: skewX(-16deg) translateY(0vh); opacity: 1; }
  58%  { transform: skewX(-16deg) translateY(0vh); opacity: 1; }
  100% { transform: skewX(-16deg) translateY(120vh); opacity: 0; }
}

@keyframes p5-about-panel-sweep {
  0%   { transform: rotate(-18deg) translateX(-95vw); opacity: 1; }
  65%  { transform: rotate(-18deg) translateX(2vw); opacity: 0.96; }
  100% { transform: rotate(-18deg) translateX(0vw); opacity: 0; }
}

@keyframes p5-resume-card-sweep {
  0%   { transform: translateX(-100vw); opacity: 1; }
  48%  { transform: translateX(3vw); opacity: 1; }
  70%  { transform: translateX(0vw); opacity: 1; }
  100% { transform: translateX(110vw); opacity: 0; }
}

.p5-transition-layer {
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  overflow: hidden;
}

.p5-trans-stripe {
  position: fixed;
  top: -6vh;
  height: 112vh;
  transform-origin: top;
  pointer-events: none;
  animation: p5-stripe-sweep 0.62s cubic-bezier(0.76, 0, 0.24, 1) forwards;
}

.p5-trans-panel {
  position: fixed;
  height: 26vh;
  clip-path: polygon(0 0, 100% 0, calc(100% - 120px) 100%, 0 100%);
  transform-origin: left center;
  pointer-events: none;
  animation: p5-about-panel-sweep 0.56s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

.p5-trans-card {
  position: fixed;
  left: -6vw;
  width: 78vw;
  height: 14vh;
  clip-path: polygon(0 0, 97% 0, 100% 100%, 3% 100%);
  pointer-events: none;
  animation: p5-resume-card-sweep 0.64s cubic-bezier(0.76, 0, 0.24, 1) forwards;
}

/* UNIFIED SIDEBAR MENU WITH EXACT P5Menu.jsx DOM & ANIMATIONS */
@keyframes p5-shadow-pop {
  0%   { transform: translateY(-42%) translateX(-10px) scaleX(0) scaleY(1); }
  55%  { transform: translateY(-48%) translateX(-14px) scaleX(1.18) scaleY(1.16); }
  75%  { transform: translateY(-40%) translateX(-9px) scaleX(0.96) scaleY(0.97); }
  100% { transform: translateY(-42%) translateX(-10px) scaleX(1) scaleY(1); }
}

@keyframes p5-wiggle-poly {
  0%   { clip-path: polygon(0% 56%, 16% 0%, 76% 7%, 100% 24%, 94% 100%, 8% 88%); }
  25%  { clip-path: polygon(0% 62%, 12% 6%, 84% 0%, 100% 34%, 88% 100%, 2% 94%); }
  50%  { clip-path: polygon(0% 40%, 28% 10%, 72% 0%, 100% 44%, 98% 92%, 14% 100%); }
  75%  { clip-path: polygon(0% 52%, 22% 0%, 80% 12%, 100% 28%, 90% 100%, 6% 82%); }
  100% { clip-path: polygon(0% 56%, 16% 0%, 76% 7%, 100% 24%, 94% 100%, 8% 88%); }
}

@keyframes p5-row-mount {
  0%   { opacity: 0; transform: translateX(-28px); }
  100% { opacity: 1; transform: translateX(0); }
}

[data-testid="stSidebar"] {
  background:
    radial-gradient(circle at 50% 24%, rgba(0, 207, 255, 0.35) 0%, transparent 55%),
    repeating-linear-gradient(-35deg, var(--bg-primary) 0px, var(--bg-primary) 14px, var(--bg-chart-deep) 14px, var(--bg-chart-deep) 28px) !important;
  border-right: 4px solid var(--p5-red) !important;
  box-shadow: 8px 0px 0px var(--bg-primary) !important;
}

[data-testid="stSidebar"][data-collapsed="true"] { visibility: hidden; }

[data-testid="stSidebarContent"] {
  padding-top: 0.75rem !important;
}

[data-testid="stSidebarNav"],
[data-testid="stSidebarNavSeparator"] {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
  opacity: 0 !important;
  pointer-events: none !important;
}

.p5-menu-stage {
  position: relative;
  width: 100%;
  min-height: 360px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  background:
    radial-gradient(circle at 75% 42%, rgba(0, 207, 255, 0.45) 0%, rgba(23, 13, 55, 0.28) 45%, rgba(5, 13, 34, 0.95) 80%),
    repeating-linear-gradient(-35deg, var(--bg-primary) 0px, var(--bg-primary) 16px, var(--bg-chart-deep) 16px, var(--bg-chart-deep) 32px);
  border: 3px solid var(--p5-red);
  box-shadow: 7px 7px 0px var(--bg-primary);
  padding: 68px 10px 38px 10px;
  margin-bottom: 1rem;
  clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
  user-select: none;
}

.p5-stage-art {
  position: absolute;
  bottom: -6px;
  right: -18px;
  height: 92%;
  width: auto;
  object-fit: contain;
  pointer-events: none;
  z-index: 2;
  opacity: 0.35;
  filter: drop-shadow(-6px 4px 10px rgba(5, 13, 34, 0.85));
}

.p5-name-tag {
  position: absolute;
  top: 10px;
  left: 14px;
  z-index: 25;
  pointer-events: none;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-style: italic;
  font-size: 30px;
  line-height: 0.86;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--text-primary);
  transform: rotate(-10deg) skewX(-6deg);
  transform-origin: left top;
  display: flex;
  flex-direction: column;
  gap: 2px;
  text-shadow: 3px 3px 0 var(--bg-primary), -1px -1px 0 var(--accent);
}

.p5-name-tag span:nth-child(2) {
  margin-left: 14px;
}

.p5-menu {
  position: relative;
  z-index: 20;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  width: 100%;
  padding: 6px 8px;
}

.p5-row {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none !important;
  cursor: pointer;
  overflow: visible;
  animation: p5-row-mount 0.45s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.p5-glow {
  position: absolute;
  inset: -14px -26px;
  background: radial-gradient(ellipse at 50% 50%, rgba(255, 255, 255, 0.5) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.25s ease;
  pointer-events: none;
  z-index: 0;
}

.p5-row.active .p5-glow,
.p5-row:hover .p5-glow {
  opacity: 1;
}

.p5-skew-wrap {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  overflow: visible;
  isolation: isolate;
}

.p5-shadow-tri {
  position: absolute;
  top: 50%;
  left: -4%;
  width: 108%;
  height: 112%;
  transform-origin: left center;
  background: rgba(255, 255, 255, 0.9);
  clip-path: polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%);
  z-index: 1;
  pointer-events: none;
  transform: translateY(-42%) translateX(-10px) scaleX(0);
  transition: transform 0.18s ease;
}

.p5-row.active .p5-shadow-tri,
.p5-row:hover .p5-shadow-tri {
  animation: p5-shadow-pop 0.28s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

.p5-highlight {
  position: absolute;
  top: 50%;
  left: -4%;
  width: 108%;
  height: 112%;
  transform-origin: left center;
  background: var(--p5-cyan);
  clip-path: polygon(0% 44%, 24% 6%, 82% 0%, 100% 36%, 82% 100%, 18% 94%);
  z-index: 2;
  pointer-events: none;
  transform: translateY(-50%) scaleX(0);
  transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1);
}

.p5-row.active .p5-highlight,
.p5-row:hover .p5-highlight {
  transform: translateY(-50%) scaleX(1);
  animation: p5-wiggle-poly 0.66s ease-in-out infinite;
}

.p5-label-wrap {
  position: relative;
  z-index: 3;
  display: inline-grid;
  place-items: center;
  padding: 4px 10px;
}

.p5-label-base {
  grid-area: 1 / 1;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-style: italic;
  line-height: 0.88;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  white-space: nowrap;
  display: block;
  pointer-events: none;
}

.p5-label-dark {
  color: var(--text-primary);
  -webkit-text-stroke: 9px rgba(5, 13, 34, 0.92);
  paint-order: stroke fill;
  opacity: 1;
  transition: opacity 0.1s ease;
}

.p5-label-bright {
  color: var(--bg-primary);
  -webkit-text-stroke: 9px rgba(255, 255, 255, 0.96);
  paint-order: stroke fill;
  opacity: 0;
  transition: opacity 0.1s ease;
}

.p5-row.active .p5-label-dark,
.p5-row:hover .p5-label-dark {
  opacity: 0;
}

.p5-row.active .p5-label-bright,
.p5-row:hover .p5-label-bright {
  opacity: 1;
}

.p5-hint {
  position: absolute;
  bottom: 8px;
  right: 10px;
  z-index: 20;
  display: flex;
  gap: 8px;
  align-items: center;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 11px;
  letter-spacing: 1.5px;
  color: rgba(255, 255, 255, 0.55);
}

.p5-hint-key {
  border: 1px solid rgba(255, 255, 255, 0.32);
  padding: 1px 5px;
  font-size: 10px;
  color: rgba(255, 255, 255, 0.78);
}

/* HERO STAGE FOR HOME PAGE ("TAKE YOUR HEART") */
.p5-hero {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  background:
    radial-gradient(circle at 78% 45%, rgba(0, 207, 255, 0.48) 0%, rgba(23, 13, 55, 0.25) 42%, rgba(5, 13, 34, 0.96) 78%),
    repeating-linear-gradient(-32deg, var(--bg-primary) 0px, var(--bg-primary) 16px, var(--bg-chart-deep) 16px, var(--bg-chart-deep) 32px);
  border: 3px solid var(--p5-red);
  box-shadow: 10px 10px 0px var(--bg-primary), -3px -3px 0px var(--p5-white);
  padding: 1.6rem 2rem;
  margin-bottom: 1.6rem;
  overflow: hidden;
  clip-path: polygon(0 0, 100% 0, calc(100% - 18px) 100%, 0 100%);
}

.p5-hero-badge {
  display: inline-block;
  background: var(--p5-yellow);
  color: var(--bg-primary);
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-weight: 900;
  letter-spacing: 0.14em;
  padding: 0.22rem 0.85rem;
  transform: skew(-8deg, -1deg);
  box-shadow: 4px 4px 0px var(--bg-primary);
  margin-bottom: 0.6rem;
  font-size: 1rem;
}

.p5-hero-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: clamp(2rem, 3.4vw, 3.1rem);
  line-height: 1.02;
  color: var(--p5-white);
  text-shadow: 4px 4px 0px var(--bg-primary), -2px -2px 0px var(--p5-red);
  margin: 0.2rem 0 0.7rem 0;
  transform: skew(-3deg, 0deg);
}

.p5-hero-sub,
.p5-hero-lead {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1rem;
  line-height: 1.55;
  color: #f2f2f2;
  max-width: 68ch;
  margin: 0;
}

.p5-hero-img {
  max-height: 155px;
  width: auto;
  flex-shrink: 0;
  filter: hue-rotate(195deg) saturate(1.25) drop-shadow(4px 4px 0 var(--bg-primary)) !important;
  transform: rotate(2deg);
  transition: transform 0.22s ease;
}

.p5-hero-img:hover {
  transform: rotate(-3deg) scale(1.06);
}

/* SLIDING PARTY / CONFIDANT BARS */
@keyframes sc-bar-slide-in {
  0%   { transform: translateX(-100%); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}

@keyframes sc-arrow-left {
  0%, 100% { transform: translateX(0); opacity: 1; }
  50%      { transform: translateX(-6px); opacity: 0.35; }
}

@keyframes sc-arrow-right {
  0%, 100% { transform: translateX(0); opacity: 1; }
  50%      { transform: translateX(6px); opacity: 0.35; }
}

@keyframes sc-right-nav-pop {
  0%   { opacity: 0; transform: scale(0.55) translateY(-10px); }
  65%  { opacity: 1; transform: scale(1.05) translateY(2px); }
  100% { opacity: 1; transform: scale(1) translateY(0); }
}

@keyframes sc-infobar-in {
  0%   { opacity: 0; transform: translateX(40px); }
  60%  { opacity: 1; transform: translateX(-4px); }
  100% { opacity: 1; transform: translateX(0); }
}

.sc-root {
  container-type: inline-size;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: 10px;
  margin: 1rem 0 1.6rem 0;
  width: 100%;
}

.sc-bar-outer {
  position: relative;
  width: 100%;
  max-width: 920px;
  cursor: pointer;
  animation: sc-bar-slide-in 0.55s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.sc-bar-outer:nth-child(1) { animation-delay: 0ms; }
.sc-bar-outer:nth-child(2) { animation-delay: 85ms; }
.sc-bar-outer:nth-child(3) { animation-delay: 170ms; }
.sc-bar-outer:nth-child(4) { animation-delay: 255ms; }
.sc-bar-outer:nth-child(5) { animation-delay: 340ms; }

.sc-bar {
  position: relative;
  width: 100%;
  min-height: 72px;
  transition: min-height 0.3s cubic-bezier(0.22, 1, 0.36, 1), transform 0.25s ease;
  background: var(--bg-chart-deep);
  border: 1px solid rgba(255, 255, 255, 0.14);
  clip-path: polygon(0 0, 100% 0, calc(100% - 16px) 100%, 0 100%);
  box-shadow: 0 6px 24px rgba(5, 13, 34, 0.75);
  z-index: 1;
  overflow: hidden;
}

.sc-bar-outer.active .sc-bar,
.sc-bar-outer:hover .sc-bar {
  min-height: 98px;
}

.sc-bar-red {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--primary);
  clip-path: polygon(45% 0, 100% 0, 100% 100%, calc(45% - 12px) 100%);
  transform: translateY(-8px);
  opacity: 0;
  transition: opacity 0.22s ease, height 0.3s cubic-bezier(0.22, 1, 0.36, 1);
  z-index: 0;
  pointer-events: none;
}

.sc-bar-outer.active .sc-bar-red,
.sc-bar-outer:hover .sc-bar-red {
  opacity: 1;
}

.sc-bar-fill {
  position: absolute;
  inset: 0;
  width: 100%;
  background: var(--text-primary);
  clip-path: polygon(100% 0, 100% 0, calc(100% - 32px) 100%, calc(100% - 32px) 100%);
  transition: clip-path 0.36s cubic-bezier(0.22, 1, 0.36, 1);
  z-index: 0;
}

.sc-bar-outer.active .sc-bar-fill,
.sc-bar-outer:hover .sc-bar-fill {
  clip-path: polygon(18% 0, 100% 0, calc(100% - 14px) 100%, calc(18% + 110px) 100%);
}

.sc-bar-shade {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 72%;
  width: 6%;
  background: linear-gradient(90deg, rgba(5, 13, 34, 0.16) 0%, rgba(5, 13, 34, 0) 100%);
  z-index: 1;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.35s ease;
}

.sc-bar-outer.active .sc-bar-shade,
.sc-bar-outer:hover .sc-bar-shade {
  opacity: 1;
}

/* La especificidad evita que las reglas de imágenes de Streamlit amplíen el retrato. */
.sc-root .sc-bar .sc-char {
  position: absolute;
  top: 0;
  left: 88px;
  height: 100%;
  width: 145px;
  max-width: 145px;
  object-fit: cover;
  object-position: 20% top;
  pointer-events: none;
  z-index: 3;
  clip-path: polygon(18px 0%, 100% 0%, calc(100% - 18px) 100%, 0% 100%);
  filter: hue-rotate(195deg) saturate(1.25) drop-shadow(4px 4px 0 var(--bg-primary)) !important;
}

.sc-bar-content {
  position: relative;
  z-index: 4;
  min-height: inherit;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 24px 12px 18px;
  gap: 16px;
}

.sc-role {
  display: flex;
  align-items: center;
  flex-shrink: 0;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 40px;
  letter-spacing: -1px;
  color: var(--text-primary);
  transform: rotate(-24deg);
  user-select: none;
  line-height: 1;
  padding: 0 12px 0 4px;
  text-shadow: 2px 2px 0 var(--bg-primary);
}

.sc-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: 4px;
  margin-left: 80px;
  padding-left: 12px;
  padding-block: 8px;
  padding-right: 12px;
  background: var(--bg-chart-deep);
}

/* Texto y superficie cambian juntos, sin depender del barrido diagonal animado. */
.sc-bar-outer.active .sc-main,
.sc-bar-outer:hover .sc-main,
.sc-bar-outer.active .sc-stats,
.sc-bar-outer:hover .sc-stats {
  background: var(--text-primary);
}

.sc-label {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1.55rem !important;
  letter-spacing: 0.06em !important;
  line-height: 1.15 !important;
  color: var(--accent) !important;
  margin-bottom: 0.25rem !important;
  white-space: normal !important;
}

.sc-subdesc {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 0.88rem !important;
  line-height: 1.4 !important;
  color: #f0f0f0 !important;
}

.sc-bar-outer.active .sc-label,
.sc-bar-outer:hover .sc-label {
  color: var(--bg-primary) !important;
}

.sc-bar-outer.active .sc-subdesc,
.sc-bar-outer:hover .sc-subdesc {
  color: var(--bg-primary) !important;
  font-weight: 500;
}

.sc-stats {
  display: flex;
  align-items: center;
  gap: 12px;
  padding-right: 12px;
  flex-shrink: 0;
  background: var(--bg-chart-deep);
}

/* La barra lateral también reduce el espacio: responder al ancho real de la sección. */
@container (max-width: 760px) {
  .sc-bar-content { flex-wrap: wrap; align-items: flex-start; }
  .sc-main { flex-basis: 100%; margin-left: 0; padding-left: 12px; }
  .sc-stats { flex-wrap: wrap; padding: 8px 12px; max-width: 100%; }
  .sc-root .sc-bar .sc-char, .sc-role { display: none; }
}

.sc-stat {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.sc-stat-top {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.sc-stat-tag {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 11px;
  letter-spacing: 1.5px;
  padding: 1px 5px;
  border: 1px solid var(--primary);
  color: var(--primary);
  line-height: 1.3;
  background: rgba(5, 13, 34, 0.85);
}

.sc-stat-num {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 26px;
  font-style: italic;
  line-height: 1;
  color: var(--text-primary);
  letter-spacing: 1px;
  /* Evita cifras grises sobre el fondo que cambia al entrar o salir el cursor. */
  transition: none;
}

.sc-bar-outer.active .sc-stat-num,
.sc-bar-outer:hover .sc-stat-num {
  color: var(--bg-primary);
}

.sc-stat-bars {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1px;
  margin-top: 2px;
}

.sc-stat-bar-color {
  height: 3px;
  width: 100%;
  background: var(--primary);
}

.sc-stat-bar-black {
  height: 2px;
  width: 100%;
  background: var(--bg-primary);
}

/* Crisp High-Contrast LB / RB Navigation Header */
.sc-right-nav-bar {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 20px;
  background: var(--bg-primary);
  border: 2px solid var(--text-primary);
  clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
  box-shadow: 8px 6px 0 var(--primary);
  animation: sc-right-nav-pop 0.38s cubic-bezier(0.22, 1, 0.36, 1) both;
  margin: 0.4rem 0 1.1rem 0;
}

.sc-right-nav-bar .sc-nav-btn {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 22px;
  font-weight: 900;
  letter-spacing: 2px;
  line-height: 1;
  color: var(--text-primary);
  background: var(--primary);
  padding: 4px 10px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 5px) 100%, 0 100%);
}

.sc-right-nav-bar .sc-nav-label {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 26px;
  letter-spacing: 2.5px;
  line-height: 1;
  color: var(--text-primary);
  padding: 0 6px;
}

.sc-right-nav-bar .sc-nav-arrow {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 20px;
  color: var(--accent);
  display: inline-block;
}

.sc-right-nav-bar .sc-nav-arrow.left  { animation: sc-arrow-left 0.8s ease-in-out infinite; }
.sc-right-nav-bar .sc-nav-arrow.right { animation: sc-arrow-right 0.8s ease-in-out infinite; }

/* Info Bars with NEW badge */
.sc-info-bar-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0.8rem 0 1.4rem 0;
}

.sc-info-bar-wrap {
  position: relative;
  height: 48px;
  background: rgba(0, 12, 29, 0.92);
  border-radius: 7px;
  padding: 1.5px;
  cursor: pointer;
  animation: sc-infobar-in 0.35s cubic-bezier(0.22, 1, 0.36, 1) both;
  transition: transform 0.18s ease, background 0.18s ease;
}

.sc-info-bar-wrap.selected,
.sc-info-bar-wrap:hover {
  background: var(--bg-chart-deep);
  transform: translateX(6px);
}

.sc-info-bar {
  position: relative;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  display: flex;
  align-items: center;
  overflow: hidden;
  transition: background 0.18s ease;
}

.sc-info-bar-wrap.selected .sc-info-bar,
.sc-info-bar-wrap:hover .sc-info-bar {
  background: var(--text-primary);
}

.sc-info-bar-wrap.selected .sc-info-bar::before,
.sc-info-bar-wrap:hover .sc-info-bar::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--primary);
  z-index: 1;
}

.sc-info-bar-new {
  position: absolute;
  left: -18px;
  top: -6px;
  height: 28px;
  width: auto;
  pointer-events: none;
  z-index: 5;
}

.sc-info-bar-icon-wrap {
  width: 44px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-left: 14px;
}

.sc-info-bar-icon {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.sc-info-bar-text {
  flex: 1;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 21px;
  letter-spacing: 0.8px;
  color: var(--text-primary);
  padding: 0 12px;
  transition: color 0.18s ease;
}

.sc-info-bar-wrap.selected .sc-info-bar-text,
.sc-info-bar-wrap:hover .sc-info-bar-text {
  color: var(--bg-primary);
}

.sc-info-bar-box {
  height: 70%;
  background: var(--bg-primary);
  display: flex;
  align-items: center;
  padding: 0 10px;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 18px;
  color: var(--text-primary);
  border-radius: 5px;
  margin-right: 8px;
}

.sc-info-bar-count {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 21px;
  letter-spacing: 1px;
  color: var(--accent);
  margin-right: 16px;
  transition: color 0.18s ease;
}

.sc-info-bar-wrap.selected .sc-info-bar-count,
.sc-info-bar-wrap:hover .sc-info-bar-count {
  color: var(--primary);
}

/* CONFIDANT RANK CARDS & DETAIL PANEL */
@keyframes resume-card-mount {
  0%   { opacity: 0; transform: translateX(-48px); }
  100% { opacity: 1; transform: translateX(0); }
}

.resume-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: 24px;
  align-items: start;
  margin: 1rem 0 1.8rem 0;
}

.resume-stack {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.resume-list-tag {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: clamp(44px, 4.5vw, 68px);
  line-height: 0.9;
  color: var(--text-primary);
  letter-spacing: 2px;
  margin: 0 0 4px 10px;
  text-shadow: 4px 4px 0 var(--bg-primary), -2px -2px 0 var(--primary);
}

.resume-card-wrap {
  position: relative;
  cursor: pointer;
  animation: resume-card-mount 0.42s cubic-bezier(0.22, 1, 0.36, 1) both;
}

.resume-card-wrap:nth-child(2) { animation-delay: 55ms; }
.resume-card-wrap:nth-child(3) { animation-delay: 110ms; }
.resume-card-wrap:nth-child(4) { animation-delay: 165ms; }
.resume-card-wrap:nth-child(5) { animation-delay: 220ms; }

.resume-card {
  position: relative;
  height: 108px;
  background: var(--bg-primary);
  border: 1px solid rgba(255, 255, 255, 0.16);
  clip-path: polygon(0 0, 97% 0, 100% 100%, 3% 100%);
  box-shadow: 0 8px 0 rgba(5, 13, 34, 0.85);
  transition: transform 0.22s ease, background 0.22s ease, box-shadow 0.22s ease;
  overflow: visible;
}

.resume-card-wrap.active .resume-card,
.resume-card-wrap:hover .resume-card {
  background: var(--text-primary);
  box-shadow: 10px 8px 0 var(--primary);
  transform: translateX(8px);
}

.resume-badge {
  position: absolute;
  top: 10px;
  left: 6px;
  width: 52px;
  height: 66px;
  background: var(--bg-primary);
  border: 3px solid var(--text-primary);
  clip-path: polygon(14% 0, 100% 0, 84% 100%, 0 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  transform: rotate(-8deg);
  z-index: 3;
}

.resume-card-wrap.active .resume-badge,
.resume-card-wrap:hover .resume-badge {
  background: var(--bg-primary);
  border-color: var(--primary);
}

.resume-badge-text {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 30px;
  color: var(--text-primary);
  letter-spacing: 1px;
  transform: rotate(8deg);
}

.resume-card-inner {
  position: absolute;
  inset: 0;
  padding: 12px 24px 12px 72px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.resume-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: clamp(32px, 3vw, 44px);
  line-height: 0.9;
  letter-spacing: 1px;
  color: var(--text-primary);
  transition: color 0.22s ease;
}

.resume-card-wrap.active .resume-title,
.resume-card-wrap:hover .resume-title {
  color: var(--bg-primary);
}

.resume-rank {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 2px;
  flex-shrink: 0;
}

.resume-rank-label {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 24px;
  letter-spacing: 2px;
  color: var(--primary);
  transition: color 0.22s ease;
}

.resume-rank-number {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 40px;
  line-height: 0.85;
  color: var(--text-primary);
  transition: color 0.22s ease;
}

.resume-card-wrap.active .resume-rank-number,
.resume-card-wrap:hover .resume-rank-number {
  color: var(--bg-primary);
}

.resume-subtitle-bar {
  position: absolute;
  left: 72px;
  right: 16px;
  bottom: 10px;
  height: 32px;
  background: var(--text-primary);
  clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
  display: flex;
  align-items: center;
  padding: 0 14px;
  transition: background 0.22s ease;
}

.resume-card-wrap.active .resume-subtitle-bar,
.resume-card-wrap:hover .resume-subtitle-bar {
  background: var(--bg-primary);
}

.resume-subtitle {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 21px;
  line-height: 1;
  color: var(--bg-primary);
  transition: color 0.22s ease;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.resume-card-wrap.active .resume-subtitle,
.resume-card-wrap:hover .resume-subtitle {
  color: var(--text-primary);
}

.resume-detail-panel {
  position: relative;
  padding: 22px 24px 24px 24px;
  background: linear-gradient(180deg, rgba(23, 13, 55, 0.96) 0%, rgba(23, 13, 55, 0.98) 100%);
  clip-path: polygon(0 0, 100% 0, calc(100% - 18px) 100%, 0 100%);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.16), 14px 14px 0 rgba(0, 207, 255, 0.75);
  overflow: hidden;
}

.resume-detail-top {
  position: relative;
  display: grid;
  grid-template-columns: 64px 1fr auto;
  align-items: center;
  gap: 12px;
  min-height: 80px;
  padding: 0 18px;
  background: var(--text-primary);
  clip-path: polygon(0 0, 100% 0, calc(100% - 16px) 100%, 0 100%);
  color: var(--bg-primary);
  box-shadow: 10px 0 0 rgba(0, 207, 255, 0.92);
}

.resume-detail-top-index {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 40px;
  line-height: 1;
  color: var(--bg-primary);
}

.resume-detail-top-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 32px;
  line-height: 0.92;
  letter-spacing: 1px;
  color: var(--bg-primary);
}

.resume-detail-top-progress {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 32px;
  letter-spacing: 2px;
  line-height: 1;
  color: var(--primary);
}

.resume-detail-list {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 9px;
  margin-top: 16px;
}

.resume-detail-row {
  display: grid;
  grid-template-columns: 44px 1fr auto;
  align-items: center;
  gap: 12px;
  min-height: 50px;
  padding: 0 14px;
  background: rgba(5, 13, 34, 0.96);
  clip-path: polygon(0 0, 100% 0, calc(100% - 12px) 100%, 0 100%);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.12);
  transition: transform 0.16s ease, background 0.16s ease;
}

.resume-detail-row:hover {
  transform: translateX(6px);
  background: rgba(0, 207, 255, 0.18);
}

.resume-detail-row-index {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 24px;
  color: var(--primary);
}

.resume-detail-row-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 23px;
  line-height: 1;
  color: var(--text-primary);
}

.resume-detail-status {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 20px;
  line-height: 1;
  letter-spacing: 1px;
  color: var(--bg-primary);
  background: var(--text-primary);
  padding: 6px 12px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
}

/* SIDE PROJECTS / ALGORITHM LOG SHELL */
.sp-shell {
  display: grid;
  grid-template-columns: 46% 54%;
  gap: 20px;
  margin: 1rem 0 1.6rem 0;
}

.sp-left {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sp-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: clamp(42px, 4.2vw, 60px);
  color: var(--text-primary);
  line-height: 0.92;
  letter-spacing: 1px;
  text-shadow: 4px 4px 0 var(--bg-primary), -2px -2px 0 var(--primary);
  margin-bottom: 4px;
}

.sp-item {
  position: relative;
  min-height: 86px;
  background: rgba(5, 13, 34, 0.94);
  clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.14), 0 8px 16px rgba(5, 13, 34, 0.45);
  padding: 12px 16px;
  cursor: pointer;
  transition: transform 0.24s ease, background 0.24s ease, box-shadow 0.24s ease;
}

.sp-item.active,
.sp-item:hover {
  background: rgba(255, 255, 255, 0.97);
  transform: translateX(8px);
  box-shadow: 8px 8px 0 var(--primary);
}

.sp-item-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 32px;
  line-height: 0.92;
  color: var(--text-primary);
}

.sp-item.active .sp-item-title,
.sp-item:hover .sp-item-title {
  color: #111111;
}

.sp-item-stack {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 22px;
  letter-spacing: 1.4px;
  color: var(--primary);
  margin-top: 4px;
}

.sp-item.active .sp-item-stack,
.sp-item:hover .sp-item-stack {
  color: var(--bg-primary);
}

.sp-right {
  position: relative;
  background: linear-gradient(180deg, rgba(5, 13, 34, 0.96) 0%, rgba(0, 12, 29, 0.98) 100%);
  clip-path: polygon(0 0, 100% 0, calc(100% - 18px) 100%, 0 100%);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.16), 12px 12px 0 var(--primary);
  padding: 24px;
  overflow: hidden;
}

.sp-tag {
  display: inline-block;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 22px;
  letter-spacing: 1.6px;
  background: var(--text-primary);
  color: var(--bg-primary);
  padding: 4px 12px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
}

.sp-right-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: clamp(34px, 3.4vw, 50px);
  line-height: 0.92;
  color: var(--text-primary);
  margin-top: 14px;
}

.sp-right-summary {
  margin-top: 14px;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 26px;
  line-height: 1.15;
  letter-spacing: 1px;
  color: var(--text-primary);
}

.sp-link {
  margin-top: 18px;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 22px;
  color: var(--text-primary);
  background: var(--primary);
  display: inline-flex;
  align-items: center;
  padding: 6px 14px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
}

/* FLOATING BGM PANEL */
.bgm-panel {
  position: fixed;
  left: 20px;
  bottom: 20px;
  z-index: 9990;
  display: flex;
  align-items: center;
  gap: 0;
  background: rgba(5, 13, 34, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 8px 10px;
  clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
  backdrop-filter: blur(4px);
  transition: gap 0.35s cubic-bezier(0.22, 1, 0.36, 1);
  box-shadow: 6px 6px 0 var(--bg-primary);
}

.bgm-panel:hover,
.bgm-panel:focus-within {
  gap: 10px;
}

.bgm-toggle {
  border: 1px solid rgba(255, 255, 255, 0.45);
  background: rgba(5, 13, 34, 0.9);
  color: var(--text-primary);
  padding: 8px 12px;
  min-width: 90px;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 16px;
  letter-spacing: 1.5px;
  font-weight: 700;
  cursor: pointer;
  clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
  transition: transform 0.15s ease, background 0.2s ease, color 0.2s ease;
}

.bgm-toggle:hover {
  transform: translateY(-1px);
}

.bgm-toggle.on {
  background: rgba(0, 207, 255, 0.96);
  color: var(--text-primary);
}

.bgm-slider {
  width: 100%;
  accent-color: var(--primary);
  cursor: pointer;
}

.bgm-slider-wrap {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  border: 1px solid rgba(255, 255, 255, 0.4);
  background: rgba(5, 13, 34, 0.85);
  clip-path: polygon(0 0, 100% 0, calc(100% - 8px) 100%, 0 100%);
  max-width: 0;
  padding: 0;
  border-width: 0;
  opacity: 0;
  overflow: hidden;
  white-space: nowrap;
  transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
  font-family: 'ComicProyecto', system-ui, sans-serif;
  color: var(--text-primary);
}

.bgm-panel:hover .bgm-slider-wrap,
.bgm-panel:focus-within .bgm-slider-wrap {
  max-width: 210px;
  padding: 6px 10px;
  border-width: 1px;
  opacity: 1;
}

/* HEADINGS, BANNERS, CALLING CARDS & BATTLE MENU */
h1, .p5-font {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size-adjust: from-font;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--p5-white) !important;
  text-shadow: 4px 4px 0px var(--bg-primary), -2px -2px 0px var(--p5-red);
}

h2, h3 {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--p5-white) !important;
  text-shadow: 3px 3px 0px var(--bg-primary);
}

.p5-banner {
  position: relative;
  display: inline-block;
  background: linear-gradient(110deg, var(--bg-panel) 0%, var(--purple-deep) 68%, var(--bg-chart) 100%);
  color: var(--p5-white);
  padding: 0.55rem 1.6rem;
  margin: 0.85rem 0 1.15rem 0;
  transform: skew(-5deg, 1.5deg);
  clip-path: polygon(0% 10%, 98% 0%, 100% 90%, 2% 100%);
  border: 2px solid var(--p5-white);
  box-shadow: 6px 6px 0px var(--bg-primary);
}

.p5-banner-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: clamp(1.4rem, 2.3vw, 2rem);
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--p5-white);
  text-shadow: 3px 3px 0px var(--bg-primary);
  margin: 0;
}

.p5-banner-sub {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1rem;
  letter-spacing: 0.12em;
  color: var(--p5-yellow);
  text-transform: uppercase;
  margin-top: 2px;
}

.p5-card {
  background: var(--p5-surface);
  border: 2px solid var(--p5-red);
  box-shadow: 6px 6px 0px var(--bg-primary);
  padding: 1.25rem 1.4rem;
  margin-bottom: 1.15rem;
  position: relative;
  clip-path: polygon(0 0, 100% 0, calc(100% - 12px) 100%, 0 100%);
}

.p5-card-accent {
  background: linear-gradient(145deg, var(--bg-chart) 0%, var(--bg-chart-deep) 100%);
  border: 2px solid var(--p5-white);
  border-left: 7px solid var(--p5-red);
  box-shadow: 6px 6px 0px var(--p5-red);
  padding: 1.2rem 1.4rem;
  margin-bottom: 1.15rem;
}

.p5-callout-warning {
  background: linear-gradient(135deg, var(--bg-chart-deep) 0%, var(--bg-chart) 100%);
  border: 2px solid var(--p5-red);
  border-left: 9px solid var(--p5-yellow);
  box-shadow: 8px 8px 0px var(--bg-primary);
  padding: 1.2rem 1.45rem;
  margin: 1.2rem 0;
  clip-path: polygon(0 0, 100% 0, calc(100% - 14px) 100%, 0 100%);
}

.p5-callout-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1.4rem;
  color: var(--p5-yellow);
  letter-spacing: 0.08em;
  margin-bottom: 0.45rem;
  text-shadow: 2px 2px 0px var(--bg-primary);
}

/* 5. Grid de 4 KPIs en Acerca del Modelo (.p5-kpi-grid): evitar palabras rotas */
.p5-kpi-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
  gap: 1rem !important;
}

.p5-kpi-card {
  background: linear-gradient(155deg, var(--bg-primary) 0%, var(--bg-chart-deep) 100%);
  border: 2px solid var(--p5-red);
  box-shadow: 6px 6px 0px var(--bg-primary);
  padding: 1rem 1.15rem !important;
  transform: skew(-3deg, 0.6deg);
  clip-path: polygon(0% 6%, 98% 0%, 100% 94%, 2% 100%);
  transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
  overflow-wrap: break-word !important;
}

.p5-kpi-card:hover {
  transform: skew(-5deg, 1deg) translateY(-4px);
  border-color: var(--p5-white);
  box-shadow: 9px 9px 0px var(--p5-red);
}

.p5-kpi-label {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1.05rem;
  letter-spacing: 0.09em;
  color: var(--p5-yellow);
  text-transform: uppercase;
  margin-bottom: 0.25rem;
}

.p5-kpi-value {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1.65rem !important;
  line-height: 1.15 !important;
  word-break: keep-all !important;
  color: var(--p5-white);
  text-shadow: 3px 3px 0px var(--bg-primary);
}

.p5-kpi-note {
  font-size: 0.84rem;
  color: #cccccc;
  margin-top: 0.25rem;
}

/* Buttons & Battle Menu Form Submit */
.stButton > button,
.stDownloadButton > button,
[data-testid="stFormSubmitButton"] > button {
  background-color: var(--p5-black) !important;
  color: var(--p5-white) !important;
  border: 2px solid var(--p5-red) !important;
  box-shadow: 6px 6px 0px var(--p5-red) !important;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1.25rem !important;
  letter-spacing: 0.09em !important;
  text-transform: uppercase !important;
  padding: 0.6rem 1.5rem !important;
  border-radius: 0px !important;
  clip-path: polygon(0 0, 100% 0, calc(100% - 10px) 100%, 0 100%);
  transform: skew(-6deg, 0deg);
  transition: all 0.16s cubic-bezier(0.22, 1, 0.36, 1) !important;
  cursor: pointer !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {
  background-color: var(--p5-white) !important;
  color: var(--p5-black) !important;
  border-color: var(--p5-red) !important;
  box-shadow: 8px 8px 0px var(--p5-red) !important;
  transform: skew(-9deg, -1.5deg) translateX(4px) scale(1.03);
}

.stButton > button:hover *,
.stDownloadButton > button:hover *,
[data-testid="stFormSubmitButton"] > button:hover * {
  color: var(--p5-black) !important;
}

[data-testid="stForm"] {
  background: linear-gradient(155deg, var(--bg-primary) 0%, var(--bg-chart-deep) 100%) !important;
  border: 3px solid var(--p5-red) !important;
  box-shadow: 10px 10px 0px var(--bg-primary) !important;
  border-radius: 0px !important;
  clip-path: polygon(0 0, 100% 0, calc(100% - 16px) 100%, 0 100%);
  padding: 1.5rem !important;
}

.p5-prob-row {
  margin-bottom: 0.85rem;
}

.p5-prob-header {
  display: flex;
  justify-content: space-between;
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 1.25rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 0.25rem;
}

.p5-prob-track {
  width: 100%;
  height: 24px;
  background: var(--bg-primary);
  border: 2px solid var(--p5-white);
  box-shadow: 4px 4px 0px var(--bg-primary);
  transform: skew(-8deg, 0deg);
  overflow: hidden;
  position: relative;
}

.p5-prob-fill {
  height: 100%;
  background: repeating-linear-gradient(
    -45deg,
    var(--p5-red),
    var(--p5-red) 12px,
    #009cd1 12px,
    #009cd1 24px
  );
  border-right: 3px solid var(--p5-yellow);
  transition: width 0.35s ease;
}

.p5-critical-alert {
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-chart) 60%, var(--primary) 100%);
  border: 4px solid var(--p5-yellow);
  box-shadow: 10px 10px 0px var(--bg-primary);
  padding: 2rem;
  margin: 1.5rem 0;
  transform: skew(-2deg, 0.5deg);
}

.p5-critical-title {
  font-family: 'ComicProyecto', system-ui, sans-serif;
  font-size: 2.5rem;
  color: var(--p5-yellow);
  text-shadow: 4px 4px 0px var(--bg-primary);
  margin: 0 0 0.75rem 0;
}

.p5-legal-footer {
  background: var(--bg-primary);
  border: 2px solid var(--p5-gray);
  border-left: 6px solid var(--p5-red);
  box-shadow: 5px 5px 0px var(--bg-primary);
  padding: 0.9rem 1.2rem;
  margin-top: 1.5rem;
  font-style: italic;
  color: #e0e0e0;
  font-size: 0.94rem;
}

/* RESPONSIVE AJUSTES */
@media (max-width: 900px) {
  .resume-grid,
  .sp-shell,
  .p5-hero-grid {
    grid-template-columns: 1fr;
  }
  .sc-main {
    margin-left: 0;
    padding-left: 16px;
  }
  .sc-root .sc-bar .sc-char {
    display: none;
  }
}

.p5-name-tag { top: 20px; left: 18px; font-size: 24px; line-height: 1.1; transform: rotate(-4deg); }
.p5-menu-stage { padding-top: 88px; }
[data-testid="stMainBlockContainer"] {
  padding: clamp(1.5rem, 3vw, 3rem) clamp(1.25rem, 3.5vw, 4rem) 7rem;
  max-width: 1560px;
}
.resume-grid { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 2rem; padding: .5rem .75rem 1.5rem; }
.sp-shell { grid-template-columns: minmax(0, .9fr) minmax(0, 1.1fr); gap: 2rem; padding: .5rem .75rem 1.5rem; }
.resume-grid > *, .sp-shell > *, .sc-main { min-width: 0; }
.resume-detail-panel, .sp-right { padding: clamp(1.25rem, 2.2vw, 2rem); }
.resume-detail-row { grid-template-columns: 1.5rem minmax(0, 1fr); padding: 1rem; row-gap: .75rem; }
.resume-detail-status { grid-column: 2; justify-self: start; max-width: 100%; overflow-wrap: anywhere; }
.resume-detail-top { grid-template-columns: 2rem minmax(0, 1fr); padding: 1rem; gap: .75rem; }
.resume-detail-top-progress { grid-column: 2; }
.resume-detail-row-title, .sp-right-summary { font-family: 'ComicProyecto', system-ui, sans-serif; font-size: 1rem; line-height: 1.6; letter-spacing: normal; }
.sp-item { padding: 1.25rem 1.5rem; }
.sp-item-title { font-size: clamp(20px, 1.7vw, 28px); line-height: 1.2; }
.sp-item-title, .sp-right-title, .p5-kpi-value, .sp-link { overflow-wrap: anywhere; }
.sp-link { display: block; font-family: 'ComicProyecto', system-ui, sans-serif; font-size: .875rem; line-height: 1.5; letter-spacing: normal; padding: 1rem; }
.sp-item-stack { font-family: 'ComicProyecto', system-ui, sans-serif; font-size: .95rem; line-height: 1.5; letter-spacing: normal; }
.sp-item:not(.active):not(:hover) .sp-item-stack { color: var(--secondary); }
.sc-root { padding: .75rem .75rem 1.5rem; }
.sc-bar-content { padding-block: 1rem; }
.p5-banner { margin-block: 2rem 1.25rem; padding: 1rem 1.5rem; }
.p5-hero-sub { max-width: 72ch; }
.p5-kpi-note { color: #dedede; line-height: 1.5; }
[data-testid="stTabs"] [role="tablist"] { gap: .5rem; flex-wrap: wrap; height: auto; padding: .5rem; }
[data-testid="stTabs"] [role="tab"] { min-height: 44px; padding: .75rem 1.25rem; white-space: normal; }
[data-testid="stTabs"] [role="tabpanel"] { padding-top: 1.5rem; }
.resume-card-wrap:focus-visible, .sp-item:focus-visible, .sc-bar-outer:focus-visible,
.sc-info-bar-wrap:focus-visible, .p5-row:focus-visible {
  outline: 3px solid var(--p5-cyan); outline-offset: 6px;
}
[hidden] { display: none !important; }
::selection { background: var(--p5-yellow); color: var(--p5-black); }
input, textarea { caret-color: var(--p5-cyan); }
@media (max-width: 1100px) {
  .resume-grid, .sp-shell { grid-template-columns: minmax(0, 1fr); }
}
@media (max-width: 640px) {
  [data-testid="stMainBlockContainer"] { padding: 1.5rem 1rem 7rem; }
  .sc-bar-content { flex-wrap: wrap; padding: 1rem; gap: 1rem; }
  .sc-main { padding-left: 0; }
  .sc-stats { flex-wrap: wrap; }
  .sc-role, .sc-char { display: none; }
  .sc-label { font-size: 1.5rem; line-height: 1.2; }
  .sc-subdesc { font-size: .95rem; line-height: 1.5; }
  .p5-hero { padding: 1.5rem; }
  .p5-hero-img { display: none; }
  .bgm-panel { max-width: calc(100vw - 2rem); left: auto; right: 1rem; bottom: 1rem; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  .p5-transition-layer { display: none; }
}
/* Fuente cómic local: se conserva el tamaño y la jerarquía de cada componente. */
html, body, .stApp { font-family: 'ComicProyecto', system-ui, sans-serif; font-synthesis: weight; }
.stApp :where(h1, h2, h3, h4, h5, h6, p, label, input, textarea, button, select, li, th, td),
.stApp [data-baseweb="select"], .stApp [role="option"] {
  font-family: 'ComicProyecto', system-ui, sans-serif !important;
}
.stApp :where(h1, h2, h3, h4) { text-wrap: balance; }
.stApp p { text-wrap: pretty; }

/* Los valores del deslizador deben conservar sus cifras en una sola línea. */
.stApp [data-testid="stSlider"] [data-testid="stMarkdownContainer"] p {
  white-space: nowrap;
  word-break: normal;
  overflow-wrap: normal;
}
.stApp [data-testid="stSlider"] label [data-testid="stMarkdownContainer"] p {
  white-space: normal;
}

@media (max-width: 600px) {
  /* La fuente cómic es más ancha: los títulos largos deben caber en móvil. */
  .stApp h1 {
    font-size: clamp(1.7rem, 7vw, 2.25rem) !important;
    line-height: 1.25 !important;
    letter-spacing: 0.01em !important;
    overflow-wrap: anywhere;
  }
}
@media (max-width: 600px) {
  .stApp [data-testid="stMainBlockContainer"] {
    padding-left: 2.5rem !important;
  }
}

/* Superficies compartidas de la identidad azul y morada. */
.stApp [data-testid="stPlotlyChart"] {
  border: 1px solid var(--border-purple);
  border-radius: 12px;
  overflow: hidden;
  background: var(--bg-chart-deep);
}
.p5-banner { border-color: var(--border-purple); }
.stApp :is(input, textarea, select) { caret-color: var(--primary); }
.stApp :is(button, input, textarea, select, a):focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 3px;
}
.stApp [data-baseweb="popover"] { background: var(--bg-panel); }

/* Los gráficos y los controles se ajustan al espacio disponible en su columna. */
.stApp [data-testid="stColumn"],
.stApp [data-testid="stPlotlyChart"] { min-width: 0; max-width: 100%; }
.stApp [data-testid="stMetricValue"] > div,
.stApp [data-testid="stMetricLabel"] p {
  white-space: normal;
  overflow-wrap: anywhere;
}
.p5-banner, .sc-right-nav-bar { max-width: 100%; }
.sc-right-nav-bar .sc-nav-label { min-width: 0; overflow-wrap: anywhere; }
.resume-card-inner { gap: .5rem; }
.resume-title { min-width: 0; overflow-wrap: anywhere; }
.resume-subtitle { white-space: normal; font-size: .95rem; line-height: 1.25; }
.resume-subtitle-bar { height: auto; min-height: 32px; padding-block: .35rem; }

@media (max-width: 800px) {
  .stApp [data-testid="stHorizontalBlock"] { flex-wrap: wrap; }
  .stApp [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    flex: 1 1 100%;
    width: 100%;
  }
  .p5-banner { transform: none; clip-path: none; padding: .8rem 1rem; }
  .p5-banner-title { font-size: clamp(1.1rem, 4vw, 1.5rem); overflow-wrap: anywhere; }
  .p5-banner-sub { font-size: .83rem; letter-spacing: .04em; }
  .sc-right-nav-bar .sc-nav-label { font-size: clamp(.9rem, 3vw, 1.25rem); letter-spacing: .06em; }
  .resume-card { height: auto; min-height: 106px; clip-path: none; }
  .resume-card-inner { position: relative; flex-wrap: wrap; padding-right: .75rem; }
  .resume-title { font-size: 1.35rem; line-height: 1.15; }
  .resume-rank-label { font-size: .8rem; letter-spacing: 0; }
  .resume-rank-number { font-size: 1.3rem; }
  .resume-subtitle-bar { position: static; margin: 0 .5rem .5rem 72px; }
}

@media (max-width: 800px) {
  .stApp .st-key-dashboard_indicadores [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    flex: 1 1 calc(50% - .5rem);
    width: calc(50% - .5rem);
  }
  .st-key-dashboard_indicadores [data-testid="stMetricValue"] > div { font-size: 1.25rem; }
}

````

