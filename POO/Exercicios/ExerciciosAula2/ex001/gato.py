from animal import Animal

class Gato(Animal):
    """Gato representa um animal da espécie gato
    
    Attributes:
        nome (str): Nome do gato.
    """

    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome

    def emitir_som(self):
        """Realiza a ação de emitir som do gato"""
        print(f"O gato chamado {self.nome} está miando.")

    def mover(self):
        """Realiza a ação de mover do gato"""
        print(f"O gato chamado {self.nome} está andando.")
