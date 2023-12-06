"""
Classe - É um modelo para o objeto.
* Atributos - Características do objeto.
* Métodos - Ações do objeto.
"""

class NomeClasse:
    """Docstring da classe."""

    # Metodo construtor: método utilizado para inicialzar um objeto da classe.
    def __init__(self, parametro1: int = 10):
        # self --> Referência ao próprio objeto.
        self.atributo1 = parametro1

        # Declarar um atributo privado.
        self.__atributo_privado = 0

    # Getters
    @property
    def atributo_privado(self):
        return self.__atributo_privado

    # Setters
    @atributo_privado.setter
    def atributo_privado(self, novo_valor: int):
        self.__atributo_privado = novo_valor

    # Metodos do objeto
    def metodo1(self):
        """Docstring do metodo."""
        print("Chamando o metodo do objeto.")


if __name__ == '__main__':
    objeto_teste = NomeClasse(20)
    print(objeto_teste.atributo1)
    objeto_teste.metodo1()
