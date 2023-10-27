// 1)
let fruits = ["Apples", "Pear", "Orange"];

// push a new value into the "copy"
let shoppingCart = fruits;
shoppingCart.push("Banana");

// what's in fruits?
alert(fruits.length); // 4

// 2)
const styles = ["Jazz", "Blues"]
styles.push("Rock-n-Roll")
styles[Math.floor(styles.length - 1) / 2] = "Classics"
alert(styles.shift())
styles.unshift("Rap", "Reggae")

// 3)
let arr = ["a", "b"];

arr.push(function () {
    alert(this);
});

arr[2](); // a,b,function() { alert( this ); }

// 4)
const sumInput = () => {
    let numbers = []
    while (true) {
        let value = prompt('Digite um valor', 0);

        if (value === "" || value === null || !isFinite(value)) break;

        numbers.push(+value);
    }
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
}

alert(sumInput())

// 5)
arr = [1, -2, 3, 4, -9, 6]
const getMaxSubSum = (array) => {
    let sum = 0
    for (let number of array) {
        sum += number < 0 ? 0 : number
    }
    return sum
}

alert(getMaxSubSum(arr))