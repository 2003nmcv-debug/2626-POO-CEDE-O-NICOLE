"""
Módulo que define la clase Producto.
Representa un plato, bebida o artículo disponible en el restaurante.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.
    
    Atributos:
        id_producto (int): Identificador único del producto
        nombre (str): Nombre del producto (ej: "Pizza Margherita")
        descripcion (str): Descripción detallada del producto
        precio (float): Precio del producto en pesos
        disponible (bool): Indica si el producto está disponible
    """
    
    def __init__(
        self, 
        id_producto: int, 
        nombre: str, 
        descripcion: str, 
        precio: float, 
        disponible: bool = True
    ) -> None:
        """
        Inicializa un nuevo producto con los datos proporcionados.
        
        Args:
            id_producto: Identificador único del producto
            nombre: Nombre descriptivo del producto
            descripcion: Descripción del producto
            precio: Precio en pesos (debe ser positivo)
            disponible: Estado del producto (por defecto True)
        """
        self.id_producto: int = id_producto
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.disponible: bool = disponible
    
    def __str__(self) -> str:
        """Retorna una representación legible del producto."""
        estado: str = "Disponible" if self.disponible else "No disponible"
        return (
            f"[ID: {self.id_producto}] {self.nombre}\n"
            f"  Descripción: {self.descripcion}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Estado: {estado}"
        )
    
    def cambiar_disponibilidad(self, estado: bool) -> None:
        """
        Cambia el estado de disponibilidad del producto.
        
        Args:
            estado: Nuevo estado de disponibilidad (True/False)
        """
        self.disponible = estado
    
    def obtener_informacion_corta(self) -> str:
        """Retorna una representación breve del producto."""
        return f"{self.nombre} (${self.precio:.2f})"
