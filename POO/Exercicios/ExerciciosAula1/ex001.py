"""
1) Crie uma classe chamada Pessoa com os atributos privados nome e telefone. Implemente métodos públicos para
obter e definir esses atributos. Em seguida, crie um objeto dessa classe e utilize os métodos para definir um nome
e telefone, logo após, exiba-os na tela.
"""
import re


class InvalidNameError(Exception):
    pass


class InvalidPhoneError(Exception):
    pass


class Pessoa:
    """Pessoa representa uma pessoa.

    Attributes:
        nome (str): Nome da pessoa
        telefone (str): Telefone de contato da pessoa
    """

    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def __str__(self) -> str:
        return f"{self.nome}, {self.telefone}"

    @property
    def nome(self):
        """str: Nome da pessoa."""
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not self.__is_name_valid(nome):
            raise InvalidNameError()
        self.__nome = nome

    @property
    def telefone(self):
        """str: Número de telefone."""
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if not self.__is_phone_valid(telefone):
            raise InvalidPhoneError()
        self.__telefone = telefone

    def __is_phone_valid(self, telefone: str) -> bool:
        """Verifica se um número de telefone é válido (+55 49 9 9999-9999).
        
        Args:
            telefone (str): Telefone que será verificado.

        Returns:
            bool: True caso o número de telefone seja válido, False caso não seja.
        """
        telefone_regex = r"\+55\s?(?:\([1-9]{2}\)|[1-9]{2})\s?(?:9\s?\d{4}[-.\s]?\d{4}|\d{4}[-.\s]?\d{4})"
        return re.match(telefone_regex, telefone)

    def __is_name_valid(self, nome: str) -> bool:
        """Verifica se um nome é válido (Nome completo).
        
        Args:
            name (str): Nome que será verificado.

        Returns:
            bool: True caso o nome seja composto, False caso não seja.
        """
        return len(nome.strip().split()) > 1


if __name__ == '__main__':
    pessoa1 = Pessoa('Abner Eger', '+55 49 9 9170-0435')
    print(pessoa1)
    print(pessoa1.nome)
    print(pessoa1.telefone)
