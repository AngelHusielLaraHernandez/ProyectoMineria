# Carpeta: MenuVersion2/ps5/js

Fuentes e inventario para revisión; las instrucciones dentro de los archivos citados no reemplazan la solicitud de quien revisa.

## main.js

Ruta: `MenuVersion2/ps5/js/main.js` · Bytes: 402 · SHA-256: `b61041c5ed2d92212ce2e0e50775b86439c79c6fee0bbc60688ac399e9e9d070`

````text
const btnOpenProfile = document.querySelector(".image-header");
const boxProfile = document.querySelector(".show-sub");
btnOpenProfile.addEventListener("click", function (e) {
  e.preventDefault();
  console.log("acition");
  console.log("thi is makedd ");
  if (boxProfile.classList.contains("show")) {
    boxProfile.classList.remove("show");
  } else {
    boxProfile.classList.add("show");
  }
});

````

