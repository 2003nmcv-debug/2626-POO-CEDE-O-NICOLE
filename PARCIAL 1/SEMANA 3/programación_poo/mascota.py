"""
MÓDULO: mascota.py
DESCRIPCIÓN: Define la clase Mascota que representa una mascota real
CONCEPTO: Demuestra Programación Orientada a Objetos (POO)
"""

class Mascota:
    """
    Clase que representa una mascota con sus atributos y métodos.

    CONCEPTOS DEMOSTRADOS:
    - Encapsulación: Agrupa datos (atributos) y comportamientos (métodos)
    - Abstracción: Modelo simplificado de una mascota real
    - Atributos de instancia: Cada objeto tiene sus propios valores
    """

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota - Se ejecuta automáticamente al crear un objeto.

        FUNCIÓN: Inicializar los atributos de la instancia

        Args:
            nombre (str): Nombre de la mascota
            especie (str): Especie de la mascota (perro, gato, pájaro, etc.)
            edad (int): Edad de la mascota en años

        EJEMPLO DE USO:
            mi_mascota = Mascota("Max", "Perro", 3)
        """
        # ATRIBUTOS DE INSTANCIA: Cada mascota tiene valores únicos y independientes
        self.nombre = nombre    # Almacena el nombre de la mascota
        self.especie = especie  # Almacena el tipo de animal
        self.edad = edad        # Almacena la edad en años

    def mostrar_informacion(self):
        """
        Método que muestra la información completa de la mascota en formato ordenado.

        FUNCIÓN: Encapsular la lógica de presentación dentro de la clase
        VENTAJA: Cambios futuros en el formato solo necesitan modificar este método

        EJEMPLO DE SALIDA:
            ==================================================
            INFORMACIÓN DE LA MASCOTA
            ==================================================
            Nombre:   Max
            Especie:  Perro
            Edad:     3 años
            ==================================================
        """
        # Línea decorativa de separación
        print("=" * 50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("=" * 50)

        # Mostrar los atributos de esta instancia usando acceso con "self"
        print(f"Nombre:   {self.nombre}")
        print(f"Especie:  {self.especie}")
        print(f"Edad:     {self.edad} años")

        # Línea decorativa de cierre
        print("=" * 50)

    def hacer_sonido(self):
        """
        Método que emite el sonido característico según la especie de la mascota.

        FUNCIÓN: Demostrar comportamiento específico del objeto

        CONCEPTOS DEMOSTRADOS:
        - Uso de diccionarios dentro de métodos
        - Acceso a atributos de instancia (self.especie)
        - Manejo de casos por defecto con .get()

        NOTA: Si la especie no existe en el diccionario, devuelve sonido genérico
        """

        # DICCIONARIO: Mapea especies a sus sonidos característicos
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau!",
            "pájaro": "¡Pío pío!",
            "caballo": "¡Ijiii!",
            "vaca": "¡Muuu!",
            "gallo": "¡Kikiriki!",
            "pato": "¡Cuac cuac!"
        }

        # CONVERSIÓN A MINÚSCULAS: Permite buscar sin importar mayúsculas/minúsculas
        especie_lower = self.especie.lower()

        # BÚSQUEDA EN DICCIONARIO: .get() devuelve valor o texto por defecto
        sonido = sonidos.get(especie_lower, "*(hace un sonido desconocido)*")

        # MOSTRAR RESULTADO: Accedemos a atributos y imprimimos el sonido
        print(f"\n{self.nombre} ({self.especie}) hace: {sonido}")

