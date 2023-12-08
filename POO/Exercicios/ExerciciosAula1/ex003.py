"""
3) Crie uma classe agenda que pode armazenar 10 pessoas e que seja capaz de realizar as seguintes operações:
adicionar_pessoa() - Adiciona uma pessoa na agenda.
remover_pessoa() - Remove uma pessoa pelo nome da agenda.
buscar_pessoa() - Busca uma pessoa pelo nome na agenda (Mostra todas as informações da pessoa encontrada).
listar_pessoas() - Mostra as informações de todas as pessoas da agenda.

As pessoas da agenda devem ser objetos da classe Pessoa (ex. 1).
"""
from ex001 import *


class Agenda:
    """Representa uma agenda que pode armazenar 10 pessoas."""

    def __init__(self, nome: str):
        self.nome = nome
        self.pessoas = []

    def adicionar_pessoa(self, nome: str, telefone: str) -> None:
        """Adiciona uma pessoa na agenda.
        
        Args:
            nome (str): Nome da pessoa.
            telefone (str): Número de telefone da pessoa.
        """
        if len(self.pessoas) < 10:
            self.pessoas.append(Pessoa(nome, telefone))
            print(f"{nome} adicionado(a) com sucesso!")
    
    def remover_pessoa(self, nome: str) -> None:
        """Remove uma pessoa pelo nome da agenda.
        
        Args:
            nome (str): Nome da pessoa.
        """
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                self.pessoas.remove(pessoa)
                print(f"{pessoa.nome} removido(a) com sucesso!")

    def buscar_pessoa(self, nome: str):
        """Busca uma pessoa pelo nome na agenda (Mostra todas as informações da pessoa encontrada).
        
        Args:
            nome (str): Nome da pessoa.
        """
        print('=====================')
        print('Esses foram os resultados encontrados: \n')
        for pessoa in self.pessoas:
            if pessoa.nome.lower()[0: len(nome)] == nome.lower():
                print(f'Nome: {pessoa.nome} | Telefone: {pessoa.telefone}')
        print('=====================')
    
    def listar_pessoas(self):
        """Mostra as informações de todas as pessoas da agenda."""
        print('=====================')
        for pessoa in self.pessoas:
            print(f'Nome: {pessoa.nome} | Telefone: {pessoa.telefone}')
        print('=====================')


if __name__ == '__main__':
    agenda1 = Agenda("Agenda Principal")

    agenda1.adicionar_pessoa("Abner Eger", "+55 49 9 9170-0435")
    agenda1.adicionar_pessoa("Rodrigo Silva", "+55 47 9 9124-2445")
    agenda1.adicionar_pessoa("Eduardo Costa", "+55 48 9 9455-2647")

    print()

    agenda1.remover_pessoa("Eduardo Costa")

    print()

    agenda1.buscar_pessoa("Rodri")

    print()

    agenda1.listar_pessoas()
