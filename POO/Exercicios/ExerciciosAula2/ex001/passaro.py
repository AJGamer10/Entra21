from animal import Animal

class Passaro(Animal):
    """Passaro representa um animal da espécie pássaro
    
    Attributes:
        nome (str): Nome do pássaro.
    """

    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome

    def emitir_som(self):
        """Realiza a ação de emitir som do pássaro"""
        print(f"O Pássaro chamado {self.nome} está assobiando.")

    def mover(self):
        """Realiza a ação de mover do pássaro"""
        print(f"O Pássaro chamado {self.nome} está voando.")
