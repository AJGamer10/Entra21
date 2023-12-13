from forma_geometrica import FormaGeometrica
from math import sqrt

class Triangulo(FormaGeometrica):
    """Triangulo representa a forma geométrica triângulo.
    
    Attributes:
        lado1 (float): Tamanho do primeiro lado do triangulo.
        lado2 (float): Tamanho do segundo lado do triangulo.
        lado3 (float): Tamanho do terceiro lado do triangulo.
    """

    def __init__(self, lado1: float, lado2: float, lado3: float):
        super().__init__()
        if not self.__is_triangle(lado1, lado2, lado3):
            raise AttributeError("Triangulo não é válido")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self) -> float:
        """Calcula a área do triangulo"""
        trangle_type = self.__get_triangle_type(self.lado1, self.lado2, self.lado3)
        if trangle_type == "equi":
            area = (self.lado1 ** 2 * sqrt(3)) / 4
        elif trangle_type == "esca":
            semiperimetro = (self.lado1 + self.lado2 + self.lado3) / 2
            area = (semiperimetro * (semiperimetro - self.lado1) * (semiperimetro - self.lado2) * (semiperimetro - self.lado3)) ** 0.5
        else:
            area = (0.25 * (4 * self.lado2**2 - (self.lado1**2 + self.lado3**2))) ** 0.5 * self.lado2
        
        area = f"{area:.3f}"
        return float(area)

    def calcular_perimetro(self) -> float:
        """Calcula o perímetro do triangulo"""
        peri = self.lado1 + self.lado2 + self.lado3
        peri = f"{peri:.3f}"
        return float(peri)

    def __is_triangle(self, lado1: float, lado2: float, lado3:float):
        return (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2
    
    def __get_triangle_type(self, lado1: float, lado2: float, lado3: float):
        if self.lado2 == self.lado1 == self.lado3:
            return "equi"
        
        if self.lado2 != self.lado1 != self.lado3:
            return "esca"

        return "iso"


if __name__ == "__main__":
    triangulo = Triangulo(10, 6, 5)
    print(triangulo.calcular_area(), triangulo.calcular_perimetro())
