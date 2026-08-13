"""Servicio principal para administrar productos y usuarios."""

from __future__ import annotations

import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Administra colecciones y operaciones del sistema."""

    def __init__(self) -> None:
        # Directorio y archivos para persistencia
        self._data_dir: Path = Path(__file__).resolve().parent.parent / "data"
        self._data_dir.mkdir(parents=True, exist_ok=True)
        self._productos_file = self._data_dir / "productos.json"
        self._usuarios_file = self._data_dir / "usuarios.json"

        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

        # Cargar datos existentes (si hay)
        self._cargar_productos()
        self._cargar_usuarios()

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto verificando codigo unico."""
        if self.buscar_producto(producto.codigo) is not None:
            raise ValueError(f"Ya existe un producto con codigo {producto.codigo}")
        self._productos.append(producto)
        self._guardar_productos()

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_normalizado = self._normalizar_clave(codigo)
        for producto in self._productos:
            if self._normalizar_clave(producto.codigo) == codigo_normalizado:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto.actualizar_datos(nombre, categoria, precio)
        self._guardar_productos()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        self._guardar_productos()
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
        self._guardar_usuarios()

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

    # ------------------ Persistencia JSON ------------------
    def _cargar_productos(self) -> None:
        try:
            if self._productos_file.exists():
                with self._productos_file.open("r", encoding="utf-8") as fh:
                    data = json.load(fh)
                if isinstance(data, list):
                    productos = []
                    for item in data:
                        try:
                            productos.append(Producto.from_dict(item))
                        except Exception:
                            # ignorar entradas mal formadas
                            continue
                    self._productos = productos
        except Exception as error:
            print(f"No se pudo cargar productos desde {self._productos_file}: {error}")

    def _guardar_productos(self) -> None:
        try:
            data = [p.to_dict() for p in self._productos]
            with self._productos_file.open("w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=2)
        except Exception as error:
            print(f"No se pudo guardar productos en {self._productos_file}: {error}")

    def _cargar_usuarios(self) -> None:
        try:
            if self._usuarios_file.exists():
                with self._usuarios_file.open("r", encoding="utf-8") as fh:
                    data = json.load(fh)
                if isinstance(data, list):
                    usuarios = []
                    for item in data:
                        try:
                            usuarios.append(Usuario.from_dict(item))
                        except Exception:
                            continue
                    self._usuarios = usuarios
        except Exception as error:
            print(f"No se pudo cargar usuarios desde {self._usuarios_file}: {error}")

    def _guardar_usuarios(self) -> None:
        try:
            data = [u.to_dict() for u in self._usuarios]
            with self._usuarios_file.open("w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=2)
        except Exception as error:
            print(f"No se pudo guardar usuarios en {self._usuarios_file}: {error}")

