"""Servicio para cargar y guardar productos, usuarios y ventas en JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Protocol, TypeVar

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
    from ..modelos.venta import Venta
except ImportError:  # Allow importing the service when main.py runs directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta

T = TypeVar("T")


class _Serializable(Protocol):
    def to_dict(self) -> dict[str, Any]:
        ...


class ArchivoServicio:
    """Centraliza el acceso a los archivos JSON del sistema."""

    def __init__(self, ruta_base: Path | None = None) -> None:
        self._ruta_base = (
            ruta_base
            if ruta_base is not None
            else Path(__file__).resolve().parent.parent / "datos"
        )
        self._ruta_base.mkdir(parents=True, exist_ok=True)
        self._ruta_productos = self._ruta_base / "productos.json"
        self._ruta_usuarios = self._ruta_base / "usuarios.json"
        self._ruta_ventas = self._ruta_base / "ventas.json"

    @property
    def ruta_base(self) -> Path:
        return self._ruta_base

    def cargar_productos(self) -> list[Producto]:
        return self._cargar_entidades(self._ruta_productos, Producto.from_dict, "producto")

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar_entidades(self._ruta_usuarios, Usuario.from_dict, "usuario")

    def cargar_ventas(self) -> list[Venta]:
        return self._cargar_entidades(self._ruta_ventas, Venta.from_dict, "venta")

    def guardar_productos(self, productos: list[Producto]) -> bool:
        return self._guardar_entidades(self._ruta_productos, productos)

    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        return self._guardar_entidades(self._ruta_usuarios, usuarios)

    def guardar_ventas(self, ventas: list[Venta]) -> bool:
        return self._guardar_entidades(self._ruta_ventas, ventas)

    def _cargar_entidades(
        self,
        ruta: Path,
        constructor: Callable[[dict[str, object]], T],
        etiqueta: str,
    ) -> list[T]:
        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            if not isinstance(registros, list):
                raise ValueError(f"El archivo {ruta.name} no contiene una lista de {etiqueta}s.")
        except FileNotFoundError:
            print(
                f"No se encontro {ruta}. "
                "El sistema iniciara con una lista vacia."
            )
            return []
        except json.JSONDecodeError:
            print(
                f"El archivo {ruta} contiene JSON invalido. "
                "Se iniciara con una lista vacia."
            )
            return []
        except PermissionError:
            print(f"No hay permisos suficientes para leer {ruta}. Se iniciara con una lista vacia.")
            return []
        except ValueError as error:
            print(f"{error} Se iniciara con una lista vacia.")
            return []

        entidades: list[T] = []
        for indice, registro in enumerate(registros, start=1):
            if not isinstance(registro, dict):
                print(
                    f"Registro {indice} omitido: debe ser un objeto JSON con datos de {etiqueta}."
                )
                continue

            try:
                entidad = constructor(registro)
            except KeyError as error:
                print(f"Registro {indice} omitido: falta la clave {error.args[0]!r}.")
                continue
            except ValueError as error:
                print(f"Registro {indice} omitido: {error}")
                continue

            entidades.append(entidad)

        return entidades

    def _guardar_entidades(self, ruta: Path, entidades: list[_Serializable]) -> bool:
        datos = [entidad.to_dict() for entidad in entidades]
        try:
            with ruta.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except PermissionError:
            print(f"No hay permisos suficientes para escribir en {ruta}.")
            return False

        return True
