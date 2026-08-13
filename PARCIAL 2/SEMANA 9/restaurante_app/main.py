"""Punto de arranque del sistema de restaurante (Semana 9)."""

from __future__ import annotations

from typing import Callable

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

# Tuple: opciones estables del menu durante la ejecucion.
OPCIONES_MENU: tuple[tuple[str, str], ...] = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Mostrar categorias"),
    ("9", "Salir"),
)


AccionMenu = Callable[[Restaurante], bool]


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    for codigo, etiqueta in OPCIONES_MENU:
        print(f"{codigo}. {etiqueta}")


def solicitar_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacio. Intente otra vez.")


def solicitar_precio(mensaje: str) -> float:
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            precio = float(texto)
            if precio <= 0:
                raise ValueError
            return precio
        except ValueError:
            print("Ingrese un precio valido mayor que cero.")


def accion_registrar_producto(restaurante: Restaurante) -> bool:
    print("\nRegistro de producto")
    codigo = solicitar_texto("Codigo: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoria: ")
    precio = solicitar_precio("Precio: ")

    try:
        restaurante.registrar_producto(Producto(codigo, nombre, categoria, precio))
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")
    return True


def accion_buscar_producto(restaurante: Restaurante) -> bool:
    print("\nBusqueda de producto")
    codigo = solicitar_texto("Codigo a buscar: ")
    producto = restaurante.buscar_producto(codigo)
    if producto is None:
        print("No se encontro un producto con ese codigo.")
    else:
        print(producto.mostrar_informacion())
    return True


def accion_actualizar_producto(restaurante: Restaurante) -> bool:
    print("\nActualizacion de producto")
    codigo = solicitar_texto("Codigo del producto a actualizar: ")

    if restaurante.buscar_producto(codigo) is None:
        print("No se encontro un producto con ese codigo.")
        return True

    nombre = solicitar_texto("Nuevo nombre: ")
    categoria = solicitar_texto("Nueva categoria: ")
    precio = solicitar_precio("Nuevo precio: ")

    try:
        actualizado = restaurante.actualizar_producto(codigo, nombre, categoria, precio)
        if actualizado:
            print("Producto actualizado correctamente.")
        else:
            print("No se encontro un producto con ese codigo.")
    except ValueError as error:
        print(f"Error: {error}")
    return True


def accion_eliminar_producto(restaurante: Restaurante) -> bool:
    print("\nEliminacion de producto")
    codigo = solicitar_texto("Codigo del producto a eliminar: ")
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("No se encontro un producto con ese codigo.")
    return True


def accion_listar_productos(restaurante: Restaurante) -> bool:
    print("\nListado de productos")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return True

    for producto in productos:
        print(producto.mostrar_informacion())
    return True


def accion_registrar_usuario(restaurante: Restaurante) -> bool:
    print("\nRegistro de usuario")
    identificacion = solicitar_texto("Identificacion: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")

    try:
        restaurante.registrar_usuario(Usuario(identificacion, nombre, correo))
        print("Usuario registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")
    return True


def accion_listar_usuarios(restaurante: Restaurante) -> bool:
    print("\nListado de usuarios")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return True

    for usuario in usuarios:
        print(usuario.mostrar_informacion())
    return True


def accion_mostrar_categorias(restaurante: Restaurante) -> bool:
    print("\nCategorias registradas")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorias registradas aun.")
        return True

    for categoria in sorted(categorias):
        print(f"- {categoria}")
    return True


def accion_salir(_: Restaurante) -> bool:
    print("Saliendo del sistema...")
    return False


def main() -> None:
    restaurante = Restaurante()

    # Dict: relacion clave -> funcion para ejecutar opcion de menu.
    acciones: dict[str, AccionMenu] = {
        "1": accion_registrar_producto,
        "2": accion_buscar_producto,
        "3": accion_actualizar_producto,
        "4": accion_eliminar_producto,
        "5": accion_listar_productos,
        "6": accion_registrar_usuario,
        "7": accion_listar_usuarios,
        "8": accion_mostrar_categorias,
        "9": accion_salir,
    }

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        accion = acciones.get(opcion)
        if accion is None:
            print("Opcion no valida. Intente de nuevo.")
            continue
        continuar = accion(restaurante)


if __name__ == "__main__":
    main()

