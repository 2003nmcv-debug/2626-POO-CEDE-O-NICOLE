"""Servicios de negocio para usuarios y productos."""

from __future__ import annotations

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:  # Allow running main.py directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario


class RestauranteServicio:
    """Concentra las operaciones sobre productos y usuarios."""

    def __init__(
        self,
        productos: list[Producto] | None = None,
        usuarios: list[Usuario] | None = None,
    ) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_usuario: dict[str, Usuario] = {}

        if productos is not None:
            self.cargar_productos_iniciales(productos)
        if usuarios is not None:
            self.cargar_usuarios_iniciales(usuarios)

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        self._productos = []
        self._productos_por_codigo = {}

        for producto in productos:
            clave = self._normalizar(producto.codigo)
            if clave in self._productos_por_codigo:
                continue
            self._productos.append(producto)
            self._productos_por_codigo[clave] = producto

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        self._usuarios = []
        self._usuarios_por_usuario = {}

        for usuario in usuarios:
            clave = self._normalizar(usuario.usuario)
            if clave in self._usuarios_por_usuario:
                continue
            self._usuarios.append(usuario)
            self._usuarios_por_usuario[clave] = usuario

    def validar_acceso(self, usuario: str, contrasena: str) -> Usuario | None:
        usuario_encontrado = self._usuarios_por_usuario.get(self._normalizar(usuario))
        if usuario_encontrado is None:
            return None
        if usuario_encontrado.contrasena != str(contrasena).strip():
            return None
        return usuario_encontrado

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def obtener_cantidad_productos(self) -> int:
        return len(self._productos)

    def obtener_cantidad_usuarios(self) -> int:
        return len(self._usuarios)

    def obtener_stock_total(self) -> int:
        return sum(producto.stock for producto in self._productos)

    @staticmethod
    def _normalizar(valor: str) -> str:
        return str(valor).strip().upper()

