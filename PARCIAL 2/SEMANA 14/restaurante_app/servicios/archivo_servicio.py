"""Servicio para leer datos JSON locales."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, TypeVar

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:  # Allow running main.py directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario

T = TypeVar("T")


class ArchivoServicio:
    """Centraliza la lectura de archivos JSON del proyecto."""

    def __init__(self, ruta_base: Path | None = None) -> None:
        self._ruta_base = (
            ruta_base
            if ruta_base is not None
            else Path(__file__).resolve().parent.parent / "datos"
        )
        self._ruta_base.mkdir(parents=True, exist_ok=True)
        self._ruta_productos = self._ruta_base / "productos.json"
        self._ruta_usuarios = self._ruta_base / "usuarios.json"

    def cargar_productos(self) -> list[Producto]:
        return self._cargar_entidades(self._ruta_productos, Producto.from_dict, "producto")

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar_entidades(self._ruta_usuarios, Usuario.from_dict, "usuario")

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
                raise ValueError(
                    f"El archivo {ruta.name} no contiene una lista de {etiqueta}s."
                )
        except FileNotFoundError:
            print(f"No se encontro {ruta}. Se cargara una lista vacia.")
            return []
        except json.JSONDecodeError:
            print(f"El archivo {ruta} contiene JSON invalido. Se cargara una lista vacia.")
            return []
        except PermissionError:
            print(f"No hay permisos suficientes para leer {ruta}. Se cargara una lista vacia.")
            return []
        except ValueError as error:
            print(f"{error} Se cargara una lista vacia.")
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

