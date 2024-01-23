jQuery(function () {
    const $form = $("form");
    const $salePriceInput = $("#salePriceInput");

    $salePriceInput.maskMoney({
        thousands: '.',
        decimal: ',',
        allowZero: true,
        prefix: 'R$ ',
        affixesStay: false
    });
    
    // Acrescentando as validações para o formulário: https://jqueryvalidation.org/validate/
    $form.validate({
        errorElement: "div", // Elemento que será criado
        errorClass: "invalid-feedback", // Classe que será aplicada
        // Como os campos com erro irão se comportar
        highlight: (element, _, validClass) => {
            $(element).addClass("is-invalid");
        },
        // Como os campos sem erro irão se comportar
        unhighlight: (element) => {
            $(element).removeClass("is-invalid");
        },
        // Onde a mensagem de erro será adicionada
        errorPlacement: (error, element) => {
            error.addClass("invalid-feedback");
            error.insertAfter(element);
        },
        // Validações que serão aplicadas
        rules: {
            name: {
                required: true,
            },
            sale_price: {
                required: true,
            },
            expiration_date: {
                required: true,
            },
        },
        // Mensagens que serão exibidas de acordo com os erros
        messages: {
            name: "Por favor, informe o nome",
            sale_price: "Por favor, informe o nome do representante",
            expiration_date: "Por favor, informe a data de validade",
        },
    });
});