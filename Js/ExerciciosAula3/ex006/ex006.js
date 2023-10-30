$(document).ready(() => {
    $('.grid-item').click(function() {
        // Remove a classe "selected" de todas as divs
        $('.grid-item').removeClass('selected');
        
        // Adiciona a classe "selected" à div clicada
        $(this).addClass('selected');
        
        // Atualiza o texto do <p> com o número da div selecionada
        $('p').text("Quadrado selecionado: " + $(this).text());
    });
});