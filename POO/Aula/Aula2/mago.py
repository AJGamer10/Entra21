from personagem import Personagem
from habilidade_especial import IHabilidadeEspecial

class Mago(Personagem, IHabilidadeEspecial):
    """Mago representa um personagem da classe Mago no jogo
    
    Attributes:
        nome (str): Nome do mago.
        nivel (int): Nível do mago.
        vida (int): Vida do mago.
        magia (int): Quantidade de magia do mago.
    """

    def __init__(self, nome: str, nivel: int, vida: int, magia: int ) -> None:
        super().__init__(nome, nivel, vida) 
        self.magia = magia  

    def atacar(self):
        """Realiza a ação de ataque do mago."""
        super().atacar()
        print(f'{self.__nome} lança feitiço poderoso com {self.magia} de magia!')

    def equipar_cajado(self):
        """Realiza a ação de equipar o cajado do mago."""
        print(f'{self.__nome} equipe o cajado! O próximo ataque causará dano em área.')

    def usar_super_habilidade(self):
        """Utiliza a super habilidade do mago"""
        print(f"{self.nome} utiliza a habilidade especial")


if __name__ == "__main__":
    mago = Mago("Abner the Mage", 1, 10, 11)

    # print(mago.nome)
    print(mago.magia)

    mago.atacar()
