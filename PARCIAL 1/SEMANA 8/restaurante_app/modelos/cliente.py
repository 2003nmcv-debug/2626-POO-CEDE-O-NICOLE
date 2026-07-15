"""Modelo Cliente: representa a una persona registrada en el restaurante."""

from __future__ import annotations


class Cliente:
    """Representa los datos básicos de un cliente del sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self._identificacion = self._validar_texto(identificacion, "identificación")
        self._nombre = self._validar_texto(nombre, "nombre")
        self._correo = self._validar_correo(correo)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto = str(valor).strip()
        if not texto:
            raise ValueError(f"La {campo} no puede estar vacía")
        return texto

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo_normalizado = str(correo).strip()
        if not correo_normalizado:
            raise ValueError("El correo no puede estar vacío")
        if "@" not in correo_normalizado or "." not in correo_normalizado:
            raise ValueError("El correo debe tener un formato válido")
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
        """Devuelve la información del cliente en una sola línea."""
        return f"Identificación: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def __repr__(self) -> str:
        return (
            "Cliente(" 
            f"identificacion={self.identificacion!r}, nombre={self.nombre!r}, correo={self.correo!r})"
        )

