"""Servicio principal que administra productos y clientes del restaurante."""

from __future__ import annotations

from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:
    """Gestiona el registro y el listado de productos y clientes."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto o bebida validando que el código sea único."""
        if self._buscar_producto_por_codigo(producto.codigo) is not None:
            raise ValueError(f"Ya existe un producto con el código {producto.codigo}")
        self._productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        """Retorna una copia de la colección de productos."""
        return list(self._productos)

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente validando que la identificación sea única."""
        if self._buscar_cliente_por_identificacion(cliente.identificacion) is not None:
            raise ValueError(
                f"Ya existe un cliente con la identificación {cliente.identificacion}"
            )
        self._clientes.append(cliente)

    def listar_clientes(self) -> list[Cliente]:
        """Retorna una copia de la colección de clientes."""
        return list(self._clientes)

    def _buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        codigo_normalizado = str(codigo).strip().upper()
        for producto in self._productos:
            if producto.codigo.upper() == codigo_normalizado:
                return producto
        return None

    def _buscar_cliente_por_identificacion(self, identificacion: str) -> Cliente | None:
        identificacion_normalizada = str(identificacion).strip().upper()
        for cliente in self._clientes:
            if cliente.identificacion.upper() == identificacion_normalizada:
                return cliente
        return None

