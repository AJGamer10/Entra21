"""
8) Crie uma classe abstrata chamada Veiculo com os seguintes atributos:
Marca (str)
Ano (int)
A classe deve ter um método abstrato chamado calcular_imposto() que calcula e 
retorna o valor do imposto a ser pago pelo veículo.
"""


class Veiculo:
    """Representa um veículo.
    
    Attributes:
        tipo (str): Tipo de veículo (moto(m) ou outro(o))
        marca (str): Marca do veículo
        ano (int): Ano de fabricação do veículo
        valor (float): Valor de médio do veículo no mercado
    """
    def __init__(self, tipo: str, marca: str, ano: int, valor: float) -> None:
        self.tipo = tipo.lower()
        self.marca = marca
        self.ano = ano
        self.valor = valor
    
    def calcular_imposto(self):
        """Calcula o imposto a ser pago pelo produto em Santa Catarina"""
        if self.tipo == "m":
            aliquota = 0.01
        else:
            aliquota = 0.02
        
        if 2023 - self.ano > 30:
            return 0
        else:
            imposto = self.valor * aliquota
            return imposto


if __name__ == "__main__":
    # Exemplo 1: Moto
    moto = Veiculo(tipo="m", marca="Honda", ano=2020, valor=15000.0)
    imposto_moto = moto.calcular_imposto()
    print(f"Imposto da moto: R${imposto_moto}")

    # Exemplo 2: Outro tipo de veículo
    carro = Veiculo(tipo="o", marca="Toyota", ano=2015, valor=25000.0)
    imposto_carro = carro.calcular_imposto()
    print(f"Imposto do carro: R${imposto_carro}")

    # Exemplo 3: Veículo com mais de 30 anos (imposto zero)
    carro_antigo = Veiculo(tipo="o", marca="Chevrolet", ano=1985, valor=8000.0)
    imposto_carro_antigo = carro_antigo.calcular_imposto()
    print(f"Imposto do carro antigo: R${imposto_carro_antigo}")
