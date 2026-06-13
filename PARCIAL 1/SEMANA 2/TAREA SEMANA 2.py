"""
PROGRAMA: Sistema de Gestión de Cuenta Bancaria
DESCRIPCIÓN: Este programa implementa una clase CuentaBancaria que simula las operaciones
             básicas de una cuenta de banco (depósitos, retiros y consulta de saldo).
SEMANA: 2
CONCEPTO: Introducción a Programación Orientada a Objetos (POO)
"""


class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con operaciones básicas.

    Atributos:
        nombre_titular (str): Nombre del propietario de la cuenta
        numero_cuenta (str): Número único de identificación de la cuenta
        saldo (float): Cantidad de dinero disponible en la cuenta
    """

    def __init__(self, nombre_titular, numero_cuenta, saldo_inicial=0.0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            nombre_titular (str): Nombre de la persona que posee la cuenta
            numero_cuenta (str): Identificador único de la cuenta bancaria
            saldo_inicial (float): Monto inicial de dinero en la cuenta (por defecto 0.0)
        """
        self.nombre_titular = nombre_titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """
        Realiza un depósito de dinero en la cuenta.

        Args:
            cantidad (float): Monto a depositar (debe ser mayor a cero)
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso: ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        """
        Realiza un retiro de dinero de la cuenta.

        Args:
            cantidad (float): Monto a retirar (debe ser mayor a cero y menor al saldo disponible)
        """
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad:.2f}")

    def mostrar_saldo(self):
        """Muestra el saldo actual de la cuenta de forma legible."""
        print(f"Saldo actual de {self.nombre_titular}: ${self.saldo:.2f}")

    def __str__(self):
        """
        Método especial que define cómo se muestra la cuenta cuando se imprime.
        Retorna una representación en texto con la información principal de la cuenta.
        """
        return (
            f"Cuenta bancaria de {self.nombre_titular}\n"
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Saldo: ${self.saldo:.2f}"
        )


def main():
    """
    Función principal que demuestra el uso de la clase CuentaBancaria.
    Crea una cuenta, realiza operaciones básicas y muestra el resultado.
    """
    # Crear una nueva cuenta bancaria con saldo inicial de $500.00
    cuenta = CuentaBancaria("Ana Pérez", "1234567890", 500.0)

    # Mostrar información inicial de la cuenta
    print(cuenta)

    # Realizar un depósito de $250.00
    cuenta.depositar(250.0)

    # Realizar un retiro de $100.00
    cuenta.retirar(100.0)

    # Mostrar el saldo final
    cuenta.mostrar_saldo()


# Punto de entrada del programa
if __name__ == "__main__":
    main()
