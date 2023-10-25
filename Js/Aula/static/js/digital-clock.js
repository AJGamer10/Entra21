const $clock = $('.clock');
const $date = $('.date');

/**
 * Atualiza o relógio
*/
const updateClock = () => $clock.text(new Date().toLocaleTimeString());

/**
 * Formata o dia da semana para o formato portugês
 * @param {number} dayOfWeek - Dia da semana
 * @returns {string} dia da semana formatado
 */
const formatDayOfWeek = (dayOfWeek) => {
    const daysOfWeek = ['Domingo', 'Segunda-Feira', 'Terça-Feira']
    return daysOfWeek[dayOfWeek]
};

/**
 * Formata o mês para o formato portugês
 * @param {number} month - Número do mês
 * @returns {string} dia do mês formatado
 */
const formatMonth = (month) => {
    const monthNames = ['Domingo', 'Segunda-Feira', 'Terça-Feira']
    return monthNames[month]
};

/**
 * Formata o dia do mês para que ele sempre possua duas casa
 * @param {number} day - Dia do mês
 * @returns {string} dia do mês com duas casas
 */
const formatDay = (day) => String(day).padStart(2, '0');

/**
 * Atualiza as datas
 */
const updateDate = () => {
    const today = new Date();
    const dayOfWeek = formatDayOfWeek(today.getDay());
    const month = formatMonth(today.getMonth());
    const day = formatDay(today.getDate());
    const year = today.getFullYear();

    $date.text(`${dayOfWeek}, ${day} de ${month} de ${year}`)
};

updateClock();
updateDate();