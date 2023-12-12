from personagem import Personagem

class Guerreiro(Personagem):
    """Guerreiro representa um personagem da classe Guerreiro no jogo
    
    Attributes:
        nome (str): Nome do mago.
        nivel (int): Nível do mago.
        vida (int): Vida do mago.
        forca (int): Quantidade de força do guerreiro.
    """

    def __init__(self, nome: str, nivel: int, vida: int, forca: int ) -> None:
        super().__init__(nome, nivel, vida) 
        self.forca = forca  

    def atacar(self):
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f'{self.nome} desfere um golpe poderoso com {self.forca} de forca!')

    def equipar_escudo(self):
        """Realiza a ação de equipar o escudo dos guerreiros."""
        print(f'{self.nome} equipa o escudo! A vida de {self.nome} aumentou.')


if __name__ == "__main__":
    guerreiro = Guerreiro("Abner the Worrior", 1, 50, 10)

    