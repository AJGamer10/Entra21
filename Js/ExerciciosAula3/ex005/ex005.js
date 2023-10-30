$(document).ready(() => {
    const people = [
        { id: 1, name: "Ana", age: 23, sex: "F" },
        { id: 2, name: "Maria", age: 42, sex: "F" },
        { id: 3, name: "João", age: 15, sex: "M" },
        { id: 4, name: "Matheus", age: 19, sex: "M" },
        { id: 5, name: "Antônio", age: 40, sex: "M" },
    ];

    const $tableBody = $("#peopleTable tbody");

    /**
     * Formatação do sexo da pessoa
     * @param {string} sex - Sexo da pessoa
     * @returns Sexo formatado
     */
    const formatSex = sex => sex === "F" ? "Feminino" : "Masculino"

    // Criando linhas com os dados
    $.each(people, (_, person) => {
        // Criando a linha com dados da pessoa
        const $row = $(
            `<tr>
            <td>${person.id}</td>
            <td>${person.name}</td>
            <td>${person.age}</td>
            <td>${formatSex(person.sex)}</td>
            </tr>`
        )

        // Inserir a linha na tabela
        $tableBody.append($row)
    })
});