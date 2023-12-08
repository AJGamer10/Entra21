"""
6) Crie uma classe chamada Carro que represente um carro com os seguintes atributos:
Marca (String)
Modelo (String)
Ano (int)
Velocidade (int)

A classe deve ter os seguintes métodos:
Um método construtor que recebe os valores iniciais para marca, modelo e ano, e inicializa a velocidade com 0.
Um método "acelerar" que aumenta a velocidade do carro em 10 unidades.
Um método "frear" que diminui a velocidade do carro em 5 unidades.
"""


class Carro:
    """Representa um carro.
    
    Attributes:
        marca (str): Marca do carro.
        modelo (str): Modelo do carro.
        ano (int): Ano de fabricação do carro.
        velocidade (int): Velocidade atual do carro.
    """
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self) -> None:
        """Aumenta a velocidade do carro em 10 unidades."""
        self.velocidade += 10
    
    def frear(self) -> None:
        """Diminui a velocidade do carro em 5 unidades."""
        if not(self.velocidade == 0 or self.velocidade - 5 < 0):
            self.velocidade -= 5
    

if __name__ == '__main__':
    carro1 = Carro("Chevrolet", "Equinox", "2023")

    carro1.acelerar()
    print(f"Velocidade: {carro1.velocidade}")
    carro1.acelerar()
    print(f"Velocidade: {carro1.velocidade}")
    carro1.frear()
    print(f"Velocidade: {carro1.velocidade}")
