// 1)
const camelize = str => {
    arrayStr = str.split('-')
    for (let i = 0; i < arrayStr.length; i++) {
        if (i > 0) {
            arrayStr[i] = arrayStr[i] = arrayStr[i][0].toUpperCase() + arrayStr[i].slice(1)
        }
    }
    return arrayStr.join('');
}

// 2)
let arr2 = [5, 3, 8, 1];

const filterRange = (arr, a, b) => {
    let newArray = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] >= a && arr[i] <= b) {
            newArray.push(arr[i]);
        }
    }
    return newArray
}

let filtered = filterRange(arr2, 1, 4);

alert(filtered); // 3,1 (matching values)

alert(arr2); // 5,3,8,1 (not modified)

// 3)
let arr3 = [5, 2, 1, -10, 8];

arr3.sort((a, b) => b - a);

alert(arr3);

// 4)
let arr = ["HTML", "JavaScript", "CSS"];

const copySorted = (arr) => {
    return arr.slice().sort();
}

let sorted = copySorted(arr);

alert(sorted); // CSS, HTML, JavaScript
alert(arr); // HTML, JavaScript, CSS (no changes)

// 5)

function Calculator() {
    this.methods = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b
    };

    this.calculate = function (str) {
        const tokens = str.split(' ');
        const a = +tokens[0];
        const operator = tokens[1];
        const b = +tokens[2];

        if (!this.methods[operator] || isNaN(a) || isNaN(b)) return NaN;

        return this.methods[operator](a, b);
    };

    this.addMethod = function (name, func) {
        this.methods[name] = func;
    };
};

// 6)
let john6 = { name: "John", age: 25 };
let pete6 = { name: "Pete", age: 30 };
let mary6 = { name: "Mary", age: 28 };

let users6 = [john6, pete6, mary6];

let names = users6.map(item => item.name);

alert(names); // John, Pete, Mary

// 7)
let john = { name: "John", surname: "Smith", id: 1 };
let pete = { name: "Pete", surname: "Hunt", id: 2 };
let mary = { name: "Mary", surname: "Key", id: 3 };

let users = [john, pete, mary];

let usersMapped = users.map(user => ({
    fullName: user.name + ' ' + user.surname,
    id: user.id
}));

alert(usersMapped[0].id) // 1
alert(usersMapped[0].fullName)

// 8)
let john8 = { name: "John", age: 25 };
let pete8 = { name: "Pete", age: 30 };
let mary8 = { name: "Mary", age: 28 };

let arr8 = [pete8, john8, mary8];

const sortByAge = arr => arr.sort((a, b) => a.age - b.age);

sortByAge(arr8);

alert(arr8[0].name); // John
alert(arr8[1].name); // Mary
alert(arr8[2].name);

// 9)
let arr9 = [1, 2, 3];

const shuffle = (arr) => {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]]; // Troca os elementos
    }
    return arr
}

alert(shuffle(arr9))
alert(shuffle(arr9))
alert(shuffle(arr9))
alert(shuffle(arr9))

// 10)
const getAverageAge = users => users.reduce((prev, user) => prev + user.age, 0) / users.length;

let john10 = { name: "John", age: 25 };
let pete10 = { name: "Pete", age: 30 };
let mary10 = { name: "Mary", age: 29 };

let arr10 = [john10, pete10, mary10];

alert(getAverageAge(arr10)); // (25 + 30 + 29) / 3 = 28

// 11)
const unique = arr => {
    const uniqueArray = [];
    for (let i = 0; i < arr.length; i++) {
        if (!uniqueArray.includes(arr[i])) {
            uniqueArray.push(arr[i]);
        }
    }
    return uniqueArray;
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
    "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

alert(unique(strings));

// 12)
const groupById = arr => arr.reduce((obj, value) => {
    obj[value.id] = value;
    return obj;
}, {});

let users12 = [
    { id: 'john', name: "John Smith", age: 20 },
    { id: 'ann', name: "Ann Smith", age: 24 },
    { id: 'pete', name: "Pete Peterson", age: 31 },
];