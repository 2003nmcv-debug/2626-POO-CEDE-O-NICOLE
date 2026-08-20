"""Servicio para cargar y guardar productos en JSON."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from ..modelos.producto import Producto
except ImportError:  # Allow importing the service when main.py runs directly.
    from modelos.producto import Producto


class ArchivoServicio:
    """Centraliza el acceso al archivo de productos."""

    def __init__(self, ruta_archivo: Path | None = None) -> None:
        self._ruta_archivo = (
            ruta_archivo
            if ruta_archivo is not None
            else Path(__file__).resolve().parent.parent / "datos" / "productos.json"
        )
        self._ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

    @property
    def ruta_archivo(self) -> Path:
        return self._ruta_archivo

    def cargar_productos(self) -> list[Producto]:
        """Lee el archivo JSON y reconstruye productos validos."""
        try:
            with self._ruta_archivo.open("r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            if not isinstance(registros, list):
                raise ValueError("El archivo no contiene una lista de productos.")
        except FileNotFoundError:
            print(
                f"No se encontro {self._ruta_archivo}. "
                "El sistema iniciara con una lista vacia."
            )
            return []
        except json.JSONDecodeError:
            print(
                f"El archivo {self._ruta_archivo} contiene JSON invalido. "
                "Se iniciara con una lista vacia."
            )
            return []
        except PermissionError:
            print(
                f"No hay permisos suficientes para leer {self._ruta_archivo}. "
                "Se iniciara con una lista vacia."
            )
            return []
        except ValueError as error:
            print(f"{error} Se iniciara con una lista vacia.")
            return []

        productos: list[Producto] = []
        for indice, registro in enumerate(registros, start=1):
            if not isinstance(registro, dict):
                print(
                    f"Registro {indice} omitido: debe ser un objeto JSON con datos de producto."
                )
                continue

            try:
                producto = Producto.from_dict(registro)
            except KeyError as error:
                print(f"Registro {indice} omitido: falta la clave {error.args[0]!r}.")
                continue
            except ValueError as error:
                print(f"Registro {indice} omitido: {error}")
                continue

            productos.append(producto)

        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        """Sobrescribe el archivo JSON con la coleccion actual de productos."""
        datos = [producto.to_dict() for producto in productos]
        try:
            with self._ruta_archivo.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except PermissionError:
            print(
                f"No hay permisos suficientes para escribir en {self._ruta_archivo}."
            )
            return False

        return True
