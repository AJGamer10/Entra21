from forma_geometrica import FormaGeometrica

class Retangulo(FormaGeometrica):
    """Retangulo representa a forma geométrica retangulo.
    
    Attributes:
        base (float): Tamanho da base do retângulo.
        altura (float): Tamanho da altura do retângulo.
    """

    def __init__(self, base: float, altura: float):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Retorna a área do retângulo"""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Retorna o perímetro do retângulo"""
        return 2 * (self.base + self.altura)
