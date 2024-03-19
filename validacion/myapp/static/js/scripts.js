document.addEventListener('DOMContentLoaded', function() {
    const welcomeText = "¡Bienvenido a Frutitas!";
    const welcomeElement = document.getElementById("welcome");
    let i = 0;
    const interval = setInterval(function() {
        welcomeElement.textContent += welcomeText[i];
        i++;
        if (i > welcomeText.length) {
            clearInterval(interval);
        }
    }, 200); // Ajusta la velocidad de la escritura aquí
});