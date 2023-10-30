$(document).ready(() => {
    const $incrementer = $('#incrementer');
    const $decrementer = $('#decrementer');
    const $counter = $('#counter');

    let valor = 0;

    const increment = () => {
        valor++;
        $counter.text(valor);
    }
    const decrement = () => {
        valor--;
        $counter.text(valor);
    }

    $incrementer.click(increment);
    $decrementer.click(decrement);
});