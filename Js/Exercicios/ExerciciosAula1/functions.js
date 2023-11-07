// 1)
function checkAge(age) {
    if (age > 18) {
        return true;
    } else {
        // ...
        return confirm('Did parents allow you?');
    }
}

function checkAge(age) {
    if (age > 18) {
        return true;
    }
    // ...
    return confirm('Did parents allow you?');
}
// Os dois não tem nenhuma diferença

// 2)
function checkAge(age) {
    if (age > 18) {
        return true;
    } else {
        return confirm('Did parents allow you?');
    }
}

    // a)
    function checkAge(age) {
        return age > 18 ? true : confirm('Did parents allow you?');
    }

    // b)
    function checkAge(age) {
        return (age > 18) || confirm('Did parents allow you?');
    }

// 3)
/**
 * Função que retorna o menor valor de 2 números
 * @param {Number} a Primeiro número
 * @param {Number} b Segundo número
 * @return {Number} Menor número
 */
function min(a, b) {
    return (a < b) ? a : b;
}

// 4)
/**
 * Função que retorna a potencia de 2 números
 * @param {Number} x Primeiro número
 * @param {Number} n Segundo número
 * @returns {Number} potencia
 */
function pow(x, n) {
    return x ** n;
}

x = +prompt('Base da potência');
n = +prompt('Espoênte da potência');

if (n < 1) {
    alert(`Power ${n} is not supported, use a positive integer`);
} else {
    alert( pow(x, n) );
}