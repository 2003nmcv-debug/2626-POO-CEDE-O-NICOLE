# Clase Producto - Sistema de Gestión de Restaurante

class Producto:
    """
    Clase que representa un producto disponible en el restaurante.
    
    Atributos:
        nombre (str): El nombre del producto (plato, bebida, etc.)
        tipo (str): Categoría del producto (entrada, plato principal, postre, bebida, etc.)
        precio (float): El precio unitario del producto
        disponible (bool): Indica si el producto está disponible para venta
    
    Métodos:
        obtener_info(): Retorna la información del producto como texto
        actualizar_disponibilidad(): Cambia el estado de disponibilidad del producto
    """
    
    def __init__(self, nombre, tipo, precio, disponible=True):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): El nombre del producto
            tipo (str): La categoría del producto
            precio (float): El precio del producto
            disponible (bool): Estado inicial de disponibilidad (por defecto True)
        """
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible
    
    def obtener_info(self):
        """
        Retorna la información del producto de forma estructurada.
        
        Returns:
            str: Información formateada del producto
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} ({self.tipo}) - S/. {self.precio:.2f} - [{estado}]"
    
    def actualizar_disponibilidad(self):
        """
        Cambia el estado de disponibilidad del producto.
        Si estaba disponible, lo marca como no disponible y viceversa.
        """
        self.disponible = not self.disponible
    
    def __str__(self):
        """
        Representación en texto del producto.
        Se ejecuta cuando se imprime el objeto.
        """
        return self.obtener_info()

