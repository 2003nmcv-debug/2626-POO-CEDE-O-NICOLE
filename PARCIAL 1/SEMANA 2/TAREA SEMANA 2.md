# Explicación detallada del programa de la clase `CuentaBancaria`

Este documento describe cada parte del programa en `TAREA SEMANA 2.py`. El objetivo es ayudarte a entender los conceptos básicos de programación orientada a objetos (POO).

## 1. ¿Qué es una clase?

Una clase es una plantilla para crear objetos. En POO, un objeto representa un elemento del mundo real con características (atributos) y acciones (métodos).

En este archivo, la clase se llama `CuentaBancaria` y representa una cuenta de banco.

## 2. Definición de la clase

```python
class CuentaBancaria:
```

- `class` es una palabra reservada de Python que inicia la definición de una nueva clase.
- `CuentaBancaria` es el nombre de la clase.

## 3. El método `__init__`

```python
    def __init__(self, nombre_titular, numero_cuenta, saldo_inicial=0.0):
        self.nombre_titular = nombre_titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
```

- `__init__` se conoce como el constructor de la clase.
- Se ejecuta automáticamente cuando se crea un objeto nuevo.
- `self` es una referencia al objeto que se está creando. Siempre debe aparecer como primer parámetro en los métodos de instancia.
- `nombre_titular`, `numero_cuenta` y `saldo_inicial` son valores que se entregan al crear la cuenta.
- Dentro del constructor, se guardan esos valores en el objeto con `self.nombre_titular`, `self.numero_cuenta` y `self.saldo`.

## 4. Método `depositar`

```python
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso: ${cantidad:.2f}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
```

- Este método permite agregar dinero a la cuenta.
- Recibe `cantidad` como parámetro.
- Si la cantidad es mayor que cero, el saldo se incrementa.
- Si la cantidad no es válida, muestra un mensaje de error.

## 5. Método `retirar`

```python
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad:.2f}")
```

- Este método permite sacar dinero de la cuenta.
- Primero verifica que la cantidad sea mayor que cero.
- Luego comprueba si hay suficiente saldo.
- Si todo está bien, resta el valor del saldo.

## 6. Método `mostrar_saldo`

```python
    def mostrar_saldo(self):
        print(f"Saldo actual de {self.nombre_titular}: ${self.saldo:.2f}")
```

- Muestra el saldo actual de la cuenta.
- Usa el nombre del titular y el saldo guardado en el objeto.

## 7. Método especial `__str__`

```python
    def __str__(self):
        return (
            f"Cuenta bancaria de {self.nombre_titular}\n"
            f"Número de cuenta: {self.numero_cuenta}\n"
            f"Saldo: ${self.saldo:.2f}"
        )
```

- `__str__` define cómo se muestra el objeto cuando se imprime.
- Permite ver la información de la cuenta de forma clara.

## 8. Función `main()`

```python
def main():
    cuenta = CuentaBancaria("Ana Pérez", "1234567890", 500.0)
    print(cuenta)
    cuenta.depositar(250.0)
    cuenta.retirar(100.0)
    cuenta.mostrar_saldo()
```

- Esta función crea un objeto `CuentaBancaria` llamado `cuenta`.
- Se crea con un saldo inicial de `500.0`.
- Luego imprime la cuenta, deposita dinero, retira dinero y muestra el saldo.

## 9. Bloque `if __name__ == "__main__"`

```python
if __name__ == "__main__":
    main()
```

- Este bloque permite que el archivo se ejecute como programa principal.
- Si abres este archivo directamente, se ejecuta `main()`.
- Si importas la clase desde otro archivo, este bloque no corre automáticamente.

## 10. ¿Por qué es útil la programación orientada a objetos?

- Permite organizar el código usando objetos que representan cosas reales.
- Cada objeto guarda sus propios datos (atributos) y puede hacer acciones (métodos).
- Facilita reutilizar y extender el programa cuando creces en experiencia.

## 11. Ejemplo visual del flujo

1. Creamos una cuenta con `CuentaBancaria("Ana Pérez", "1234567890", 500.0)`.
2. Imprimimos la cuenta con `print(cuenta)` y se usa `__str__`.
3. Llamamos a `cuenta.depositar(250.0)` y el saldo aumenta.
4. Llamamos a `cuenta.retirar(100.0)` y el saldo disminuye.
5. Llamamos a `cuenta.mostrar_saldo()` para ver cuánto dinero queda.

---

Si quieres, puedo ayudarte a agregar más ejemplos con otras clases como `Libro`, `Auto` o `Estudiante`.