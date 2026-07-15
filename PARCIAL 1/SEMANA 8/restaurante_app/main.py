"""Punto de arranque del sistema interactivo de restaurante."""

from __future__ import annotations

from modelos.bebida import Bebida
from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def solicitar_texto(mensaje: str) -> str:
    """Solicita texto no vacío por consola."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacío. Intente nuevamente.")


def solicitar_precio(mensaje: str) -> float:
    """Solicita un precio válido mayor que cero."""
    while True:
        texto_precio = input(mensaje).strip().replace(",", ".")
        try:
            precio = float(texto_precio)
            if precio <= 0:
                raise ValueError
            return precio
        except ValueError:
            print("Ingrese un precio válido mayor que cero.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\nRegistro de producto")
    codigo = solicitar_texto("Código del producto: ")
    nombre = solicitar_texto("Nombre del producto: ")
    categoria = solicitar_texto("Categoría del producto: ")
    precio = solicitar_precio("Precio del producto: ")

    try:
        producto = Producto(codigo, nombre, categoria, precio)
        restaurante.registrar_producto(producto)
        print("Producto registrado correctamente.\n")
    except ValueError as error:
        print(f"Error: {error}\n")


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\nRegistro de bebida")
    codigo = solicitar_texto("Código de la bebida: ")
    nombre = solicitar_texto("Nombre de la bebida: ")
    categoria = solicitar_texto("Categoría de la bebida: ")
    precio = solicitar_precio("Precio de la bebida: ")
    tamano = solicitar_texto("Tamaño de la bebida: ")
    tipo_envase = solicitar_texto("Tipo de envase: ")

    try:
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        restaurante.registrar_producto(bebida)
        print("Bebida registrada correctamente.\n")
    except ValueError as error:
        print(f"Error: {error}\n")


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\nRegistro de cliente")
    identificacion = solicitar_texto("Identificación del cliente: ")
    nombre = solicitar_texto("Nombre del cliente: ")
    correo = solicitar_texto("Correo del cliente: ")

    try:
        cliente = Cliente(identificacion, nombre, correo)
        restaurante.registrar_cliente(cliente)
        print("Cliente registrado correctamente.\n")
    except ValueError as error:
        print(f"Error: {error}\n")


def listar_productos(restaurante: Restaurante) -> None:
    print("\nListado de productos")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.\n")
        return

    for producto in productos:
        print(producto.mostrar_informacion())
    print()


def listar_clientes(restaurante: Restaurante) -> None:
    print("\nListado de clientes")
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.\n")
        return

    for cliente in clientes:
        print(cliente.mostrar_informacion())
    print()


def ejecutar_opcion(opcion: str, restaurante: Restaurante) -> bool:
    """Ejecuta la acción asociada al menú y devuelve False si se debe salir."""
    if opcion == "1":
        registrar_producto(restaurante)
    elif opcion == "2":
        registrar_bebida(restaurante)
    elif opcion == "3":
        registrar_cliente(restaurante)
    elif opcion == "4":
        listar_productos(restaurante)
    elif opcion == "5":
        listar_clientes(restaurante)
    elif opcion == "6":
        print("Saliendo del sistema...")
        return False
    else:
        print("Opción no válida. Intente de nuevo.\n")
    return True


def main() -> None:
    restaurante = Restaurante()
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        continuar = ejecutar_opcion(opcion, restaurante)


if __name__ == "__main__":
    main()

