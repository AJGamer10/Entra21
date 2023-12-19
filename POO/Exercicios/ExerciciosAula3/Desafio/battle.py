from pokemon import Pokemon
from damage_calculator import DamageCalculator
from random import choice


class Battle:
    """Representa uma batalha pokemon.
    
    Args:
        pokemon1 (Pokemon): Pokemon jogador.
        pokemon2 (Pokemon): Pokemon oponente.
    """
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turno = self.pokemon1.nome
        self.count = 1

    def turno_battle(self):
        """Realiza um turno"""
        while True:
            if self.count == 1:
                input(f"Você encontra um(a) {self.pokemon2} no caminho!")
                input(f"Você lança {self.pokemon1.nome}, e ele se prepara para atacar!")
                self.count += 1

            print(self.pokemon1)
            print(self.pokemon2)

            if self.turno == self.pokemon1.nome:
                while True:
                    print("Moves:")
                    contador = 1
                    for ataque in self.pokemon1.ataques:
                        print(f"""      {contador}) {ataque.nome} - atk: {ataque.dano} - tipo: {ataque.tipo}""")
                        contador += 1
                    opcao = input("Qual ataque deseja realizar: ")
                    if (not opcao.isdigit()) or int(opcao) > 4:
                        input('Por favor digite um numero correspondente para continuar')
                        continue
                    else:
                        opcao = int(opcao)
                        break
                    
                input(f"{self.pokemon1.nome} usou {self.pokemon1.ataques[opcao - 1].nome}")
                self.pokemon1.atacar(self.pokemon1, self.pokemon1.ataques[opcao - 1], self.pokemon2)
                if self.pokemon2.current_hp <= 0:
                    input(f"{self.pokemon2.nome} desmaiou!")
                    input(f"{self.pokemon1.nome} venceu!")
                    break
                else:
                    self.__trocar_turno()
                    continue

            elif self.turno == self.pokemon2.nome:
                input(f"{self.pokemon2.nome} se prepara para atacar!")
                ataque_usado = choice(self.pokemon2.ataques)
                input(f"{self.pokemon2.nome} usou {ataque_usado.nome}")
                self.pokemon2.atacar(self.pokemon2, ataque_usado, self.pokemon1)
                if self.pokemon1.current_hp <= 0:
                    input(f"{self.pokemon1.nome} desmaiou!")
                    input(f"{self.pokemon2.nome} venceu!")
                    input("Você perdeu!")
                    break
                else:
                    self.__trocar_turno()
                    continue
        
    def __trocar_turno(self):
        if self.turno == self.pokemon1.nome:
            self.turno = self.pokemon2.nome
        else:
            self.turno = self.pokemon1.nome
    