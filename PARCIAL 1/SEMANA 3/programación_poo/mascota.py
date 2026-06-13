# Clase Mascota - Programación Orientada a Objetos

class Mascota:
    """
    Clase que representa una mascota.

    Atributos:
        nombre (str): El nombre de la mascota
        especie (str): La especie del animal
        edad (int): La edad de la mascota en años

    Métodos:
        mostrar_informacion(): Muestra la información completa de la mascota
        hacer_sonido(): Reproduce el sonido característico de la mascota
    """

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.

        Args:
            nombre (str): El nombre de la mascota
            especie (str): La especie del animal
            edad (int): La edad de la mascota
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        Método que muestra la información completa de la mascota de forma organizada.
        """
        print("\n" + "=" * 50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("=" * 50)
        print(f"Nombre:  {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad:    {self.edad} años")
        print("=" * 50)

    def hacer_sonido(self):
        """
        Método que reproduce el sonido característico de la mascota según su especie.
        Este método implementa abstracción basada en el tipo de especie.
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau!",
            "pajaro": "¡Pío pío!",
            "hamster": "¡Chic chic!",
            "conejo": "¡Sniff sniff!",
            "pez": "Burbujas...",
        }

        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, f"¡{self.nombre} emite sonidos!")

        print(f"\n{self.nombre} dice: {sonido}")

