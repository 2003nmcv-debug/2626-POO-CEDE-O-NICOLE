"""
Módulo que define la clase Restaurante.
Administra productos y clientes del restaurante.
"""

from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra el restaurante.
    Gestiona listas de productos y clientes registrados.
    
    Atributos:
        nombre (str): Nombre del restaurante
        productos (List[Producto]): Lista de productos disponibles
        clientes (List[Cliente]): Lista de clientes registrados
    """
    
    def __init__(self, nombre: str) -> None:
        """
        Inicializa un nuevo restaurante.
        
        Args:
            nombre: Nombre del restaurante
        """
        self.nombre: str = nombre
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Objeto Producto a agregar
        """
        self.productos.append(producto)
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un cliente a la lista del restaurante.
        
        Args:
            cliente: Objeto Cliente a agregar
        """
        self.clientes.append(cliente)
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto por su identificador.
        
        Args:
            id_producto: ID del producto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                return True
        return False
    
    def buscar_cliente(self, id_cliente: int) -> Cliente | None:
        """
        Busca un cliente por su identificador.
        
        Args:
            id_cliente: ID del cliente a buscar
            
        Returns:
            Cliente si existe, None en caso contrario
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def listar_productos(self) -> None:
        """Muestra todos los productos registrados en el restaurante."""
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        print(f"\n{'='*60}")
        print(f"PRODUCTOS DE {self.nombre.upper()}")
        print(f"{'='*60}")
        for producto in self.productos:
            print(f"\n{producto}")
    
    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados en el restaurante."""
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        
        print(f"\n{'='*60}")
        print(f"CLIENTES DE {self.nombre.upper()}")
        print(f"{'='*60}")
        for cliente in self.clientes:
            print(f"\n{cliente}")
    
    def contar_productos(self) -> int:
        """Retorna la cantidad total de productos."""
        return len(self.productos)
    
    def contar_clientes(self) -> int:
        """Retorna la cantidad total de clientes."""
        return len(self.clientes)
    
    def obtener_resumen(self) -> None:
        """Muestra un resumen del estado del restaurante."""
        print(f"\n{'='*60}")
        print(f"RESUMEN: {self.nombre.upper()}")
        print(f"{'='*60}")
        print(f"Total de productos: {self.contar_productos()}")
        print(f"Total de clientes: {self.contar_clientes()}")
        
        productos_disponibles: int = sum(
            1 for producto in self.productos if producto.disponible
        )
        clientes_premium: int = sum(
            1 for cliente in self.clientes if cliente.miembro_premium
        )
        
        print(f"Productos disponibles: {productos_disponibles}")
        print(f"Clientes premium: {clientes_premium}")
