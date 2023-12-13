"""
3) Crie uma superclasse Conta com os seguintes atributos: número da conta, titular e saldo. 
Essa superclasse deve implementar os seguintes métodos: depositar(), sacar(), transferir(). 
Implemente as subclasses: ContaCorrente (Possui um limite adicional para saque e transferências), 
ContaPoupança (Gera juros mensalmente), ContaInvestimento (Permite investir em ações). 
Cada conta possui uma taxa diferente para depósito conforme abaixo:
Conta corrente: 0.2%
Conta poupança: 0.5%
Conta investimento: 0.8%
"""
from __future__ import annotations
from abc import ABC
from random import randint


class Conta(ABC):
    """Conta representa uma conta bancária.
    
    Atributes:
        holder (str): Nome do titular da conta.
    """

    def __init__(self, holder: str) -> None:
        self.__registration = randint(0, 100_000)
        self.__balance = 0
        self.holder = holder

    @property
    def registration(self):
        """(int): Número da conta."""
        return self.__registration
    
    @property
    def balance(self):
        """(float): Número da conta."""
        return self.__balance
    
    @balance.setter
    def balance(self,value: float):
        if value < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self.__balance = value

    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.
        
        Args:
            amount (float): Valor que será sacado.

        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        
        return False

    def deposit(self, amount: float):
        """Deposita um valor na conta.
        
        Args:
            amount (float): Valor que será depositado na conta.
        """
        tax = self.get_deposit_tax()
        
        self.__balance += amount * (1 - tax)
    
    def transfer(self, amount: float, target_account: Conta):
        """Transfere um valor para outra conta.
        
        Args:
            amount (float): Valor que será transferido.
            target_account (Conta): Conta de destino da transferencia.
        """
        if (self.withdraw(amount)):
            target_account.deposit(amount)
        else:
            print("Não foi possivel realizar a transferencia: Saldo indisponivel")

    def __get_deposit_tax(self) -> float:
        """Pega a taxa do depósito"""
