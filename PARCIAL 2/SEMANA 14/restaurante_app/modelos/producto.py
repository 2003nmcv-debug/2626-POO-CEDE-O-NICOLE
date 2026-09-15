"""Modelo de producto para la aplicacion del restaurante."""

from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto registrado en el restaurante."""

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
        self._stock = self._validar_entero(stock, "stock", minimo=0)

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
    def _validar_entero(valor: int, campo: str, minimo: int = 0) -> int:
        try:
            numero = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError(f"El campo '{campo}' debe ser un entero valido") from error

        if numero < minimo:
            raise ValueError(f"El campo '{campo}' no puede ser menor que {minimo}")
        return numero

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

    def mostrar_informacion(self) -> str:
        return (
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | Precio: S/. {self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Producto":
        return cls(
            codigo=data["codigo"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio=data["precio"],
            stock=data.get("stock", data.get("cantidad", 0)),
        )

