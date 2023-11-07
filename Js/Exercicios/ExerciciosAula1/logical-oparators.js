// 1)
alert( null || 2 || undefined ); // 2

// 2)
alert( alert(1) || 2 || alert(3) ); // primeiro 1, então 2

// 3)
alert( 1 && null && 2 ); // null

// 4)
alert( alert(1) && alert(2) ); // primeiro 1, então undefined

// 5)
alert( null || 2 && 3 || 4 ); // 3

// 6)
const age6 = +prompt('Diga sua idade');

if (age6 >= 14 && age6 <= 90) {
    alert('incluso');
};

// 7)
const age7 = +prompt('Diga sua idade');

    // a)
    if (!(age7 >= 14 && age7 <= 90)) {
        alert('Não incluso');
    };

    // b)
    if (age7 < 14 || age7 > 90) {
        alert('Não incluso');
    };

// 8)
if (-1 || 0) alert( 'first' ); // true
if (-1 && 0) alert( 'second' ); // false
if (null || -1 && 1) alert( 'third' ); // true

// 9)
const login = prompt('Digite seu login')

if (login === "Admin") {

    const senha = prompt('Digite sua Senha')

    if (senha === "TheMaster") {
        alert('Bem vindo!')
    } else if (senha === '' || senha === null) {
        alert('Cancelado')
    } else {
        alert('Senha incorreta')
    }

} else if (login === '' || login === null) {
    alert('Cancelado')
} else {
    alert("Eu não te conheço")
}