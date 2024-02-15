jQuery(function() {
    $("#submitButton").on("click", function() {
        $button = $(this);

        $button.prop("disabled", true);
        
        $buttonText = $("#buttonText");
        loadingText = $buttonText.data("loading-text");

        $("#buttonText").text(loadingText);
        $("#loadingSpinner").show();

        $("#form").submit();
    });
});