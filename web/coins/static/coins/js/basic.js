// Función para inicializar el menú
function initMenu() {
  // Selecciona todos los elementos con la clase "accordion"
  const accordions = document.getElementsByClassName("accordion");

  if (accordions.length === 0) {
    console.log("No se encontraron elementos con la clase 'accordion'");
    return;
  }

  // Itera sobre cada elemento
  Array.from(accordions).forEach((accordion) => {
    // Agrega un evento de click a cada elemento
    accordion.addEventListener("click", () => {
      // Alterna la clase "active" en el elemento
      accordion.classList.toggle("active");

      // Selecciona el panel que se encuentra después del elemento
      const panel = accordion.nextElementSibling;

      // Alterna la visibilidad del panel
      panel.style.display = panel.style.display === "block" ? "none" : "block";
    });
  });
}

// Función que se ejecuta cuando el documento está listo
function onReady() {
  initMenu();
}

// Espera a que el documento esté listo antes de ejecutar la función onReady
document.addEventListener("DOMContentLoaded", onReady);
