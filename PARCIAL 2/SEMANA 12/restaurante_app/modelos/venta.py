"""Modelo Venta para relacionar usuario y producto."""

from __future__ import annotations

from typing import Any


class Venta:
    """Representa una venta registrada en el sistema."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self._usuario_id = self._validar_texto(usuario_id, "usuario_id")
        self._producto_codigo = self._validar_texto(producto_codigo, "producto_codigo")
        self._cantidad = self._validar_cantidad(cantidad)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto = str(valor).strip()
        if not texto:
            raise ValueError(f"El campo '{campo}' no puede estar vacio")
        return texto

    @staticmethod
    def _validar_cantidad(valor: int) -> int:
        try:
            cantidad = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("La cantidad debe ser un entero valido") from error

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        return cantidad

    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @property
    def producto_codigo(self) -> str:
        return self._producto_codigo

    @property
    def cantidad(self) -> int:
        return self._cantidad

    def mostrar_informacion(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def __repr__(self) -> str:
        return (
            "Venta("
            f"usuario_id={self.usuario_id!r}, "
            f"producto_codigo={self.producto_codigo!r}, cantidad={self.cantidad!r})"
        )

    def to_dict(self) -> dict[str, Any]:
        """Convierte la venta a un diccionario compatible con JSON."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Venta":
        """Reconstruye una venta desde un diccionario JSON."""
        return cls(
            usuario_id=data["usuario_id"],
            producto_codigo=data["producto_codigo"],
            cantidad=data["cantidad"],
        )
