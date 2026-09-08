"""Vista de acceso para la aplicacion del restaurante."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:  # Allow running main.py directly.
    from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    """Pantalla de acceso simulada."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        on_login_success,
    ) -> None:
        super().__init__(master, padding=24)
        self._servicio = servicio
        self._on_login_success = on_login_success
        self._mensaje_var = tk.StringVar(value="Ingrese sus credenciales para continuar.")
        self._usuario_var = tk.StringVar()
        self._contrasena_var = tk.StringVar()
        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        self.columnconfigure(0, weight=1)

        contenedor = ttk.Frame(self, padding=24)
        contenedor.grid(row=0, column=0, sticky="nsew")
        contenedor.columnconfigure(1, weight=1)

        ttk.Label(contenedor, text="Restaurante App", font=("Segoe UI", 18, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 16)
        )
        ttk.Label(contenedor, text="Usuario:").grid(row=1, column=0, sticky="w", pady=6)
        self._usuario_entry = ttk.Entry(contenedor, textvariable=self._usuario_var, width=28)
        self._usuario_entry.grid(row=1, column=1, sticky="ew", pady=6)
        ttk.Label(contenedor, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=6)
        self._contrasena_entry = ttk.Entry(
            contenedor, textvariable=self._contrasena_var, show="*", width=28
        )
        self._contrasena_entry.grid(row=2, column=1, sticky="ew", pady=6)

        ttk.Button(contenedor, text="Ingresar", command=self._iniciar_sesion).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=(14, 8)
        )
        ttk.Label(
            contenedor,
            textvariable=self._mensaje_var,
            foreground="#7a1f1f",
            wraplength=320,
        ).grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        self._usuario_entry.bind("<Return>", self._manejar_enter)
        self._contrasena_entry.bind("<Return>", self._manejar_enter)

    def _manejar_enter(self, _event) -> None:
        self._iniciar_sesion()

    def _iniciar_sesion(self) -> None:
        usuario = self._usuario_var.get().strip()
        contrasena = self._contrasena_var.get().strip()

        if not usuario or not contrasena:
            self._mensaje_var.set("Debe completar usuario y contraseña.")
            return

        usuario_autenticado = self._servicio.validar_acceso(usuario, contrasena)
        if usuario_autenticado is None:
            self._mensaje_var.set("Credenciales incorrectas. Intente nuevamente.")
            return

        self._mensaje_var.set("")
        self._usuario_var.set("")
        self._contrasena_var.set("")
        self._on_login_success(usuario_autenticado)
