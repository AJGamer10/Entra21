$(document).ready(() => {
    const people = [
        { id: 1, name: "Ana", age: 23, sex: "F" },
        { id: 2, name: "Maria", age: 42, sex: "F" },
        { id: 3, name: "João", age: 15, sex: "M" },
        { id: 4, name: "Matheus", age: 19, sex: "M" },
        { id: 5, name: "Antônio", age: 40, sex: "M" },
    ];

    const $tableBody = $("#peopleTable tbody");

    people.forEach(person => {
        $tableBody.append(
            '<tr>' +
            '<td>' + person.id + '</td>' +
            '<td>' + person.name + '</td>' +
            '<td>' + person.age + '</td>' +
            '<td>' + (person.sex === "F" ? "Feminino" : "Masculino") + '</td>' +
            '</tr>'
        )
    })
});