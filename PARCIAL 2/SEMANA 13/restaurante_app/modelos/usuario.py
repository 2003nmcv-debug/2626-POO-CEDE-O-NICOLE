"""Modelo de usuario para la simulacion de acceso."""

from __future__ import annotations

from typing import Any


class Usuario:
    """Representa un usuario para ingreso y consulta en la interfaz."""

    def __init__(self, usuario: str, contrasena: str, nombre: str) -> None:
        self._usuario = self._validar_texto(usuario, "usuario")
        self._contrasena = self._validar_texto(contrasena, "contrasena")
        self._nombre = self._validar_texto(nombre, "nombre")

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto = str(valor).strip()
        if not texto:
            raise ValueError(f"El campo '{campo}' no puede estar vacio")
        return texto

    @property
    def usuario(self) -> str:
        return self._usuario

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @property
    def nombre(self) -> str:
        return self._nombre

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario} | Nombre: {self.nombre}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "nombre": self.nombre,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Usuario":
        return cls(
            usuario=data["usuario"],
            contrasena=data["contrasena"],
            nombre=data["nombre"],
        )

