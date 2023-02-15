import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto):
        distancia = self.centro.calcular_distancia(punto)
        if distancia <= self.radio:
            return True
        else:
            return False
p = Punto(1, 2)
c = Circulo(p, 5)

print(c.calcular_area())
print(c.calcular_perimetro())     
print(c.punto_pertenece(p))
print(c.punto_pertenece(Punto(5, 6)))
