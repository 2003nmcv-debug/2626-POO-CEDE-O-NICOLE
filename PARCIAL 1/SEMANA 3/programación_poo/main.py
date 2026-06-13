# Programa principal - Demostración de Programación Orientada a Objetos
from mascota import Mascota

def main():
    """
    Función principal que crea objetos de la clase Mascota y ejecuta sus métodos.
    """
    print("=" * 50)
    print("TIENDA DE MASCOTAS - PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=" * 50)

    # Crear el primer objeto: Mascota (instancia de la clase Mascota)
    mascota1 = Mascota("Firulais", "Perro", 3)

    # Crear el segundo objeto: Mascota
    mascota2 = Mascota("Whiskers", "Gato", 2)

    # Crear un tercer objeto para demostrar más funcionalidad
    mascota3 = Mascota("Tweety", "Pajaro", 1)

    # Mostrar información y comportamiento de la primera mascota
    print("\n--- MASCOTA 1 ---")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    # Mostrar información y comportamiento de la segunda mascota
    print("\n--- MASCOTA 2 ---")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

    # Mostrar información y comportamiento de la tercera mascota
    print("\n--- MASCOTA 3 ---")
    mascota3.mostrar_informacion()
    mascota3.hacer_sonido()

    # Demostración de acceso a atributos directos
    print("\n" + "=" * 50)
    print("ACCESO A ATRIBUTOS DE LOS OBJETOS")
    print("=" * 50)
    print(f"El nombre de la primera mascota es: {mascota1.nombre}")
    print(f"La especie de la segunda mascota es: {mascota2.especie}")
    print(f"La edad de la tercera mascota es: {mascota3.edad} años")

    print("\n" + "=" * 50)
    print("¡Gracias por visitar la tienda de mascotas!")
    print("=" * 50 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

