from forma_geometrica import FormaGeometrica
from math import pi

class Circulo(FormaGeometrica):
    """Circulo representa a forma geométrica círculo
    
    Attributes:
        raio (float): Raio do círculo.
    """

    def __init__(self, raio: float) -> None:
        super().__init__()
        self.raio = raio

    def calcular_area(self):
        """Calcula a área do círculo"""
        area = pi * self.raio ** 2
        area = f"{area:.3f}"
        return float(area)

    def calcular_perimetro(self):
        """Calcula a circunferência do círculo"""
        peri = 2 * pi * self.raio
        peri = f"{peri:.3f}"
        return float(peri)
    

if __name__ == "__main__":
    circ = Circulo(10)
    print(circ.calcular_area(), circ.calcular_perimetro())
