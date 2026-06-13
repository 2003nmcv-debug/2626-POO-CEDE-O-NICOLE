# Programa para registrar y mostrar información de mascotas sin usar clases

def registrar_mascota():
    """
    Función para registrar la información de una mascota
    Retorna un diccionario con los datos de la mascota
    """
    print("=" * 50)
    print("Hola bienvenidos a su tienda mascota.")
    print("Ayúdame con los datos de su mascota")
    print("=" * 50)

    nombre = input("\nIngrese el nombre de su mascota: ")
    especie = input("Ingrese la especie de su mascota: ")
    edad = input("Ingrese la edad de su mascota: ")
    color = input("Ingrese el color de su mascota: ")
    peso = input("Ingrese el peso de su mascota (en kg): ")

    # Almacenar los datos en un diccionario
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "color": color,
        "peso": peso
    }

    return mascota


def mostrar_mascota(mascota):
    """
    Función para mostrar la información registrada de forma organizada
    """
    print("\n" + "=" * 50)
    print("INFORMACIÓN DE LA MASCOTA REGISTRADA")
    print("=" * 50)
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")
    print(f"Color:   {mascota['color']}")
    print(f"Peso:    {mascota['peso']} kg")
    print("=" * 50 + "\n")


# Programa principal
def main():
    """Función principal que controla el flujo del programa"""
    mascota = registrar_mascota()
    mostrar_mascota(mascota)
    print("¡Gracias por registrar tu mascota!")


# Ejecutar el programa
if __name__ == "__main__":
    main()
