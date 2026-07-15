"""Modelo Bebida: especialización de Producto para representar bebidas."""

from __future__ import annotations

from modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante y reutiliza la base Producto."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        tipo_envase: str,
    ) -> None:
        super().__init__(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        self._tamano = self._validar_texto(tamano, "tamaño")
        self._tipo_envase = self._validar_texto(tipo_envase, "tipo de envase")

    @property
    def tamano(self) -> str:
        return self._tamano

    @property
    def tipo_envase(self) -> str:
        return self._tipo_envase

    def mostrar_informacion(self) -> str:
        """Extiende la información del producto con datos propios de la bebida."""
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: S/. {self.precio:.2f} | "
            f"Tamaño: {self.tamano} | Envase: {self.tipo_envase}"
        )

    def __repr__(self) -> str:
        return (
            "Bebida(" 
            f"codigo={self.codigo!r}, nombre={self.nombre!r}, categoria={self.categoria!r}, "
            f"precio={self.precio!r}, tamano={self.tamano!r}, tipo_envase={self.tipo_envase!r})"
        )

