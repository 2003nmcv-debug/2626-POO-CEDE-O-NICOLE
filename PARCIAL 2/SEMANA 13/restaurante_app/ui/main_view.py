"""Vista principal del restaurante."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

try:
    from ..modelos.usuario import Usuario
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:  # Allow running main.py directly.
    from modelos.usuario import Usuario
    from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Pantalla principal para consultar usuarios y productos."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        usuario_activo: Usuario,
        on_logout,
    ) -> None:
        super().__init__(master, padding=18)
        self._servicio = servicio
        self._usuario_activo = usuario_activo
        self._on_logout = on_logout
        self._estado_var = tk.StringVar()
        self._crear_interfaz()
        self.mostrar_productos()

    def _crear_interfaz(self) -> None:
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, sticky="ew")
        encabezado.columnconfigure(0, weight=1)

        ttk.Label(
            encabezado,
            text=f"Bienvenido, {self._usuario_activo.nombre}",
            font=("Segoe UI", 16, "bold"),
        ).grid(row=0, column=0, sticky="w")
        ttk.Button(encabezado, text="Cerrar sesión", command=self._on_logout).grid(
            row=0, column=1, sticky="e"
        )

        resumen = ttk.Frame(self, padding=(0, 14, 0, 10))
        resumen.grid(row=1, column=0, sticky="ew")
        ttk.Label(
            resumen,
            text=(
                f"Productos: {self._servicio.obtener_cantidad_productos()}   |   "
                f"Usuarios: {self._servicio.obtener_cantidad_usuarios()}   |   "
                f"Stock total: {self._servicio.obtener_stock_total()}"
            ),
        ).grid(row=0, column=0, sticky="w")

        acciones = ttk.Frame(self)
        acciones.grid(row=2, column=0, sticky="nsew")
        acciones.columnconfigure(0, weight=1)
        acciones.rowconfigure(1, weight=1)

        botones = ttk.Frame(acciones)
        botones.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        for indice in range(4):
            botones.columnconfigure(indice, weight=1)

        ttk.Button(botones, text="Productos", command=self.mostrar_productos).grid(
            row=0, column=0, sticky="ew", padx=(0, 6)
        )
        ttk.Button(botones, text="Usuarios", command=self.mostrar_usuarios).grid(
            row=0, column=1, sticky="ew", padx=6
        )
        ttk.Button(botones, text="Ventas (pendiente)", command=self.mostrar_pendiente).grid(
            row=0, column=2, sticky="ew", padx=6
        )
        ttk.Button(botones, text="Actualizar", command=self.mostrar_productos).grid(
            row=0, column=3, sticky="ew", padx=(6, 0)
        )

        tabla_contenedor = ttk.Frame(acciones)
        tabla_contenedor.grid(row=1, column=0, sticky="nsew")
        tabla_contenedor.rowconfigure(0, weight=1)
        tabla_contenedor.columnconfigure(0, weight=1)

        self._tabla = ttk.Treeview(tabla_contenedor, show="headings", height=12)
        self._tabla.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(
            tabla_contenedor, orient="vertical", command=self._tabla.yview
        )
        scroll.grid(row=0, column=1, sticky="ns")
        self._tabla.configure(yscrollcommand=scroll.set)

        ttk.Label(self, textvariable=self._estado_var, foreground="#1f4d7a").grid(
            row=3, column=0, sticky="w", pady=(10, 0)
        )

    def mostrar_productos(self) -> None:
        productos = self._servicio.listar_productos()
        self._configurar_tabla(("Codigo", "Nombre", "Categoria", "Precio", "Stock"))
        self._limpiar_tabla()

        for producto in productos:
            self._tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"S/. {producto.precio:.2f}",
                    producto.stock,
                ),
            )

        self._estado_var.set(f"Se muestran {len(productos)} productos cargados.")

    def mostrar_usuarios(self) -> None:
        usuarios = self._servicio.listar_usuarios()
        self._configurar_tabla(("Usuario", "Nombre"))
        self._limpiar_tabla()

        for usuario in usuarios:
            self._tabla.insert("", "end", values=(usuario.usuario, usuario.nombre))

        self._estado_var.set(f"Se muestran {len(usuarios)} usuarios cargados.")

    def mostrar_pendiente(self) -> None:
        self._configurar_tabla(("Funcion", "Estado"))
        self._limpiar_tabla()
        self._tabla.insert("", "end", values=("Ventas", "Pendiente de desarrollo"))
        self._estado_var.set("La funcionalidad de ventas se incorporara mas adelante.")

    def _configurar_tabla(self, columnas: tuple[str, ...]) -> None:
        self._tabla["columns"] = columnas
        for columna in columnas:
            self._tabla.heading(columna, text=columna)
            self._tabla.column(columna, anchor="center", stretch=True, width=140)

    def _limpiar_tabla(self) -> None:
        for item in self._tabla.get_children():
            self._tabla.delete(item)

