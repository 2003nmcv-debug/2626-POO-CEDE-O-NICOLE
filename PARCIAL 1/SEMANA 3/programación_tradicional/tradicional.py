# Programa de Registro de Mascotas - Programación Tradicional

def registrar_mascota():
    """Función para registrar los datos de una mascota mediante teclado"""
    print("=" * 50)
    print("BIENVENIDO A LA TIENDA DE MASCOTAS")
    print("=" * 50)
    print("\nPor favor, ingrese los datos de su mascota:\n")

    # Solicitar datos por teclado
    nombre = input("Nombre de la mascota: ").strip()
    especie = input("Especie de la mascota (perro/gato/pájaro/otro): ").strip()
    edad = input("Edad de la mascota (en años): ").strip()
    color = input("Color de la mascota: ").strip()
    peso = input("Peso de la mascota (en kg): ").strip()

    # Crear un diccionario con la información
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "color": color,
        "peso": peso
    }

    return mascota


def mostrar_mascota(mascota):
    """Función para mostrar la información registrada de forma organizada"""
    print("\n" + "=" * 50)
    print("INFORMACIÓN DE LA MASCOTA REGISTRADA")
    print("=" * 50)
    print(f"\nNombre:   {mascota['nombre']}")
    print(f"Especie:  {mascota['especie']}")
    print(f"Edad:     {mascota['edad']} años")
    print(f"Color:    {mascota['color']}")
    print(f"Peso:     {mascota['peso']} kg")
    print("\n" + "=" * 50 + "\n")


def programa_principal():
    """Función principal que controla el flujo del programa"""
    continuar = True
    mascotas = []

    while continuar:
        # Registrar mascota
        mascota = registrar_mascota()
        mascotas.append(mascota)

        # Mostrar la mascota registrada
        mostrar_mascota(mascota)

        # Preguntar si desea registrar otra mascota
        respuesta = input("¿Desea registrar otra mascota? (si/no): ").strip().lower()
        if respuesta != "si" and respuesta != "s":
            continuar = False

    # Mostrar resumen de todas las mascotas registradas
    if len(mascotas) > 1:
        print("\n" + "=" * 50)
        print("RESUMEN DE TODAS LAS MASCOTAS REGISTRADAS")
        print("=" * 50)
        for i, mascota in enumerate(mascotas, 1):
            print(f"\nMascota {i}:")
            print(f"  Nombre:   {mascota['nombre']}")
            print(f"  Especie:  {mascota['especie']}")
            print(f"  Edad:     {mascota['edad']} años")
            print(f"  Color:    {mascota['color']}")
            print(f"  Peso:     {mascota['peso']} kg")
        print("\n" + "=" * 50)

    print("\n¡Gracias por usar el sistema de registro de mascotas!")


# Punto de entrada del programa
if __name__ == "__main__":
    programa_principal()
