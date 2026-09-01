"""Servicio principal para administrar productos, usuarios y ventas."""

from __future__ import annotations

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
    from ..modelos.venta import Venta
except ImportError:  # Allow importing the service when main.py runs directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta


class Restaurante:
    """Administra colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        """Reemplaza la coleccion interna por productos cargados desde JSON."""
        self._productos = []
        self._productos_por_codigo = {}

        for producto in productos:
            codigo_normalizado = self._normalizar_clave(producto.codigo)
            if codigo_normalizado in self._productos_por_codigo:
                continue

            self._productos.append(producto)
            self._productos_por_codigo[codigo_normalizado] = producto

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        """Reemplaza la coleccion interna por usuarios cargados desde JSON."""
        self._usuarios = []
        self._usuarios_por_identificacion = {}

        for usuario in usuarios:
            identificacion_normalizada = self._normalizar_clave(usuario.identificacion)
            if identificacion_normalizada in self._usuarios_por_identificacion:
                continue

            self._usuarios.append(usuario)
            self._usuarios_por_identificacion[identificacion_normalizada] = usuario

    def cargar_ventas_iniciales(self, ventas: list[Venta]) -> None:
        """Carga las ventas recuperadas desde JSON."""
        self._ventas = list(ventas)
        self._ventas_por_usuario = {}

        for venta in self._ventas:
            self._agregar_venta_a_indice(venta)

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto verificando codigo unico."""
        codigo_normalizado = self._normalizar_clave(producto.codigo)
        if codigo_normalizado in self._productos_por_codigo:
            raise ValueError(f"Ya existe un producto con codigo {producto.codigo}")

        self._productos.append(producto)
        self._productos_por_codigo[codigo_normalizado] = producto

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self._productos_por_codigo.get(self._normalizar_clave(codigo))

    def actualizar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: float
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        producto.actualizar_datos(nombre, categoria, precio)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        self._productos.remove(producto)
        self._productos_por_codigo.pop(self._normalizar_clave(producto.codigo), None)
        return True

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def obtener_categorias_unicas(self) -> set[str]:
        """Usa set para devolver categorias sin elementos repetidos."""
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> None:
        identificacion_normalizada = self._normalizar_clave(usuario.identificacion)
        if identificacion_normalizada in self._usuarios_por_identificacion:
            raise ValueError(
                f"Ya existe un usuario con identificacion {usuario.identificacion}"
            )
        self._usuarios.append(usuario)
        self._usuarios_por_identificacion[identificacion_normalizada] = usuario

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        return self._usuarios_por_identificacion.get(
            self._normalizar_clave(identificacion)
        )

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def vender_producto(
        self, codigo_producto: str, identificacion_usuario: str, cantidad: int
    ) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        try:
            cantidad_solicitada = int(cantidad)
        except (TypeError, ValueError):
            return False

        if cantidad_solicitada <= 0 or producto.stock < cantidad_solicitada:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad_solicitada)
        self._ventas.append(venta)
        self._agregar_venta_a_indice(venta)
        producto.vender(cantidad_solicitada)
        return True

    def buscar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        clave_usuario = self._normalizar_clave(identificacion_usuario)
        return list(self._ventas_por_usuario.get(clave_usuario, []))

    def listar_ventas(self) -> list[Venta]:
        return list(self._ventas)

    @staticmethod
    def _normalizar_clave(valor: str) -> str:
        return str(valor).strip().upper()

    def _agregar_venta_a_indice(self, venta: Venta) -> None:
        clave_usuario = self._normalizar_clave(venta.usuario_id)
        if clave_usuario not in self._ventas_por_usuario:
            self._ventas_por_usuario[clave_usuario] = []
        self._ventas_por_usuario[clave_usuario].append(venta)
