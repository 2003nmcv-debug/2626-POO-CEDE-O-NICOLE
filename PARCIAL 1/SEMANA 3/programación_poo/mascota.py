"""
Módulo que define la clase Mascota
"""

class Mascota:
    """Clase que representa una mascota con sus atributos y métodos"""

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota

        Args:
            nombre (str): Nombre de la mascota
            especie (str): Especie de la mascota (perro, gato, pájaro, etc.)
            edad (int): Edad de la mascota en años
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Método que muestra la información completa de la mascota"""
        print("=" * 50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("=" * 50)
        print(f"Nombre:   {self.nombre}")
        print(f"Especie:  {self.especie}")
        print(f"Edad:     {self.edad} años")
        print("=" * 50)

    def hacer_sonido(self):
        """Método que emite el sonido característico según la especie"""
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau!",
            "pájaro": "¡Pío pío!",
            "caballo": "¡Ijiii!",
            "vaca": "¡Muuu!",
            "gallo": "¡Kikiriki!",
            "pato": "¡Cuac cuac!"
        }

        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "*(hace un sonido desconocido)*")

        print(f"\n{self.nombre} ({self.especie}) hace: {sonido}")

