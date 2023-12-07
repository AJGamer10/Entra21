"""Implementação da Conta."""
from __future__ import annotations


class Conta:
    """Conta representa uma conta bancária.

    Attributes:
        numero (str): Número identificador da Conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo da conta.
        limite (float): Limite da conta.
    """
    quantidade_contas = 0 # Atributo estático -> pertence a classe e não ao objeto

    def __init__(self, numero: str, titular: str):
        # Realizando validação do número da conta
        if len(numero) != 9:
            raise AttributeError("número da conta deve possuir 9 digitos")
        
        # Encapsulamento
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir o valor
        self.__limite = 100
        self.__saldo = 0

        Conta.quantidade_contas += 1

    # Formata a visualização (print) do objeto
    def __str__(self):
        return f"Titular: {self.__titular} | Saldo: {self.__saldo} | Limite: {self.__limite}"

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
    
    def sacar(self, valor: float) -> bool:
        """Saca valor da conta se o saldo + limite for maior ou igual ao valor do saque.
        
        Args:
            valor (float): Valor saque.
        
        Returns:
            True se for bem-sucedido, False caso contrário.
        """
        if (self.__saldo + self.__limite) < valor:
            print("Saldo indisponivel para realizar a operação.")
            return False
        
        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor
        
        return True
    
    def tranferir(self, valor: float, conta_destino: Conta) -> None:
        """Tranfere o valor de uma conta para outra se o (saldo + limite)
        for maior ou igual ao valor do saque.

        Args:
            valor (float): Valor da tranferência.
            conta_destino (Conta): Conta de destino da transferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")

    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        """Verifica se o número da conta é válido.

        Args:
            numero (str): Número da conta.

        Returns:
            True caso o número da conta seja válido, False caso contrário
        """
        return len(numero) == 9


if __name__ == "__main__":
    conta_william = Conta('123456789', "william círico")

    print(f'Nome titular quando foi criado: {conta_william.titular}')

    conta_william.titular = 'william círico'

    print(f'Nome titular após a modificação: {conta_william.titular}')

    print(f'Valor antes do deposito: {conta_william.saldo}')
    conta_william.depositar(100_000_000)
    print(f'Valor antes do deposito: {conta_william.saldo}')
    conta_william.sacar(100_000_101)
    conta_william.sacar(1000)
    print(conta_william)
    conta_william.sacar(99999050)
    print(conta_william)

    conta_marcos = Conta('123467282', "marcos")
    print(conta_marcos)

    conta_william.tranferir(20, conta_marcos)
    print(conta_william)
    print(conta_marcos)

    print(Conta.quantidade_contas)

    if Conta.verifica_numero_conta('256173852'):
        print('Número da conta é válido!')
    else:
        print('Número da conta é inválido!')
