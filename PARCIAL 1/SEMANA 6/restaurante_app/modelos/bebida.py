# Clase hija: Bebida
# Hereda de Producto y agrega atributos específicos para bebidas

from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto y agrega atributos específicos como volumen y tipo.
    """
    
    def __init__(self, nombre, precio, tipo_bebida, volumen_ml, disponibilidad=True):
        """
        Constructor de la clase Bebida.
        Utiliza super() para reutilizar los atributos de la clase padre.
        
        Args:
            nombre (str): Nombre de la bebida
            precio (float): Precio de la bebida (debe ser > 0)
            tipo_bebida (str): Tipo de bebida (Refrescante, Alcohólica, Caliente, etc.)
            volumen_ml (int): Volumen de la bebida en mililitros
            disponibilidad (bool): Disponibilidad de la bebida (default: True)
        """
        super().__init__(nombre, precio, disponibilidad)
        self.tipo_bebida = tipo_bebida
        self.volumen_ml = volumen_ml
    
    def obtener_tipo_bebida(self):
        """Retorna el tipo de bebida."""
        return self.tipo_bebida
    
    def obtener_volumen(self):
        """Retorna el volumen de la bebida en mililitros."""
        return self.volumen_ml
    
    def cambiar_volumen(self, nuevo_volumen):
        """
        Modifica el volumen de la bebida.
        
        Args:
            nuevo_volumen (int): Nuevo volumen en mililitros
        """
        self.volumen_ml = nuevo_volumen
        print(f"Volumen de '{self.obtener_nombre()}' actualizado a {nuevo_volumen} ml")
    
    def mostrar_informacion(self):
        """
        Muestra la información de la bebida.
        Sobrescribe el método de la clase padre (polimorfismo).
        """
        estado = "Disponible" if self.obtener_disponibilidad() else "No disponible"
        print(f"\n[BEBIDA]")
        print(f"  Nombre: {self.obtener_nombre()}")
        print(f"  Precio: ${self.obtener_precio():.2f}")
        print(f"  Tipo: {self.tipo_bebida}")
        print(f"  Volumen: {self.volumen_ml} ml")
        print(f"  Estado: {estado}")
