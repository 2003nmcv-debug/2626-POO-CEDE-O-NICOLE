"""Modelo base que representa un producto del restaurante."""

from __future__ import annotations


class Producto:
    """Representa los datos comunes de cualquier producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self._codigo = self._validar_texto(codigo, "código")
        self._nombre = self._validar_texto(nombre, "nombre")
        self._categoria = self._validar_texto(categoria, "categoría")
        self._precio = self._validar_precio(precio)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto = str(valor).strip()
        if not texto:
            raise ValueError(f"El {campo} no puede estar vacío")
        return texto

    @staticmethod
    def _validar_precio(valor: float) -> float:
        try:
            precio = float(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("El precio debe ser un número válido") from error
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        return precio

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def precio(self) -> float:
        return self._precio

    def mostrar_informacion(self) -> str:
        """Devuelve la información del producto en un formato legible."""
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: S/. {self.precio:.2f}"
        )

    def __repr__(self) -> str:
        return (
            "Producto(" 
            f"codigo={self.codigo!r}, nombre={self.nombre!r}, "
            f"categoria={self.categoria!r}, precio={self.precio!r})"
        )

