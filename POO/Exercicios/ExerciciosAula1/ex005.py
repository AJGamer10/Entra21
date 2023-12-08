"""
5) Crie uma classe Calculadora que implemente os métodos estáticos: soma, subtracacao, multiplicacao e divisao.
"""


class Calculadora:
    """Representa uma calculadora"""

    @staticmethod
    def soma(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def subtracao(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiplicacao(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def divisao(a: float, b: float) -> float:
        return a / b
    
    @staticmethod
    def potencia(a: float, b: float) -> float:
        return a ** b
    
    @staticmethod
    def raiz(num: float) -> float:
        return num ** 0.5
    

if __name__ == "__main__":
    print(f"""
    Soma: {Calculadora.soma(10, 15)}
    Subtração: {Calculadora.subtracao(10, 4)}
    Multiplicação: {Calculadora.multiplicacao(6, 3)}
    Divisão: {Calculadora.divisao(24, 4)}
    Potência: {Calculadora.potencia(4, 2)}
    Raíz quadrada: {Calculadora.raiz(16)}
""")
