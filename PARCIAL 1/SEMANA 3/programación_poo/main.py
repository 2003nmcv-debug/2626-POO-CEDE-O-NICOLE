"""
ARCHIVO: main.py
DESCRIPCIÓN: Programa principal que demuestra el uso de la clase Mascota
CONCEPTO: Programación Orientada a Objetos - Creación y manipulación de objetos

PARTES PRINCIPALES:
1. Importación de módulos
2. Función main()
3. Creación de objetos (instancias)
4. Llamada a métodos
5. Procesamiento de colecciones
6. Punto de entrada del programa
"""

from mascota import Mascota  # Importar la clase Mascota del módulo mascota.py


def main():
    """
    FUNCIÓN PRINCIPAL: Demuestra los conceptos fundamentales de POO

    RESPONSABILIDADES:
    - Crear objetos de la clase Mascota
    - Llamar a métodos de cada objeto
    - Procesar colecciones de objetos

    CONCEPTOS DEMOSTRADOS:
    - Instanciación: Crear objetos específicos de la clase
    - Polimorfismo: Cada objeto responde individualmente a los mismos métodos
    - Colecciones: Agrupar múltiples objetos en una lista
    """

    # ==================== ENCABEZADO DEL PROGRAMA ====================
    print("\n" + "=" * 50)
    print("SISTEMA DE REGISTRO DE MASCOTAS - POO")
    print("=" * 50 + "\n")

    # ==================== SECCIÓN 1: CREACIÓN DE OBJETOS ====================
    # INSTANCIACIÓN: El constructor __init__ se ejecuta automáticamente
    # Cada línea crea un nuevo objeto INDEPENDIENTE con sus propios atributos

    print(">>> CREANDO OBJETOS (INSTANCIAS) DE LA CLASE MASCOTA...\n")

    # Crear primer objeto Mascota - instancia 1
    mascota1 = Mascota("Max", "Perro", 3)
    print("   ✓ Mascota 1 creada: Max (Perro)")

    # Crear segundo objeto Mascota - instancia 2
    mascota2 = Mascota("Luna", "Gato", 2)
    print("   ✓ Mascota 2 creada: Luna (Gato)")

    # Crear tercer objeto Mascota - instancia 3
    mascota3 = Mascota("Tweety", "Pájaro", 1)
    print("   ✓ Mascota 3 creada: Tweety (Pájaro)\n")

    # ==================== SECCIÓN 2: USO DE MÉTODOS ====================
    # Cada objeto ejecuta los métodos con sus PROPIOS datos independientes

    print(">>> ACCEDIENDO A MÉTODOS DE CADA OBJETO...\n")

    # MASCOTA 1: Mostrar información y sonido
    print("MASCOTA 1:")
    mascota1.mostrar_informacion()  # Llama método con datos de mascota1
    mascota1.hacer_sonido()          # Llama método con datos de mascota1

    # MASCOTA 2: Mostrar información y sonido
    print("\n\nMASCOTA 2:")
    mascota2.mostrar_informacion()  # Llama método con datos de mascota2
    mascota2.hacer_sonido()          # Llama método con datos de mascota2

    # MASCOTA 3: Mostrar información y sonido
    print("\n\nMASCOTA 3:")
    mascota3.mostrar_informacion()  # Llama método con datos de mascota3
    mascota3.hacer_sonido()          # Llama método con datos de mascota3

    # ==================== SECCIÓN 3: PROCESAMIENTO DE COLECCIONES ====================
    # Agrupamos múltiples objetos en una lista para procesamiento colectivo

    print("\n\n" + "=" * 50)
    print("RESUMEN DE MASCOTAS CREADAS")
    print("=" * 50)

    # CREAR LISTA: Agrupa las tres instancias de Mascota
    mascotas = [mascota1, mascota2, mascota3]
    print(f"\nTotal de mascotas registered: {len(mascotas)}\n")

    # ITERAR: Acceder a cada objeto secuencialmente
    # enumerate() proporciona el índice (comenzando desde 1) y el objeto
    for i, mascota in enumerate(mascotas, 1):
        # Accedemos a los ATRIBUTOS de cada objeto individual
        print(f"{i}. {mascota.nombre} - {mascota.especie} ({mascota.edad} años)")

    print("\n" + "=" * 50 + "\n")


# ==================== PUNTO DE ENTRADA DEL PROGRAMA ====================
"""
ESTRUCTURA ESTÁNDAR DE PYTHON:
- Esta estructura es la mejor práctica en Python
- Permite que el módulo sea utilizado como biblioteca sin ejecutar código
- if __name__ == "__main__": se ejecuta SOLO si el archivo es el principal

VENTAJAS:
✓ El archivo puede ser importado sin ejecutar main()
✓ El código se ejecuta solo cuando se corre directamente
✓ Permite reutilizar código en otros programas
"""

if __name__ == "__main__":
    # Si este archivo se ejecuta directamente, se llama a main()
    main()

