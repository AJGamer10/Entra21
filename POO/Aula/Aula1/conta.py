"""Implementação da Conta."""


class Conta:
    """Conta representa uma conta bancária.

    Attributes:
        numero (str): Número identificador da Conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """

    def __init__(self, numero: str, titular: str):
        # Realizando validação do número da conta
        if len(numero) != 9:
            raise AttributeError("número da conta deve possuir 9 digitos")
        
        # Encapsulamento
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir o valor
        self.__limite = 100
        self.__saldo = 0    

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite: str):
        self.__limite = novo_limite
    
    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float) -> None:
        """Depositar um valor no saldo da conta.

        Args:
            valor (float): Valor do deposito.
        """
        self.__saldo += valor


if __name__ == "__main__":
    conta_william = Conta('123456789', "william círico")

    print(f'Nome titular quando foi criado: {conta_william.titular}')

    conta_william.titular = 'william círico'

    print(f'Nome titular após a modificação: {conta_william.titular}')

    print(f'Valor antes do deposito: {conta_william.saldo}')
    conta_william.depositar(100_000_000)
    print(f'Valor antes do deposito: {conta_william.saldo}')
