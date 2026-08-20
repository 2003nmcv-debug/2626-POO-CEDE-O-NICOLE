"""Servicio principal para administrar productos y usuarios."""

from __future__ import annotations

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:  # Allow importing the service when main.py runs directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario


class Restaurante:
    """Administra colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

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
        if self._buscar_usuario(usuario.identificacion) is not None:
            raise ValueError(
                f"Ya existe un usuario con identificacion {usuario.identificacion}"
            )
        self._usuarios.append(usuario)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def _buscar_usuario(self, identificacion: str) -> Usuario | None:
        clave = self._normalizar_clave(identificacion)
        for usuario in self._usuarios:
            if self._normalizar_clave(usuario.identificacion) == clave:
                return usuario
        return None

    @staticmethod
    def _normalizar_clave(valor: str) -> str:
        return str(valor).strip().upper()
