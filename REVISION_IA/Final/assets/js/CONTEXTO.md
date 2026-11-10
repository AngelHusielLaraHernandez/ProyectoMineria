# Carpeta: Final/assets/js

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## interacciones.js

Ruta: `Final/assets/js/interacciones.js` · Bytes: 3420 · SHA-256: `3cccdd60929a1a661ff15ffd2aeb2e7e71bb19bd8c0b0b3a3e49fa7e1d773f38`

````text
// Delegación persistente: los submenús siguen respondiendo tras cada rerender.
(() => {
  const selector = '.resume-card-wrap, .sp-item, .sc-bar-outer, .sc-info-bar-wrap';
  if (win.__p5Interactions) win.__p5Interactions.abort();
  if (win.__p5Observer) win.__p5Observer.disconnect();
  const controller = new win.AbortController();
  win.__p5Interactions = controller;
  const options = {signal: controller.signal};

  function activate(item) {
    const isCard = item.matches('.resume-card-wrap');
    const isProject = item.matches('.sp-item');
    const root = item.closest(isCard ? '.resume-grid' : isProject ? '.sp-shell' :
      item.matches('.sc-bar-outer') ? '.sc-root' : '.sc-info-bar-list');
    if (!root) return;
    const type = isCard ? '.resume-card-wrap' : isProject ? '.sp-item' :
      item.matches('.sc-bar-outer') ? '.sc-bar-outer' : '.sc-info-bar-wrap';
    const activeClass = type === '.sc-info-bar-wrap' ? 'selected' : 'active';
    root.querySelectorAll(type).forEach(sibling => {
      const selected = sibling === item;
      sibling.classList.toggle(activeClass, selected);
      sibling.setAttribute('aria-pressed', String(selected));
    });
    if (isCard || isProject) {
      const target = isCard ? item.dataset.detailTarget : item.dataset.spTarget;
      root.querySelectorAll(isCard ? '[data-detail-id]' : '[data-sp-id]').forEach(panel => {
        const selected = (isCard ? panel.dataset.detailId : panel.dataset.spId) === target;
        panel.style.display = selected ? 'block' : 'none';
        panel.hidden = !selected;
      });
    }
  }

  function decorate() {
    doc.querySelectorAll(selector).forEach(item => {
      item.setAttribute('role', 'button');
      item.setAttribute('tabindex', '0');
      item.setAttribute('aria-pressed', String(item.classList.contains('active') || item.classList.contains('selected')));
    });
  }
  doc.addEventListener('click', event => {
    const item = event.target.closest(selector);
    if (item) { activate(item); win.playSelectSound(); }
    if (event.target.closest('.p5-row, .stButton button, [data-testid="stFormSubmitButton"] button')) win.playSelectSound();
  }, options);
  doc.addEventListener('mouseover', event => {
    const item = event.target.closest(selector);
    if (item && !item.contains(event.relatedTarget)) activate(item);
  }, options);
  doc.addEventListener('focusin', event => {
    const item = event.target.closest(selector);
    if (item) activate(item);
  }, options);
  doc.addEventListener('keydown', event => {
    const item = event.target.closest(selector);
    if (!item) return;
    if (['Enter', ' '].includes(event.key)) {
      event.preventDefault(); activate(item);
    } else if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
      const parent = item.parentElement;
      const items = [...parent.querySelectorAll(selector)].filter(node => node.parentElement === parent);
      const direction = ['ArrowUp', 'ArrowLeft'].includes(event.key) ? -1 : 1;
      const next = items[(items.indexOf(item) + direction + items.length) % items.length];
      if (next) { event.preventDefault(); next.focus(); }
    }
  }, options);
  const observer = new win.MutationObserver(decorate);
  observer.observe(doc.querySelector('[data-testid="stAppViewContainer"]') || doc.body,
    {childList: true, subtree: true});
  win.__p5Observer = observer;
  decorate();
})();

````

