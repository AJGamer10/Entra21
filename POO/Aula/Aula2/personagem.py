from abc import ABC

class Personagem(ABC):
    """Personagem representa um personagem em um jogo.
    
    Attributes:
        nome (str): Nome do personagem.
        nivel (int): Nivel do personagem.
        vida (int): Vida do personagem.
    """

    def __init__(self, nome: str, nivel: int, vida: int) -> None:
        self.nome = nome
        self.nivel = nivel
        self.vida = vida

    def atacar(self):
        """Realiza a ação de ataque do personagem."""
        print(f'{self.nome} está atacando!')
    
    def defender(self):
        """Realiza a ação de defesa do personagem."""
        print(f'{self.nome} está defendendo!')

    def morrer(self):
        """Realiza a ação de morte do personagem."""
        print(f'{self.nome} foi derrotado!')


if __name__ == "__main__":
    personagem = Personagem("Abner", 1, 10)

    personagem.atacar()
    personagem.defender()
    personagem.morrer()