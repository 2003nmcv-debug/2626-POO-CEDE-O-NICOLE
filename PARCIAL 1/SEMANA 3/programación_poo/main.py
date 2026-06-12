"""
Archivo principal que demuestra el uso de la clase Mascota
"""

from mascota import Mascota


def main():
    """Función principal que crea objetos de Mascota y ejecuta sus métodos"""

    print("\n" + "=" * 50)
    print("SISTEMA DE REGISTRO DE MASCOTAS - POO")
    print("=" * 50 + "\n")

    # Crear primer objeto Mascota
    mascota1 = Mascota("Max", "Perro", 3)

    # Crear segundo objeto Mascota
    mascota2 = Mascota("Luna", "Gato", 2)

    # Crear tercer objeto Mascota (extra)
    mascota3 = Mascota("Tweety", "Pájaro", 1)

    # Mostrar información de mascota1
    print("\nMAscota 1:")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    # Mostrar información de mascota2
    print("\n\nMascota 2:")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

    # Mostrar información de mascota3
    print("\n\nMascota 3:")
    mascota3.mostrar_informacion()
    mascota3.hacer_sonido()

    # Resumen de todas las mascotas
    print("\n\n" + "=" * 50)
    print("RESUMEN DE MASCOTAS CREADAS")
    print("=" * 50)
    mascotas = [mascota1, mascota2, mascota3]
    for i, mascota in enumerate(mascotas, 1):
        print(f"\n{i}. {mascota.nombre} - {mascota.especie} ({mascota.edad} años)")

    print("\n" + "=" * 50 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

