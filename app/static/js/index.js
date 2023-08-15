const alerta = () => {
    alert("Hola Mundo!");
};

const showDatosBrecha = () => {
  
  // encuentro el elemento div con id de brecha
  const brechaContainer = document.getElementById("brecha");
  // si ya se está mostrando el elemento, se oculta, sino se muestra
    if (brechaContainer.style.display === "none") {
        brechaContainer.style.display = "block";
        }
    else {
        brechaContainer.style.display = "none";
        }
};
