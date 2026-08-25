"""Modelo Producto para el sistema de restaurante."""

from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto con codigo, nombre, categoria, precio y stock."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int = 0,
    ) -> None:
        self._codigo = self._validar_texto(codigo, "codigo")
        self._nombre = self._validar_texto(nombre, "nombre")
        self._categoria = self._validar_texto(categoria, "categoria")
        self._precio = self._validar_precio(precio)
        self._stock = self._validar_stock(stock)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto = str(valor).strip()
        if not texto:
            raise ValueError(f"El campo '{campo}' no puede estar vacio")
        return texto

    @staticmethod
    def _validar_precio(valor: float) -> float:
        try:
            precio = float(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("El precio debe ser un numero valido") from error

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        return precio

    @staticmethod
    def _validar_stock(valor: int) -> int:
        try:
            stock = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("El stock debe ser un entero valido") from error

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        return stock

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

    @property
    def stock(self) -> int:
        return self._stock

    def actualizar_datos(self, nombre: str, categoria: str, precio: float) -> None:
        """Actualiza campos editables del producto."""
        self._nombre = self._validar_texto(nombre, "nombre")
        self._categoria = self._validar_texto(categoria, "categoria")
        self._precio = self._validar_precio(precio)

    def vender(self, cantidad: int) -> None:
        cantidad_validada = self._validar_stock(cantidad)
        if cantidad_validada == 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero")
        if cantidad_validada > self._stock:
            raise ValueError("No hay stock suficiente para realizar la venta")

        self._stock -= cantidad_validada

    def mostrar_informacion(self) -> str:
        return (
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | Precio: S/. {self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def __repr__(self) -> str:
        return (
            "Producto("
            f"codigo={self.codigo!r}, nombre={self.nombre!r}, "
            f"categoria={self.categoria!r}, precio={self.precio!r}, "
            f"stock={self.stock!r})"
        )

    def to_dict(self) -> dict[str, Any]:
        """Convierte el producto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Producto":
        """Reconstruye un producto desde un diccionario JSON."""
        return cls(
            codigo=data["codigo"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio=data["precio"],
            stock=data.get("stock", 0),
        )
