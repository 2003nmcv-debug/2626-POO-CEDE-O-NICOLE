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

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        """Reemplaza la coleccion interna por productos cargados desde JSON."""
        self._productos = []
        codigos_registrados: set[str] = set()

        for producto in productos:
            codigo_normalizado = self._normalizar_clave(producto.codigo)
            if codigo_normalizado in codigos_registrados:
                continue

            codigos_registrados.add(codigo_normalizado)
            self._productos.append(producto)

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        """Reemplaza la coleccion interna por usuarios cargados desde JSON."""
        self._usuarios = []
        identificaciones_registradas: set[str] = set()

        for usuario in usuarios:
            identificacion_normalizada = self._normalizar_clave(usuario.identificacion)
            if identificacion_normalizada in identificaciones_registradas:
                continue

            identificaciones_registradas.add(identificacion_normalizada)
            self._usuarios.append(usuario)

    def cargar_ventas_iniciales(self, ventas: list[Venta]) -> None:
        """Carga las ventas recuperadas desde JSON."""
        self._ventas = list(ventas)

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto verificando codigo unico."""
        if self.buscar_producto(producto.codigo) is not None:
            raise ValueError(f"Ya existe un producto con codigo {producto.codigo}")

        self._productos.append(producto)

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_normalizado = self._normalizar_clave(codigo)
        for producto in self._productos:
            if self._normalizar_clave(producto.codigo) == codigo_normalizado:
                return producto
        return None

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
        return True

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def obtener_categorias_unicas(self) -> set[str]:
        """Usa set para devolver categorias sin elementos repetidos."""
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> None:
        if self.buscar_usuario(usuario.identificacion) is not None:
            raise ValueError(
                f"Ya existe un usuario con identificacion {usuario.identificacion}"
            )
        self._usuarios.append(usuario)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        clave = self._normalizar_clave(identificacion)
        for usuario in self._usuarios:
            if self._normalizar_clave(usuario.identificacion) == clave:
                return usuario
        return None

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
        producto.vender(cantidad_solicitada)
        return True

    def buscar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if self._normalizar_clave(venta.usuario_id) == self._normalizar_clave(
                identificacion_usuario
            ):
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return list(self._ventas)

    @staticmethod
    def _normalizar_clave(valor: str) -> str:
        return str(valor).strip().upper()
