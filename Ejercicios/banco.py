class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print('Fondos insuficientes')

    def aplicar_cuota_manejo(self):
        self.balance *= 0.98

    def mostrar_detalles(self):
        print('Número de cuenta:', self.numero_cuenta)
        print('Propietarios:', self.propietarios)
        print('Balance:', self.balance)

cuenta1 = CuentaBancaria('123456', ['Juan Perez', 'Maria Gomez'], 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.aplicar_cuota_manejo()
cuenta1.mostrar_detalles()
