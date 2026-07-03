# Clase padre: Producto
# Representa un producto general disponible en el restaurante
# Con atributos comunes y métodos de acceso controlado

class Producto:
    """
    Clase padre que representa un producto del restaurante.
    Encapsula los atributos comunes: nombre, precio y disponibilidad.
    """
    
    def __init__(self, nombre, precio, disponibilidad=True):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto (debe ser > 0)
            disponibilidad (bool): Disponibilidad del producto (default: True)
        
        Raises:
            ValueError: Si el precio es menor o igual a 0
        """
        self.__nombre = nombre
        self.__precio = self._validar_precio(precio)
        self._disponibilidad = disponibilidad
    
    def _validar_precio(self, precio):
        """
        Valida que el precio sea un número positivo.
        
        Args:
            precio (float): Precio a validar
        
        Returns:
            float: Precio validado
        
        Raises:
            ValueError: Si el precio no es válido
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        return precio
    
    def obtener_nombre(self):
        """Retorna el nombre del producto."""
        return self.__nombre
    
    def obtener_precio(self):
        """Retorna el precio del producto."""
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """
        Modifica el precio del producto con validación.
        
        Args:
            nuevo_precio (float): Nuevo precio (debe ser > 0)
        
        Raises:
            ValueError: Si el nuevo precio no es válido
        """
        self.__precio = self._validar_precio(nuevo_precio)
        print(f"Precio de '{self.__nombre}' actualizado a: ${self.__precio:.2f}")
    
    def cambiar_disponibilidad(self, disponibilidad):
        """
        Modifica la disponibilidad del producto.
        
        Args:
            disponibilidad (bool): True si está disponible, False si no
        """
        self._disponibilidad = disponibilidad
        estado = "disponible" if disponibilidad else "no disponible"
        print(f"'{self.__nombre}' ahora está {estado}")
    
    def obtener_disponibilidad(self):
        """Retorna el estado de disponibilidad del producto."""
        return self._disponibilidad
    
    def mostrar_informacion(self):
        """
        Muestra la información básica del producto.
        Este método será sobrescrito en las clases hijas (polimorfismo).
        """
        estado = "Disponible" if self._disponibilidad else "No disponible"
        print(f"Nombre: {self.__nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}")
