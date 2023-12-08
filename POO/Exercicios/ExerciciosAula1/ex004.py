"""
4) Crie uma classe chamada Ponto2D para representar um ponto no espaço cartesiano. 

Essa classe deve ter os atributos: x e y.
Essa classe deve ter o método estático tem_eixo_comum(ponto_a, ponto_b) que retorna 
True se as duas classes tiverem as mesmas coordenadas para algum dos eixos.
"""
from __future__ import annotations


class Ponto2D:
    """Representa um ponto no espaço cartesiano.
    
    Attributes:
        x (int): Eixo das abscissas.
        y (int): Eixo das ordenadas.
    """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    @staticmethod
    def tem_eixo_comum(ponto_a: Ponto2D, ponto_b: Ponto2D) -> bool:
        """Verifica se tem algum eixo em comum entre esses dois pontos.
        
        Args:
            ponto_a (Ponto2D): Primeiro ponto.
            ponto_b (Ponto2D): Segundo ponto.
        
        Returns:
            True se as duas classes tiverem as mesmas coordenadas para algum dos eixos, False caso contrário.
        """
        if ponto_a.y == ponto_b.y or ponto_a.x == ponto_b.x:
            if ponto_a.y == ponto_b.y:
                print("O eixo igual é das ordenadas")
            else:
                print("O eixo igual é das abscissas")
            return True
        else:
            print("Nenhum dos eixos é igual")
        return False
    

if __name__ == "__main__":
    ponto1 = Ponto2D(4, 3)
    ponto2 = Ponto2D(4, 8)
    ponto3 = Ponto2D(7, 3)

    Ponto2D.tem_eixo_comum(ponto1, ponto2)
    Ponto2D.tem_eixo_comum(ponto1, ponto3)
    Ponto2D.tem_eixo_comum(ponto2, ponto3)