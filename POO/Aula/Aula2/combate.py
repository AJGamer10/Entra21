from personagem import Personagem
from mago import Mago
from guerreiro import Guerreiro

class Combate:
    """Combate representa uma partida no jogo.
    
    Attributes:
        personagem1 (Personagem): Personagem 1.
        personagem2 (Personagem): Personagem 2.
    """

    def __init__(self, personagem1: Personagem, personagem2: Personagem) -> None:
        if not isinstance(personagem1, Personagem):
            raise TypeError("personagem1 precisa ser do tipo Personagem")

        if not isinstance(personagem2, Personagem):
            raise TypeError("personagem2 precisa ser do tipo Personagem")

        self.personagem1 = personagem1
        self.personagem2 = personagem2

    def iniciar_combate(self):
        """Inicia um combate entre dois personagens"""
        print(f'Inicio do combate entre {self.personagem1} e {self.personagem2}')

        self.personagem1.atacar()
        self.personagem2.defender()

        self.personagem2.atacar()
        self.personagem1.defender()

        self.personagem1.atacar()
        self.personagem2.morrer()

        print("Fim do combate")


if __name__ == "__main__":
    will_mage = Mago("William the mage", 1, 10, 10)
    abner_warrior = Guerreiro("Abner the warrior", 1, 50, 10)

    combate = Combate(will_mage, abner_warrior)
    combate.iniciar_combate()
