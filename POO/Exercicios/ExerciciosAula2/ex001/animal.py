"""
1) Implemente uma superclasse Animal com métodos como emitir_som() e mover(). Crie 
subclasses como Cachorro, Gato, Pássaro. Sobrescreva os métodos para representar o 
nome específico de cada animal.
"""
from abc import ABC

class Animal(ABC):
    """Animal representa um animal."""

    def emitir_som(self):
        """Realiza a ação de emitir som do animal."""
        print("O animal está emitindo um som.")

    def mover(self):
        """Realiza a ação de mover do animal."""
        print("O animal está se movendo")
