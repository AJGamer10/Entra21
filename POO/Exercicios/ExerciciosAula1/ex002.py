"""
2) Implemente a classe Aluno que possua os atributos: número de matrícula, nome, 
notas. Essa classe deve conter os seguintes métodos: 
    get_media() - Calcula a média do aluno com base nas notas.
    get_situacao() - Informa a situação do aluno com base no critérios:
        0 à 4 - Reprovado
        5 à 6 - Recuperação
        7 à 10 - Aprovado
"""


class Aluno:
    """Aluno representa um aluno de uma escola.

    Attributes:
        numero_matricula (str): Número de matrícula do aluno
        nome (str): Nome do aluno
        notas (list): Notas do aluno
    """

    def __init__(self, nome: str, numero_matricula: str, notas: list) -> None:
        self.__numero_matricula = numero_matricula
        self.nome = nome
        self.notas = notas

    def __str__(self):
        return f"Nome: {self.nome} | Número de matrícula: {self.numero_matricula} | Notas: {self.notas}"

    @property
    def numero_matricula(self):
        """(int): Número da matricula do aluno"""
        return self.__numero_matricula

    def get_media(self) -> float:
        """Calcula a média do aluno com base nas notas.

        Returns:
            Media do aluno com base nas notas
        """
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def get_situacao(self) -> str:
        """Informa a situação do aluno com base no critérios:
        0 à 4 - Reprovado
        5 à 6 - Recuperação
        7 à 10 - Aprovado

        Returns:
            Reprovado se a média for menor ou igual 4
            Recuperação se a média estiver entre 5 á 6
            Aprovado se a média for maior ou igual 7
        """
        media = self.get_media()

        if 0 <= media <= 4:
            return 'Reprovado'

        if 5 <= media <= 6:
            return 'Recuperação'

        return 'Aprovado'


if __name__ == '__main__':
    abner = Aluno("4547084881", "Abner Eger", [10, 9, 9.5])
    print(abner)
    print(f'Média do aluno: {abner.get_media(abner.notas)}')
    print(f'Situação do aluno: {abner.get_situacao(
        abner.nome, abner.numero_matricula, abner.notas)}')

    ricardo = Aluno("4547083881", "Ricardo Araujo", [5, 7, 6])
    print(ricardo)
    print(f'Média do aluno: {ricardo.get_media(ricardo.notas)}')
    print(f'Situação do aluno: {ricardo.get_situacao(
        ricardo.nome, ricardo.numero_matricula, ricardo.notas)}')

    eduardo = Aluno("4547083861", "Eduardo Silva", [2, 3, 1])
    print(eduardo)
    print(f'Média do aluno: {eduardo.get_media(eduardo.notas)}')
    print(f'Situação do aluno: {eduardo.get_situacao(
        eduardo.nome, eduardo.numero_matricula, eduardo.notas)}')
