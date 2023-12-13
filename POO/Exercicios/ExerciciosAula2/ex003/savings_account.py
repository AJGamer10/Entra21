from conta import Conta

class SavingsAccount(Conta):
    """SavingsAccount representa uma conta poupança."""
    interest_percentage = 0.58

    def __init__(self, holder: str, initial_balance: float) -> None:
        super().__init__(holder)
        self.initial_balance = initial_balance
        self.deposit(initial_balance)

    def generate_interest(self):
        """Gera o juros mensal da conta."""
        self.balance += self.balance * (SavingsAccount.interest_percentage / 100)

    def get_deposit_tax(self) -> float:
        return 0.005
