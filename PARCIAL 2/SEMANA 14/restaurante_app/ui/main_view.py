"""Vista principal del restaurante."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
    from ..servicios.archivo_servicio import ArchivoServicio
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:  # Allow running main.py directly.
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from servicios.archivo_servicio import ArchivoServicio
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
        self._archivo_servicio = ArchivoServicio()
        self._estado_var = tk.StringVar()
        self._vista_actual = "productos"
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
        self._boton_actualizar = botones.grid_slaves(row=0, column=3)[0]

        acciones_crud = ttk.Frame(acciones)
        acciones_crud.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        for indice in range(3):
            acciones_crud.columnconfigure(indice, weight=1)

        ttk.Button(acciones_crud, text="Registrar", command=self._registrar).grid(
            row=0, column=0, sticky="ew", padx=(0, 6)
        )
        ttk.Button(acciones_crud, text="Editar", command=self._editar).grid(
            row=0, column=1, sticky="ew", padx=6
        )
        ttk.Button(acciones_crud, text="Eliminar", command=self._eliminar).grid(
            row=0, column=2, sticky="ew", padx=(6, 0)
        )

        tabla_contenedor = ttk.Frame(acciones)
        tabla_contenedor.grid(row=2, column=0, sticky="nsew")
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
        self._vista_actual = "productos"
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
        self._boton_actualizar.configure(command=self.mostrar_productos)

    def mostrar_usuarios(self) -> None:
        self._vista_actual = "usuarios"
        usuarios = self._servicio.listar_usuarios()
        self._configurar_tabla(("Usuario", "Nombre"))
        self._limpiar_tabla()

        for usuario in usuarios:
            self._tabla.insert("", "end", values=(usuario.usuario, usuario.nombre))

        self._estado_var.set(f"Se muestran {len(usuarios)} usuarios cargados.")
        self._boton_actualizar.configure(command=self.mostrar_usuarios)

    def mostrar_pendiente(self) -> None:
        self._configurar_tabla(("Funcion", "Estado"))
        self._limpiar_tabla()
        self._tabla.insert("", "end", values=("Ventas", "Pendiente de desarrollo"))
        self._estado_var.set("La funcionalidad de ventas se incorporara mas adelante.")
        self._vista_actual = "ventas"
        self._boton_actualizar.configure(command=self.mostrar_pendiente)

    def _registrar(self) -> None:
        if self._vista_actual == "productos":
            self._abrir_formulario_producto()
            return
        if self._vista_actual == "usuarios":
            self._abrir_formulario_usuario()
            return
        self._estado_var.set("Seleccione productos o usuarios para usar CRUD.")

    def _editar(self) -> None:
        seleccionado = self._tabla.selection()
        if not seleccionado:
            self._estado_var.set("Seleccione un registro para editar.")
            return
        valores = self._tabla.item(seleccionado[0], "values")

        if self._vista_actual == "productos":
            self._abrir_formulario_producto(valores=valores)
            return
        if self._vista_actual == "usuarios":
            self._abrir_formulario_usuario(valores=valores)
            return
        self._estado_var.set("Seleccione productos o usuarios para editar.")

    def _eliminar(self) -> None:
        seleccionado = self._tabla.selection()
        if not seleccionado:
            self._estado_var.set("Seleccione un registro para eliminar.")
            return
        valores = self._tabla.item(seleccionado[0], "values")

        if self._vista_actual == "productos":
            codigo = valores[0]
            if not messagebox.askyesno("Confirmar", f"¿Eliminar producto {codigo}?"):
                return
            try:
                self._servicio.eliminar_producto(codigo)
                self._archivo_servicio.guardar_productos(self._servicio.listar_productos())
            except ValueError as error:
                self._estado_var.set(str(error))
                return
            self.mostrar_productos()
            self._estado_var.set(f"Producto {codigo} eliminado.")
            return

        if self._vista_actual == "usuarios":
            usuario = valores[0]
            if not messagebox.askyesno("Confirmar", f"¿Eliminar usuario {usuario}?"):
                return
            try:
                self._servicio.eliminar_usuario(usuario)
                self._archivo_servicio.guardar_usuarios(self._servicio.listar_usuarios())
            except ValueError as error:
                self._estado_var.set(str(error))
                return
            self.mostrar_usuarios()
            self._estado_var.set(f"Usuario {usuario} eliminado.")
            return

        self._estado_var.set("Seleccione productos o usuarios para eliminar.")

    def _abrir_formulario_producto(self, valores: tuple[str, ...] | None = None) -> None:
        ventana = tk.Toplevel(self)
        ventana.title("Producto")
        ventana.resizable(False, False)
        ventana.transient(self.winfo_toplevel())
        ventana.grab_set()

        formulario = ttk.Frame(ventana, padding=14)
        formulario.grid(row=0, column=0, sticky="nsew")

        codigo_var = tk.StringVar(value=valores[0] if valores else "")
        nombre_var = tk.StringVar(value=valores[1] if valores else "")
        categoria_var = tk.StringVar(value=valores[2] if valores else "")
        precio_var = tk.StringVar(value=str(valores[3]).replace("S/. ", "") if valores else "")
        stock_var = tk.StringVar(value=str(valores[4]) if valores else "0")

        campos = [
            ("Codigo:", codigo_var),
            ("Nombre:", nombre_var),
            ("Categoria:", categoria_var),
            ("Precio:", precio_var),
            ("Stock:", stock_var),
        ]
        for fila, (texto, variable) in enumerate(campos):
            ttk.Label(formulario, text=texto).grid(row=fila, column=0, sticky="w", pady=4)
            ttk.Entry(formulario, textvariable=variable, width=28).grid(
                row=fila, column=1, sticky="ew", pady=4
            )

        def guardar() -> None:
            try:
                producto = Producto(
                    codigo=codigo_var.get(),
                    nombre=nombre_var.get(),
                    categoria=categoria_var.get(),
                    precio=float(precio_var.get()),
                    stock=int(stock_var.get()),
                )
                if valores is None:
                    self._servicio.registrar_producto(producto)
                else:
                    self._servicio.editar_producto(valores[0], producto)
                self._archivo_servicio.guardar_productos(self._servicio.listar_productos())
            except ValueError as error:
                messagebox.showerror("Datos invalidos", str(error), parent=ventana)
                return

            ventana.destroy()
            self.mostrar_productos()
            accion = "registrado" if valores is None else "actualizado"
            self._estado_var.set(f"Producto {producto.codigo} {accion}.")

        ttk.Button(formulario, text="Guardar", command=guardar).grid(
            row=len(campos), column=0, columnspan=2, sticky="ew", pady=(10, 0)
        )

    def _abrir_formulario_usuario(self, valores: tuple[str, ...] | None = None) -> None:
        ventana = tk.Toplevel(self)
        ventana.title("Usuario")
        ventana.resizable(False, False)
        ventana.transient(self.winfo_toplevel())
        ventana.grab_set()

        formulario = ttk.Frame(ventana, padding=14)
        formulario.grid(row=0, column=0, sticky="nsew")

        usuario_var = tk.StringVar(value=valores[0] if valores else "")
        nombre_var = tk.StringVar(value=valores[1] if valores else "")
        contrasena_var = tk.StringVar()

        ttk.Label(formulario, text="Usuario:").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(formulario, textvariable=usuario_var, width=28).grid(
            row=0, column=1, sticky="ew", pady=4
        )
        ttk.Label(formulario, text="Nombre:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Entry(formulario, textvariable=nombre_var, width=28).grid(
            row=1, column=1, sticky="ew", pady=4
        )
        ttk.Label(formulario, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(formulario, textvariable=contrasena_var, show="*", width=28).grid(
            row=2, column=1, sticky="ew", pady=4
        )

        def guardar() -> None:
            try:
                if valores is not None and not contrasena_var.get().strip():
                    usuario_existente = next(
                        (
                            item
                            for item in self._servicio.listar_usuarios()
                            if item.usuario.strip().upper() == str(valores[0]).strip().upper()
                        ),
                        None,
                    )
                    if usuario_existente is None:
                        raise ValueError("No se pudo recuperar la contraseña del usuario.")
                    contrasena = usuario_existente.contrasena
                else:
                    contrasena = contrasena_var.get()

                usuario_nuevo = Usuario(
                    usuario=usuario_var.get(),
                    contrasena=contrasena,
                    nombre=nombre_var.get(),
                )
                if valores is None:
                    self._servicio.registrar_usuario(usuario_nuevo)
                else:
                    self._servicio.editar_usuario(valores[0], usuario_nuevo)
                self._archivo_servicio.guardar_usuarios(self._servicio.listar_usuarios())
            except ValueError as error:
                messagebox.showerror("Datos invalidos", str(error), parent=ventana)
                return

            ventana.destroy()
            self.mostrar_usuarios()
            accion = "registrado" if valores is None else "actualizado"
            self._estado_var.set(f"Usuario {usuario_nuevo.usuario} {accion}.")

        ttk.Button(formulario, text="Guardar", command=guardar).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=(10, 0)
        )

    def _configurar_tabla(self, columnas: tuple[str, ...]) -> None:
        self._tabla["columns"] = columnas
        for columna in columnas:
            self._tabla.heading(columna, text=columna)
            self._tabla.column(columna, anchor="center", stretch=True, width=140)

    def _limpiar_tabla(self) -> None:
        for item in self._tabla.get_children():
            self._tabla.delete(item)
