from animal import Animal

class Cachorro(Animal):
    """Cachorro representa um animal da espécie cachorro
    
    Attributes:
        nome (str): Nome do cachorro.
    """

    def __init__(self, nome: str) -> None:
        super().__init__()
        self.nome = nome

    def emitir_som(self):
        """Realiza ação de emitir som do cachorro"""
        print(f"O cachorro chamado {self.name} está latindo.")

    def mover(self):
        """Realiza ação de mover do cachorro"""
        print(f"O cachorro chamado {self.name} está andando.")
