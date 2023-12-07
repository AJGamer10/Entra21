"""
1) Crie uma classe chamada Pessoa com os atributos privados nome e telefone. Implemente métodos públicos para
obter e definir esses atributos. Em seguida, crie um objeto dessa classe e utilize os métodos para definir um nome
e telefone, logo após, exiba-os na tela.
"""

class Pessoa:
    """Pessoa representa uma pessoa física.

    Attributes:
        nome (str): Nome da pessoa
        telefone (str): Telefone de contato da pessoa
    """

    def __init__(self, nome: str, telefone: str) -> None:
        self.__nome = nome
        self.__telefone = telefone

    def __str__(self) -> str:
        return f"Nome: {self.__nome} | Telefone: {self.__telefone}"
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone


if __name__ == '__main__':
    abner = Pessoa("Abner Eguer", "(49)99170-0437")
    print(abner)
    abner.nome = "Abner Eger"
    print(abner)
    abner.telefone = "(49)99170-0435"
    print(abner)
