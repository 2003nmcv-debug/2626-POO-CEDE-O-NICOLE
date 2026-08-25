"""Punto de arranque del sistema de restaurante (Semana 11)."""

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

AccionMenu = Callable[[Restaurante], tuple[bool, set[str]]]

OPCIONES_MENU: tuple[tuple[str, str], ...] = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Registrar venta"),
    ("9", "Consultar ventas por usuario"),
    ("10", "Mostrar categorias"),
    ("11", "Salir"),
)


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


def solicitar_entero(mensaje: str, minimo: int = 1) -> int:
    while True:
        texto = input(mensaje).strip()
        try:
            valor = int(texto)
            if valor < minimo:
                raise ValueError
            return valor
        except ValueError:
            print(f"Ingrese un numero entero valido mayor o igual que {minimo}.")


def accion_registrar_producto(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nRegistro de producto")
    codigo = solicitar_texto("Codigo: ")
    nombre = solicitar_texto("Nombre: ")
    categoria = solicitar_texto("Categoria: ")
    precio = solicitar_precio("Precio: ")
    stock = solicitar_entero("Stock: ", minimo=0)

    try:
        restaurante.registrar_producto(Producto(codigo, nombre, categoria, precio, stock))
        print("Producto registrado correctamente.")
        return True, {"productos"}
    except ValueError as error:
        print(f"Error: {error}")
        return True, set()


def accion_buscar_producto(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nBusqueda de producto")
    codigo = solicitar_texto("Codigo a buscar: ")
    producto = restaurante.buscar_producto(codigo)
    if producto is None:
        print("No se encontro un producto con ese codigo.")
    else:
        print(producto.mostrar_informacion())
    return True, set()


def accion_actualizar_producto(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nActualizacion de producto")
    codigo = solicitar_texto("Codigo del producto a actualizar: ")

    if restaurante.buscar_producto(codigo) is None:
        print("No se encontro un producto con ese codigo.")
        return True, set()

    nombre = solicitar_texto("Nuevo nombre: ")
    categoria = solicitar_texto("Nueva categoria: ")
    precio = solicitar_precio("Nuevo precio: ")

    try:
        actualizado = restaurante.actualizar_producto(codigo, nombre, categoria, precio)
        if actualizado:
            print("Producto actualizado correctamente.")
            return True, {"productos"}

        print("No se encontro un producto con ese codigo.")
        return True, set()
    except ValueError as error:
        print(f"Error: {error}")
        return True, set()


def accion_eliminar_producto(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nEliminacion de producto")
    codigo = solicitar_texto("Codigo del producto a eliminar: ")
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
        return True, {"productos"}

    print("No se encontro un producto con ese codigo.")
    return True, set()


def accion_listar_productos(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nListado de productos")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return True, set()

    for producto in productos:
        print(producto.mostrar_informacion())
    return True, set()


def accion_registrar_usuario(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nRegistro de usuario")
    identificacion = solicitar_texto("Identificacion: ")
    nombre = solicitar_texto("Nombre: ")
    correo = solicitar_texto("Correo: ")

    try:
        restaurante.registrar_usuario(Usuario(identificacion, nombre, correo))
        print("Usuario registrado correctamente.")
        return True, {"usuarios"}
    except ValueError as error:
        print(f"Error: {error}")
        return True, set()


def accion_listar_usuarios(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nListado de usuarios")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return True, set()

    for usuario in usuarios:
        print(usuario.mostrar_informacion())
    return True, set()


def accion_registrar_venta(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nRegistro de venta")
    identificacion = solicitar_texto("Identificacion del usuario: ")
    codigo = solicitar_texto("Codigo del producto: ")
    cantidad = solicitar_entero("Cantidad: ")

    if restaurante.vender_producto(codigo, identificacion, cantidad):
        print("Venta registrada correctamente. El stock fue actualizado.")
        return True, {"productos", "ventas"}

    print(
        "No fue posible registrar la venta. Verifique usuario, producto, cantidad y stock."
    )
    return True, set()


def accion_consultar_ventas_usuario(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nConsulta de ventas por usuario")
    identificacion = solicitar_texto("Identificacion del usuario: ")
    usuario = restaurante.buscar_usuario(identificacion)
    if usuario is None:
        print("No se encontro un usuario con esa identificacion.")
        return True, set()

    ventas = restaurante.buscar_ventas_por_usuario(identificacion)
    if not ventas:
        print("No hay ventas registradas para ese usuario.")
        return True, set()

    print(f"Ventas de {usuario.nombre}:")
    for venta in ventas:
        producto = restaurante.buscar_producto(venta.producto_codigo)
        nombre_producto = producto.nombre if producto is not None else "Producto no disponible"
        print(
            f"Codigo: {venta.producto_codigo} | Nombre: {nombre_producto} | "
            f"Cantidad: {venta.cantidad}"
        )
    return True, set()


def accion_mostrar_categorias(restaurante: Restaurante) -> tuple[bool, set[str]]:
    print("\nCategorias registradas")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorias registradas aun.")
        return True, set()

    for categoria in sorted(categorias):
        print(f"- {categoria}")
    return True, set()


def accion_salir(_: Restaurante) -> tuple[bool, set[str]]:
    print("Saliendo del sistema...")
    return False, set()


def main() -> None:
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()
    restaurante.cargar_productos_iniciales(archivo_servicio.cargar_productos())
    restaurante.cargar_usuarios_iniciales(archivo_servicio.cargar_usuarios())
    restaurante.cargar_ventas_iniciales(archivo_servicio.cargar_ventas())

    acciones: dict[str, AccionMenu] = {
        "1": accion_registrar_producto,
        "2": accion_buscar_producto,
        "3": accion_actualizar_producto,
        "4": accion_eliminar_producto,
        "5": accion_listar_productos,
        "6": accion_registrar_usuario,
        "7": accion_listar_usuarios,
        "8": accion_registrar_venta,
        "9": accion_consultar_ventas_usuario,
        "10": accion_mostrar_categorias,
        "11": accion_salir,
    }

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        accion = acciones.get(opcion)
        if accion is None:
            print("Opcion no valida. Intente de nuevo.")
            continue

        continuar, archivos_a_guardar = accion(restaurante)
        if "productos" in archivos_a_guardar:
            archivo_servicio.guardar_productos(restaurante.listar_productos())
        if "usuarios" in archivos_a_guardar:
            archivo_servicio.guardar_usuarios(restaurante.listar_usuarios())
        if "ventas" in archivos_a_guardar:
            archivo_servicio.guardar_ventas(restaurante.listar_ventas())


if __name__ == "__main__":
    main()
