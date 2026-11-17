// Delegación persistente e interfaz accesible de pestañas tras cada rerender.
(() => {
  try {
    const groups = [
      {
        rootSelector: '.resume-grid',
        listSelector: '.resume-stack',
        labelSelector: '.resume-list-tag',
        tabSelector: '.resume-card-wrap',
        panelSelector: '[data-detail-id]',
        targetAttr: 'detailTarget',
        panelAttr: 'detailId',
        fallbackLabel: 'Indicadores clave del catálogo',
        storageKey: 'p5-tab-resume',
      },
      {
        rootSelector: '.sp-shell',
        listSelector: '.sp-left',
        labelSelector: '.sp-title',
        tabSelector: '.sp-item',
        panelSelector: '[data-sp-id]',
        targetAttr: 'spTarget',
        panelAttr: 'spId',
        fallbackLabel: 'Comparativa de algoritmos',
        storageKey: 'p5-tab-algo',
      },
    ];

    if (win.__p5Interactions) win.__p5Interactions.abort();
    if (win.__p5Observer) win.__p5Observer.disconnect();
    if (win.__p5DecorateTimer) win.clearTimeout(win.__p5DecorateTimer);

    const controller = new win.AbortController();
    win.__p5Interactions = controller;
    const options = {signal: controller.signal};
    let observer = null;
    let isMutatingDom = false;

    function safeStorageGet(key) {
      try {
        return win.sessionStorage.getItem(key);
      } catch (err) {
        return null;
      }
    }

    function safeStorageSet(key, val) {
      try {
        win.sessionStorage.setItem(key, val);
      } catch (err) {}
    }

    function findGroupForTab(tabEl) {
      for (const grp of groups) {
        if (tabEl.matches(grp.tabSelector)) {
          const root = tabEl.closest(grp.rootSelector);
          if (root) return {grp, root};
        }
      }
      return null;
    }

    function syncGroup(grp, root, activeTarget, shouldSave) {
      const tabs = [...root.querySelectorAll(grp.tabSelector)];
      const panels = [...root.querySelectorAll(grp.panelSelector)];
      if (!tabs.length) return;

      const listEl = root.querySelector(grp.listSelector);
      if (listEl) {
        listEl.setAttribute('role', 'tablist');
        listEl.setAttribute('aria-orientation', 'vertical');
        const labelEl = listEl.querySelector(grp.labelSelector);
        if (labelEl) {
          labelEl.setAttribute('aria-hidden', 'true');
          const tagText = (labelEl.textContent || '').trim();
          listEl.setAttribute('aria-label', tagText || grp.fallbackLabel);
        } else {
          listEl.setAttribute('aria-label', grp.fallbackLabel);
        }
      }

      const validTargets = tabs.map(t => t.dataset[grp.targetAttr]).filter(Boolean);
      let chosen = activeTarget;
      if (!chosen || !validTargets.includes(chosen)) {
        const currentTab = tabs.find(t => t.classList.contains('active'));
        chosen = (currentTab && currentTab.dataset[grp.targetAttr]) || validTargets[0];
      }
      if (!chosen) return;

      tabs.forEach(tab => {
        const targetId = tab.dataset[grp.targetAttr];
        const selected = targetId === chosen;
        tab.id = tab.id || `p5-tab-${targetId}`;
        tab.setAttribute('role', 'tab');
        tab.removeAttribute('aria-pressed');
        tab.setAttribute('aria-selected', String(selected));
        tab.setAttribute('tabindex', selected ? '0' : '-1');
        tab.classList.toggle('active', selected);
      });

      panels.forEach(panel => {
        const panelId = panel.dataset[grp.panelAttr];
        const selected = panelId === chosen;
        const ownerTab = tabs.find(t => t.dataset[grp.targetAttr] === panelId);
        panel.setAttribute('role', 'tabpanel');
        if (ownerTab && ownerTab.id) {
          panel.setAttribute('aria-labelledby', ownerTab.id);
        }
        panel.hidden = !selected;
        panel.style.display = selected ? 'block' : 'none';
        if (selected) {
          panel.setAttribute('tabindex', '0');
        } else {
          panel.removeAttribute('tabindex');
        }
      });

      if (shouldSave) {
        safeStorageSet(`${win.location.pathname}::${grp.storageKey}`, chosen);
      }
    }

    function decorate() {
      if (isMutatingDom) return;
      isMutatingDom = true;
      try {
        groups.forEach(grp => {
          doc.querySelectorAll(grp.rootSelector).forEach(root => {
            const saved = safeStorageGet(`${win.location.pathname}::${grp.storageKey}`);
            syncGroup(grp, root, saved, false);
          });
        });
      } catch (err) {
      } finally {
        isMutatingDom = false;
      }
    }

    function scheduleDecorate() {
      if (isMutatingDom) return;
      if (win.__p5DecorateTimer) win.clearTimeout(win.__p5DecorateTimer);
      win.__p5DecorateTimer = win.setTimeout(() => {
        win.__p5DecorateTimer = null;
        decorate();
      }, 45);
    }

    doc.addEventListener('click', event => {
      try {
        const tabEl = event.target.closest('.resume-card-wrap, .sp-item');
        if (tabEl) {
          const match = findGroupForTab(tabEl);
          if (match) {
            syncGroup(match.grp, match.root, tabEl.dataset[match.grp.targetAttr], true);
            if (typeof win.playSelectSound === 'function') win.playSelectSound();
            return;
          }
        }
        if (event.target.closest('.p5-row, .stButton button, [data-testid="stFormSubmitButton"] button')) {
          if (typeof win.playSelectSound === 'function') win.playSelectSound();
        }
      } catch (err) {}
    }, options);

    doc.addEventListener('keydown', event => {
      try {
        const tabEl = event.target.closest('.resume-card-wrap, .sp-item');
        if (!tabEl) return;
        const match = findGroupForTab(tabEl);
        if (!match) return;
        const {grp, root} = match;
        const tabs = [...root.querySelectorAll(grp.tabSelector)];
        if (!tabs.length) return;
        const idx = tabs.indexOf(tabEl);
        let nextTab = null;

        if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
          nextTab = tabs[(idx - 1 + tabs.length) % tabs.length];
        } else if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
          nextTab = tabs[(idx + 1) % tabs.length];
        } else if (event.key === 'Home') {
          nextTab = tabs[0];
        } else if (event.key === 'End') {
          nextTab = tabs[tabs.length - 1];
        } else if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          syncGroup(grp, root, tabEl.dataset[grp.targetAttr], true);
          if (typeof win.playSelectSound === 'function') win.playSelectSound();
          return;
        }

        if (nextTab) {
          event.preventDefault();
          syncGroup(grp, root, nextTab.dataset[grp.targetAttr], true);
          nextTab.focus();
        }
      } catch (err) {}
    }, options);

    controller.signal.addEventListener('abort', () => {
      if (win.__p5DecorateTimer) {
        win.clearTimeout(win.__p5DecorateTimer);
        win.__p5DecorateTimer = null;
      }
      if (observer) observer.disconnect();
    });

    const targetRoot = doc.querySelector('[data-testid="stAppViewContainer"]') || doc.body;
    if (targetRoot && typeof win.MutationObserver === 'function') {
      observer = new win.MutationObserver(scheduleDecorate);
      observer.observe(targetRoot, {childList: true, subtree: true});
      win.__p5Observer = observer;
    }
    decorate();
  } catch (err) {}
})();
