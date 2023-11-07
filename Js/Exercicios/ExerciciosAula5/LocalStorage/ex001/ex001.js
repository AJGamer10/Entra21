$(document).ready(() => {
    const $textarea = $('#textarea');
    const $clearButton = $('#clearButton');

    $clearButton.click(() => {
        $textarea.val('');
        localStorage.clear();
    })

    const reloadData = () => {
        text = localStorage.getItem('text');
        $textarea.val(text)
    };

    $textarea.on('input', () => {
        let digitedText = $textarea.val();
        localStorage.setItem('text', digitedText);
    });

    reloadData();
});