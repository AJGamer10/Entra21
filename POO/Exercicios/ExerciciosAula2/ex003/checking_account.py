from conta import Conta

class CheckingAccount(Conta):
    """CheckingAccount representa uma conta corrente."""

    def __init__(self, holder: str, limit: float) -> None:
        super().__init__(holder)
        self.__limit = limit

    @property
    def limit(self):
        return self.__limit
    
    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.
        
        Args:
            amount (float): Valor que será sacado.

        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if (self.__balance + self.__limit) < amount:
            print("Saldo indisponivel para realizar a operação.")
            return False
        
        if self.balance < amount:
            self.__limit -= amount - self.balance
            self.balance = 0
        else:
            self.balance -= amount
        
        return True
    
    def __get_deposit_tax(self) -> float:
        return 0.002
