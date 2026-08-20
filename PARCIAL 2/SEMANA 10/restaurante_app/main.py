"""Punto de arranque del sistema de restaurante (Semana 10)."""

from __future__ import annotations

from typing import Callable

try:
    from .modelos.producto import Producto
    from .modelos.usuario import Usuario
    from .servicios.archivo_servicio import ArchivoServicio
    from .servicios.restaurante import Restaurante
except ImportError:  # Allow running main.py directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from servicios.archivo_servicio import ArchivoServicio
    from servicios.restaurante import Restaurante

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

OPCIONES_CON_GUARDADO = {"1", "3", "4"}

AccionMenu = Callable[[Restaurante], tuple[bool, bool]]


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


def accion_registrar_producto(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nRegistro de producto")
    codigo = solicitar_texto("Codigo: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoria: ")
    precio = solicitar_precio("Precio: ")

    try:
        restaurante.registrar_producto(Producto(codigo, nombre, categoria, precio))
        print("Producto registrado correctamente.")
        return True, True
    except ValueError as error:
        print(f"Error: {error}")
        return True, False


def accion_buscar_producto(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nBusqueda de producto")
    codigo = solicitar_texto("Codigo a buscar: ")
    producto = restaurante.buscar_producto(codigo)
    if producto is None:
        print("No se encontro un producto con ese codigo.")
    else:
        print(producto.mostrar_informacion())
    return True, False


def accion_actualizar_producto(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nActualizacion de producto")
    codigo = solicitar_texto("Codigo del producto a actualizar: ")

    if restaurante.buscar_producto(codigo) is None:
        print("No se encontro un producto con ese codigo.")
        return True, False

    nombre = solicitar_texto("Nuevo nombre: ")
    categoria = solicitar_texto("Nueva categoria: ")
    precio = solicitar_precio("Nuevo precio: ")

    try:
        actualizado = restaurante.actualizar_producto(codigo, nombre, categoria, precio)
        if actualizado:
            print("Producto actualizado correctamente.")
            return True, True

        print("No se encontro un producto con ese codigo.")
        return True, False
    except ValueError as error:
        print(f"Error: {error}")
        return True, False


def accion_eliminar_producto(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nEliminacion de producto")
    codigo = solicitar_texto("Codigo del producto a eliminar: ")
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
        return True, True

    print("No se encontro un producto con ese codigo.")
    return True, False


def accion_listar_productos(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nListado de productos")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return True, False

    for producto in productos:
        print(producto.mostrar_informacion())
    return True, False


def accion_registrar_usuario(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nRegistro de usuario")
    identificacion = solicitar_texto("Identificacion: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")

    try:
        restaurante.registrar_usuario(Usuario(identificacion, nombre, correo))
        print("Usuario registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")
    return True, False


def accion_listar_usuarios(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nListado de usuarios")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return True, False

    for usuario in usuarios:
        print(usuario.mostrar_informacion())
    return True, False


def accion_mostrar_categorias(restaurante: Restaurante) -> tuple[bool, bool]:
    print("\nCategorias registradas")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorias registradas aun.")
        return True, False

    for categoria in sorted(categorias):
        print(f"- {categoria}")
    return True, False


def accion_salir(_: Restaurante) -> tuple[bool, bool]:
    print("Saliendo del sistema...")
    return False, False


def main() -> None:
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()
    restaurante.cargar_productos_iniciales(archivo_servicio.cargar_productos())

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

        continuar, modificado = accion(restaurante)
        if modificado and opcion in OPCIONES_CON_GUARDADO:
            archivo_servicio.guardar_productos(restaurante.listar_productos())


if __name__ == "__main__":
    main()
