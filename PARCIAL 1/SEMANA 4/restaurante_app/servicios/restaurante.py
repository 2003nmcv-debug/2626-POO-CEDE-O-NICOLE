# Clase Restaurante - Sistema de Gestión de Restaurante
# Importamos las clases que necesitamos
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que gestiona las operaciones principales del restaurante.

    Atributos:
        nombre (str): El nombre del restaurante
        productos (list): Lista de productos disponibles en el restaurante
        clientes_registrados (list): Lista de clientes registrados en el sistema

    Métodos:
        agregar_producto(): Añade un producto al catálogo del restaurante
        registrar_cliente(): Registra un nuevo cliente en el sistema
        listar_productos(): Muestra todos los productos disponibles
        listar_clientes(): Muestra todos los clientes registrados
        buscar_producto(): Busca un producto por nombre
        obtener_resumen(): Muestra un resumen del estado del restaurante
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre (str): El nombre del restaurante
        """
        self.nombre = nombre
        self.productos = []
        self.clientes_registrados = []

    def agregar_producto(self, producto):
        """
        Añade un producto nuevo al catálogo del restaurante.

        Args:
            producto (Producto): Objeto de tipo Producto a agregar
        """
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el sistema del restaurante.

        Args:
            cliente (Cliente): Objeto de tipo Cliente a registrar
        """
        self.clientes_registrados.append(cliente)

    def listar_productos(self):
        """
        Muestra de forma organizada todos los productos del catálogo.
        """
        print("\n" + "=" * 70)
        print(f"CATÁLOGO DE PRODUCTOS - {self.nombre}")
        print("=" * 70)

        if not self.productos:
            print("No hay productos registrados en el catálogo.")
        else:
            for idx, producto in enumerate(self.productos, 1):
                print(f"{idx}. {producto}")

        print("=" * 70)

    def listar_clientes(self):
        """
        Muestra de forma organizada todos los clientes registrados.
        """
        print("\n" + "=" * 70)
        print(f"CLIENTES REGISTRADOS - {self.nombre}")
        print("=" * 70)

        if not self.clientes_registrados:
            print("No hay clientes registrados en el sistema.")
        else:
            for idx, cliente in enumerate(self.clientes_registrados, 1):
                print(f"{idx}. {cliente}")

        print("=" * 70)

    def buscar_producto(self, nombre_producto):
        """
        Busca un producto en el catálogo por nombre.

        Args:
            nombre_producto (str): El nombre del producto a buscar

        Returns:
            Producto: El objeto del producto si lo encuentra, None si no existe
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None

    def obtener_resumen(self):
        """
        Muestra un resumen general del estado del restaurante.
        """
        print("\n" + "=" * 70)
        print(f"RESUMEN DEL RESTAURANTE: {self.nombre}")
        print("=" * 70)
        print(f"Total de productos en catálogo: {len(self.productos)}")
        print(f"Total de clientes registrados: {len(self.clientes_registrados)}")

        # Contar productos disponibles
        productos_disponibles = sum(1 for p in self.productos if p.disponible)
        print(f"Productos disponibles: {productos_disponibles}")

        # Contar clientes VIP
        clientes_vip = sum(1 for c in self.clientes_registrados if c.es_miembro_vip)
        print(f"Clientes VIP: {clientes_vip}")

        print("=" * 70)

    def __str__(self):
        """
        Representación en texto del restaurante.
        """
        return f"Restaurante: {self.nombre} | Productos: {len(self.productos)} | Clientes: {len(self.clientes_registrados)}"

