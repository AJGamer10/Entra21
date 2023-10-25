// 1)
const sumSalaries = salaries => {
    let sum = 0;
    for (let salary of Object.values(salaries)) {
        sum += salary
    };
    return sum;
}
let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": 250
};

alert(sumSalaries(salaries)); // 650

// 2)
const count = user => Object.keys(user).length;
let user = {
    name: 'John',
    age: 30
};

alert(count(user)); // 2