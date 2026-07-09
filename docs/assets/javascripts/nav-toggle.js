/*
 * Botones "Expandir todo" / "Colapsar todo" para el menú de navegación
 * lateral de MkDocs Material. El tema no trae este control de fábrica;
 * el menú usa checkboxes ocultos (input.md-nav__toggle) para controlar
 * qué secciones están abiertas — esta barra simplemente los marca o
 * desmarca todos a la vez.
 */
(function () {
  function initNavToggleBar() {
    var sidebar = document.querySelector(
      ".md-sidebar--primary .md-sidebar__scrollwrap"
    );
    if (!sidebar || sidebar.querySelector(".nav-toggle-bar")) {
      return;
    }

    var nav = sidebar.querySelector(".md-nav--primary");
    if (!nav) {
      return;
    }

    var bar = document.createElement("div");
    bar.className = "nav-toggle-bar";

    var expandBtn = document.createElement("button");
    expandBtn.type = "button";
    expandBtn.className = "nav-toggle-btn";
    expandBtn.textContent = "Expandir todo";
    expandBtn.setAttribute("aria-label", "Expandir todas las secciones del menú");

    var collapseBtn = document.createElement("button");
    collapseBtn.type = "button";
    collapseBtn.className = "nav-toggle-btn";
    collapseBtn.textContent = "Colapsar todo";
    collapseBtn.setAttribute("aria-label", "Colapsar todas las secciones del menú");

    function setAll(checked) {
      var toggles = nav.querySelectorAll("input.md-nav__toggle");
      toggles.forEach(function (input) {
        input.checked = checked;
      });
    }

    expandBtn.addEventListener("click", function () {
      setAll(true);
    });
    collapseBtn.addEventListener("click", function () {
      setAll(false);
    });

    bar.appendChild(expandBtn);
    bar.appendChild(collapseBtn);
    nav.parentNode.insertBefore(bar, nav);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initNavToggleBar);
  } else {
    initNavToggleBar();
  }
})();
