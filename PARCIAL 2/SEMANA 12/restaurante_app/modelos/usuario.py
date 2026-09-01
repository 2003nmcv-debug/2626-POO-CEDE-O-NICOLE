"""Modelo Usuario para personas registradas en el sistema."""

from __future__ import annotations

from typing import Any


class Usuario:
    """Representa una persona registrada en el restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self._identificacion = self._validar_texto(identificacion, "identificacion")
        self._nombre = self._validar_texto(nombre, "nombre")
        self._correo = self._validar_correo(correo)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto = str(valor).strip()
        if not texto:
            raise ValueError(f"El campo '{campo}' no puede estar vacio")
        return texto

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo_normalizado = str(correo).strip()
        if not correo_normalizado:
            raise ValueError("El correo no puede estar vacio")
        if "@" not in correo_normalizado or "." not in correo_normalizado:
            raise ValueError("El correo debe tener un formato valido")
        return correo_normalizado

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def mostrar_informacion(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Nombre: {self.nombre} | Correo: {self.correo}"
        )

    def __repr__(self) -> str:
        return (
            "Usuario("
            f"identificacion={self.identificacion!r}, "
            f"nombre={self.nombre!r}, correo={self.correo!r})"
        )

    def to_dict(self) -> dict[str, Any]:
        """Serializa el usuario a un diccionario simple para JSON."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Usuario":
        """Crea una instancia de Usuario a partir de un diccionario."""
        return cls(
            identificacion=data["identificacion"],
            nombre=data["nombre"],
            correo=data["correo"],
        )
