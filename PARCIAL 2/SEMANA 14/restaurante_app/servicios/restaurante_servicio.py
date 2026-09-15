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

    def registrar_producto(self, producto: Producto) -> None:
        clave = self._normalizar(producto.codigo)
        if clave in self._productos_por_codigo:
            raise ValueError("Ya existe un producto con ese codigo.")
        self._productos.append(producto)
        self._productos_por_codigo[clave] = producto

    def editar_producto(
        self, codigo_original: str, nuevo_producto: Producto
    ) -> None:
        clave_original = self._normalizar(codigo_original)
        producto_existente = self._productos_por_codigo.get(clave_original)
        if producto_existente is None:
            raise ValueError("No existe el producto a editar.")

        clave_nueva = self._normalizar(nuevo_producto.codigo)
        if clave_nueva != clave_original and clave_nueva in self._productos_por_codigo:
            raise ValueError("Ya existe otro producto con ese codigo.")

        indice = self._productos.index(producto_existente)
        self._productos[indice] = nuevo_producto
        del self._productos_por_codigo[clave_original]
        self._productos_por_codigo[clave_nueva] = nuevo_producto

    def eliminar_producto(self, codigo: str) -> None:
        clave = self._normalizar(codigo)
        producto = self._productos_por_codigo.get(clave)
        if producto is None:
            raise ValueError("No existe el producto a eliminar.")
        self._productos.remove(producto)
        del self._productos_por_codigo[clave]

    def registrar_usuario(self, usuario: Usuario) -> None:
        clave = self._normalizar(usuario.usuario)
        if clave in self._usuarios_por_usuario:
            raise ValueError("Ya existe un usuario con ese nombre de acceso.")
        self._usuarios.append(usuario)
        self._usuarios_por_usuario[clave] = usuario

    def editar_usuario(
        self, usuario_original: str, nuevo_usuario: Usuario
    ) -> None:
        clave_original = self._normalizar(usuario_original)
        usuario_existente = self._usuarios_por_usuario.get(clave_original)
        if usuario_existente is None:
            raise ValueError("No existe el usuario a editar.")

        clave_nueva = self._normalizar(nuevo_usuario.usuario)
        if clave_nueva != clave_original and clave_nueva in self._usuarios_por_usuario:
            raise ValueError("Ya existe otro usuario con ese nombre de acceso.")

        indice = self._usuarios.index(usuario_existente)
        self._usuarios[indice] = nuevo_usuario
        del self._usuarios_por_usuario[clave_original]
        self._usuarios_por_usuario[clave_nueva] = nuevo_usuario

    def eliminar_usuario(self, usuario: str) -> None:
        clave = self._normalizar(usuario)
        usuario_existente = self._usuarios_por_usuario.get(clave)
        if usuario_existente is None:
            raise ValueError("No existe el usuario a eliminar.")
        self._usuarios.remove(usuario_existente)
        del self._usuarios_por_usuario[clave]

    @staticmethod
    def _normalizar(valor: str) -> str:
        return str(valor).strip().upper()
