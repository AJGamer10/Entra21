// 1)
let i1 = 3;

while (i1) {
    alert(i1--);
} // O ultimo valor será 1, pois quando chega a 0 o condicional é falso

// 2)

    // a)
    let i2 = 0;
    while (++i2 < 5) alert(i2); // 1, 2, 3, 4
    // ++ antes faz com que o valor incrementedo seja o resultado,
    // ou seja, a comparação do while começa com 1 pois ele incrementa
    // primeiro, depois faz a comparação.

    // b)
    let i3 = 0;
    while (i3++ < 5) alert(i3); // 1, 2, 3, 4, 5
    // Já neste caso, como o ++ está depois ele vai retornar seu valor
    // e apenas depois faz a incrementação, ou seja, ele faz a comparação
    // primeiro (sendo que o valor neste momento é 0), e apenas depois
    // faz a incrementação.

// 3)

    // a)
    for (let i = 0; i < 5; i++) alert( i ); // 0, 1, 2, 3, 4

    // b)
    for (let i = 0; i < 5; ++i) alert( i ); // 0, 1, 2, 3, 4

    // Os dois terão os mesmos resultados, quando é um loop for o incremento é separado da
    // comparação for (começo; comparação; fim) ou seja, importa se está em prefixo ou
    // posfixo o ++, pois o valor retornado do incremento não é usado.

// 4)
for (let i = 2; i <= 10; i++) {

    if (i % 2 == 0) {

        alert( i );
    };
};

// 5)
let i = 0;

while (i < 3) {
    alert( `number ${i++}!` );
}

// 6)
let answer;
do {
    answer = prompt("Enter a number greater than 100?");
} while (answer <= 100 && answer);

// 7)
const number = +prompt("Digite um número");
let answers = [];

for (let i = 2; i <= number; i++) {
    let isPrime = true;
    for (let j = 2; j < i; j++) {
        if (i % j === 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        answers.push(i);
    }
}

alert(answers)