class Carta:
    PINTAS = ('Corazones', 'Diamantes', 'Tréboles', 'Picas')

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta
carta1 = Carta('As', 'Corazones')
carta2 = Carta('Reina', 'Picas')

print(carta1.valor, carta1.pinta)  
print(carta2.valor, carta2.pinta)