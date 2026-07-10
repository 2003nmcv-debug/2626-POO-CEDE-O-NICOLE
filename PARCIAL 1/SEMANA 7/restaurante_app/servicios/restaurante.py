"""
Servicio Restaurante: administra listas de productos y clientes.
Incluye un método cargar_ejemplos() para precargar datos didácticos desde consola.
"""
from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        # listas internas para almacenar objetos
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def cargar_ejemplos(self):
        """Precarga productos y clientes de ejemplo para uso didáctico.
        Los objetos se crean mediante los constructores y se registran mediante
        los métodos del servicio (evitando duplicados).
        """
        ejemplos_p = [
            ('Lomo Saltado', 'Plato Principal', 28.0, True),
            ('Ceviche', 'Entrada', 20.0, True),
            ('Jugo de Maracuyá', 'Bebida', 6.5, True),
            ('Torta de Chocolate', 'Postre', 12.0, False),
        ]
        for nombre, categoria, precio, disponible in ejemplos_p:
            try:
                p = Producto(nombre, categoria, precio, disponible)
                self.registrar_producto(p)
            except ValueError:
                # si ya existe o es inválido, omitir
                pass

        ejemplos_c = [
            ('C001', 'Ana Pérez', 'ana.perez@example.com'),
            ('C002', 'Juan García', 'juan.garcia@example.com'),
        ]
        for idc, nombre, correo in ejemplos_c:
            try:
                c = Cliente(id_cliente=idc, nombre=nombre, correo=correo)
                self.registrar_cliente(c)
            except ValueError:
                pass

    # Métodos para productos
    def registrar_producto(self, producto: Producto):
        """Registra un producto evitando duplicados por nombre (case-insensitive)."""
        if any(p.nombre.lower() == producto.nombre.lower() for p in self._productos):
            raise ValueError("El producto ya está registrado")
        self._productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        """Devuelve copia de la lista de productos."""
        return list(self._productos)

    def buscar_producto(self, termino: str) -> List[Producto]:
        termino = termino.strip().lower()
        return [p for p in self._productos if termino in p.nombre.lower()]

    # Métodos para clientes
    def registrar_cliente(self, cliente: Cliente):
        """Registra un cliente evitando duplicados por id_cliente."""
        if any(c.id_cliente == cliente.id_cliente for c in self._clientes):
            raise ValueError("El cliente ya está registrado")
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        return list(self._clientes)

    def buscar_cliente_por_id(self, id_cliente: str):
        id_cliente = str(id_cliente).strip()
        for c in self._clientes:
            if c.id_cliente == id_cliente:
                return c
        return None