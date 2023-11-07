$(document).ready(() => {
    const $clicker = $('#clicker');
    const $secret = $('#secret');

    let isClicked = false;

    const viewSecret = () => {
        isClicked = !isClicked;
        
        $clicker.text(isClicked ? 'Esconder' : 'Mostrar');
        $secret.css('display', isClicked ? 'block' : 'none');
    }

    $clicker.click(viewSecret);
});