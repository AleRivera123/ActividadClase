class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        ancho = abs(self.esquina2.x - self.esquina1.x)
        alto = abs(self.esquina2.y - self.esquina1.y)
        perimetro = 2 * (ancho + alto)
        return perimetro

    def calcular_area(self):
        ancho = abs(self.esquina2.x - self.esquina1.x)
        alto = abs(self.esquina2.y - self.esquina1.y)
        area = ancho * alto
        return area

    def es_cuadrado(self):
        ancho = abs(self.esquina2.x - self.esquina1.x)
        alto = abs(self.esquina2.y - self.esquina1.y)
        if ancho == alto:
            return True
        else:
            return False

p1 = Punto(1, 2)
p2 = Punto(5, 6)
r = Rectangulo(p1, p2)

print(r.calcular_perimetro())  
print(r.calcular_area())
print(r.es_cuadrado())


