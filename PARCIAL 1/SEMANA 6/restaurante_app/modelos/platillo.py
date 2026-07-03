# Clase hija: Platillo
# Hereda de Producto y agrega atributos específicos para platos

from .producto import Producto


class Platillo(Producto):
    """
    Clase que representa un platillo del restaurante.
    Hereda de Producto y agrega atributos específicos como tipo y tiempo de preparación.
    """
    
    def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion, disponibilidad=True):
        """
        Constructor de la clase Platillo.
        Utiliza super() para reutilizar los atributos de la clase padre.
        
        Args:
            nombre (str): Nombre del platillo
            precio (float): Precio del platillo (debe ser > 0)
            tipo_platillo (str): Tipo de platillo (Entrada, Principal, Postre, etc.)
            tiempo_preparacion (int): Tiempo de preparación en minutos
            disponibilidad (bool): Disponibilidad del platillo (default: True)
        """
        super().__init__(nombre, precio, disponibilidad)
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion
    
    def obtener_tipo_platillo(self):
        """Retorna el tipo de platillo."""
        return self.tipo_platillo
    
    def obtener_tiempo_preparacion(self):
        """Retorna el tiempo de preparación en minutos."""
        return self.tiempo_preparacion
    
    def cambiar_tiempo_preparacion(self, nuevo_tiempo):
        """
        Modifica el tiempo de preparación.
        
        Args:
            nuevo_tiempo (int): Nuevo tiempo en minutos
        """
        self.tiempo_preparacion = nuevo_tiempo
        print(f"Tiempo de preparación de '{self.obtener_nombre()}' actualizado a {nuevo_tiempo} min")
    
    def mostrar_informacion(self):
        """
        Muestra la información del platillo.
        Sobrescribe el método de la clase padre (polimorfismo).
        """
        estado = "Disponible" if self.obtener_disponibilidad() else "No disponible"
        print(f"\n[PLATILLO]")
        print(f"  Nombre: {self.obtener_nombre()}")
        print(f"  Precio: ${self.obtener_precio():.2f}")
        print(f"  Tipo: {self.tipo_platillo}")
        print(f"  Tiempo de preparación: {self.tiempo_preparacion} minutos")
        print(f"  Estado: {estado}")
