"""Punto de entrada de la aplicacion grafica del restaurante."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from .servicios.archivo_servicio import ArchivoServicio
    from .servicios.restaurante_servicio import RestauranteServicio
    from .ui.login_view import LoginView
    from .ui.main_view import MainView
except ImportError:  # Allow running main.py directly.
    from servicios.archivo_servicio import ArchivoServicio
    from servicios.restaurante_servicio import RestauranteServicio
    from ui.login_view import LoginView
    from ui.main_view import MainView


class AplicacionRestaurante:
    """Controla la ventana principal y el cambio entre vistas."""

    def __init__(self, raiz: tk.Tk, servicio: RestauranteServicio) -> None:
        self._raiz = raiz
        self._servicio = servicio
        self._vista_actual: ttk.Frame | None = None

    def mostrar_login(self) -> None:
        self._reemplazar_vista(
            LoginView(self._raiz, self._servicio, self.mostrar_principal)
        )

    def mostrar_principal(self, usuario_autenticado) -> None:
        self._reemplazar_vista(
            MainView(self._raiz, self._servicio, usuario_autenticado, self.mostrar_login)
        )

    def _reemplazar_vista(self, vista: ttk.Frame) -> None:
        if self._vista_actual is not None:
            self._vista_actual.destroy()
        self._vista_actual = vista
        self._vista_actual.pack(fill="both", expand=True)


def crear_servicio() -> RestauranteServicio:
    archivo_servicio = ArchivoServicio()
    return RestauranteServicio(
        productos=archivo_servicio.cargar_productos(),
        usuarios=archivo_servicio.cargar_usuarios(),
    )


def main() -> None:
    raiz = tk.Tk()
    raiz.title("Restaurante App")
    raiz.geometry("900x560")
    raiz.minsize(760, 480)

    estilo = ttk.Style(raiz)
    if "clam" in estilo.theme_names():
        estilo.theme_use("clam")

    servicio = crear_servicio()
    aplicacion = AplicacionRestaurante(raiz, servicio)
    aplicacion.mostrar_login()
    raiz.mainloop()


if __name__ == "__main__":
    main()

