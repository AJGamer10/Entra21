$(document).ready(() => {
    const $cronometro = $('#cronometro');
    const $toggle = $('#toggle');
    const $reset = $('#reset');

    let running = false;
    let startTime = 0;
    let elapsedTime = 0;
    let timerInterval;

    const formatTime = (milliseconds) => {
        const hours = Math.floor(milliseconds / 3600000);
        const minutes = Math.floor((milliseconds % 3600000) / 60000);
        const seconds = Math.floor((milliseconds % 60000) / 1000);

        return (
            (hours < 10 ? '0' : '') + hours + ':' +
            (minutes < 10 ? '0' : '') + minutes + ':' +
            (seconds < 10 ? '0' : '') + seconds
        );
    };

    const updateCronometro = () => {
        const currentTime = new Date().getTime();
        elapsedTime = currentTime - startTime;
        $cronometro.text(formatTime(elapsedTime));
    };

    const toggleCronometro = () => {
        if (running) {
            running = false;
            clearInterval(timerInterval);
            $toggle.text('Resumir');
        } else {
            running = true;
            startTime = new Date().getTime() - elapsedTime;
            timerInterval = setInterval(updateCronometro, 1000);
            $toggle.text('Pausar');
        }
    };

    $toggle.click(toggleCronometro);

    const resetCronometro = () => {
        running = false;
        startTime = 0;
        elapsedTime = 0;
        clearInterval(timerInterval);
        $toggle.text('Iniciar');
        $cronometro.text('00:00:00');
    };

    $reset.click(resetCronometro);
});