class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, otro_punto):
        distancia_x = otro_punto.x - self.x
        distancia_y = otro_punto.y - self.y
        distancia = (distancia_x**2 + distancia_y**2)**0.5
        return distancia

p1 = Punto(1, 2)
p2 = Punto(4, 6)
distancia = p1.calcular_distancia(p2)
print(distancia)