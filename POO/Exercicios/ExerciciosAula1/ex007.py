"""
7) Crie uma classe chamada Universidade que representa uma universidade com os seguintes atributos estáticos:
Total de estudantes (int)
Total de professores (int)

A classe deve ter os seguintes métodos estáticos:
Um método matricular_estudante que incrementa o total de estudantes.
Um método contratar_professor que incrementa o total de professores.
Um método obter_total_pessoas que retorna o total de estudantes e professores juntos.

Além disso, a classe deve ter um atributo nome(str) para representar o nome da universidade.

"""


class Universidade:
    """Representa uma universidade
    
    Attributes:
        nome (str): Nome da universidade
    """

    total_estudantes = 0
    total_professores = 0

    def __init__(self, nome: str) -> None:
        self.nome = nome

    @classmethod
    def matricular_estudante(cls):
        """Matricula um estudante"""
        cls.total_estudantes += 1
    
    @classmethod
    def contratar_professor(cls):
        """Contrata um professor"""
        cls.total_professores += 1
    
    @classmethod
    def obter_total_pessoas(cls):
        """Obtem o valor total de pessoas na universidade
        
        Returns:
            Total de estudantes e professores juntos
        """
        return cls.total_estudantes + cls.total_professores
    

if __name__ == "__main__":
    Universidade.matricular_estudante()
    Universidade.contratar_professor()
    print(Universidade.obter_total_pessoas())
