class CuentaBancaria:
    def __init__(self, nombre_titular, numero_cuenta, saldo_inicial=0.0):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso: ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad:.2f}")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.nombre_titular}: ${self.saldo:.2f}")

    def __str__(self):
        return (
            f"Cuenta bancaria de {self.nombre_titular}\n"
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Saldo: ${self.saldo:.2f}"
        )


def main():
    cuenta = CuentaBancaria("Ana Pérez", "1234567890", 500.0)
    print(cuenta)
    cuenta.depositar(250.0)
    cuenta.retirar(100.0)
    cuenta.mostrar_saldo()


if __name__ == "__main__":
    main()
