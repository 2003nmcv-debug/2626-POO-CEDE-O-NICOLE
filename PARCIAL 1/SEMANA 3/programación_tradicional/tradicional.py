# ============================================================
# ARCHIVO: tradicional.py
# DESCRIPCIÓN: Sistema de registro de mascotas usando PROGRAMACIÓN TRADICIONAL (Procedural)
# CONCEPTO: Enfoque sin clases - basado en funciones y diccionarios
# ============================================================
#
# CARACTERÍSTICAS PRINCIPALES:
# - Datos y funciones separadas
# - Uso de diccionarios para agrupar datos
# - Funciones que procesan datos
# - Entrada del usuario con input()
# - Control de flujo con bucles y condicionales
# ============================================================


def registrar_mascota():
    """
    FUNCIÓN: Registrar los datos de UNA mascota mediante entrada del teclado

    RESPONSABILIDADES:
    - Mostrar interfaz de bienvenida
    - Solicitar datos al usuario
    - Validar que no estén vacíos (usando .strip())
    - Retornar diccionario con información

    RETORNA:
        dict: Diccionario con claves: nombre, especie, edad, color, peso

    VENTAJAS Y LIMITACIONES (vs POO):
    ✓ Fácil de entender para principiantes
    ✗ No hay reutilización de métodos
    ✗ Lógica dispersa en varias funciones
    """

    # Mostrar interfaz visual
    print("=" * 50)
    print("BIENVENIDO A LA TIENDA DE MASCOTAS")
    print("=" * 50)
    print("\nPor favor, ingrese los datos de su mascota:\n")

    # SECCIÓN: Solicitar datos por teclado
    # .strip() elimina espacios en blanco innecesarios al inicio y final
    nombre = input("Nombre de la mascota: ").strip()
    especie = input("Especie de la mascota (perro/gato/pájaro/otro): ").strip()
    edad = input("Edad de la mascota (en años): ").strip()
    color = input("Color de la mascota: ").strip()
    peso = input("Peso de la mascota (en kg): ").strip()

    # ESTRUCTURA DE DATOS: Diccionario para agrupar datos relacionados
    # Los diccionarios son similares a objetos, pero sin métodos
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "color": color,
        "peso": peso
    }

    # Retornar el diccionario al llamador
    return mascota


def mostrar_mascota(mascota):
    """
    FUNCIÓN: Mostrar la información de una mascota registrada

    PARÁMETRO:
        mascota (dict): Diccionario con información de la mascota

    RESPONSABILIDADES:
    - Recibir diccionario con datos
    - Formatear información de forma legible
    - Mostrar en pantalla

    ACCESO A DATOS:
    - Con diccionarios: mascota['nombre']
    - Con objetos (POO): mascota.nombre (más simple)
    """
    print("\n" + "=" * 50)
    print("INFORMACIÓN DE LA MASCOTA REGISTRADA")
    print("=" * 50)

    # Acceder a valores del diccionario usando las CLAVES entre comillas
    print(f"\nNombre:   {mascota['nombre']}")
    print(f"Especie:  {mascota['especie']}")
    print(f"Edad:     {mascota['edad']} años")
    print(f"Color:    {mascota['color']}")
    print(f"Peso:     {mascota['peso']} kg")
    print("\n" + "=" * 50 + "\n")


def programa_principal():
    """
    FUNCIÓN PRINCIPAL: Controla el flujo completo del programa

    RESPONSABILIDADES:
    - Inicializar variables de control
    - Iterar para permitir múltiples registro
    - Coordinar llamadas a otras funciones
    - Mostrar resumen final

    FLUJO DEL PROGRAMA:
    1. Inicializar: crear variables globales
    2. Bucle while: repetir mientras usuario quiera continuar
    3. Registrar: llamar función registrar_mascota()
    4. Almacenar: guardar en lista
    5. Mostrar: llamar función mostrar_mascota()
    6. Preguntar: ¿registrar otra?
    7. Resumen: mostrar todas si hay más de una
    """

    # ==================== INICIALIZACIÓN ====================
    # Variable de control: governa el bucle while
    continuar = True

    # LISTA para almacenar diccionarios (datos de múltiples mascotas)
    # Similar a crear multiple objetos en POO, pero como diccionarios
    mascotas = []

    # ==================== BUCLE PRINCIPAL ====================
    # Se repite mientras continuar sea True
    while continuar:

        # PASO 1: Registrar nueva mascota usando función
        mascota = registrar_mascota()

        # PASO 2: Agregar diccionario a la lista
        mascotas.append(mascota)

        # PASO 3: Mostrar la mascota registrada
        mostrar_mascota(mascota)

        # PASO 4: Preguntar si desea registrar más
        respuesta = input("¿Desea registrar otra mascota? (si/no): ").strip().lower()

        # CONDICIONAL: Cambiar variable de control
        if respuesta != "si" and respuesta != "s":
            continuar = False  # Sale del bucle

    # ==================== SECCIÓN: RESUMEN FINAL ====================
    # Mostrar resumen solo si se registró más de una mascota
    if len(mascotas) > 1:
        print("\n" + "=" * 50)
        print("RESUMEN DE TODAS LAS MASCOTAS REGISTRADAS")
        print("=" * 50)

        # BUCLE: Iterar sobre la lista de diccionarios
        # enumerate() proporciona índice y elemento
        for i, mascota in enumerate(mascotas, 1):
            print(f"\nMascota {i}:")
            # Acceder a cada valor usando la clave del diccionario
            print(f"  Nombre:   {mascota['nombre']}")
            print(f"  Especie:  {mascota['especie']}")
            print(f"  Edad:     {mascota['edad']} años")
            print(f"  Color:    {mascota['color']}")
            print(f"  Peso:     {mascota['peso']} kg")
        print("\n" + "=" * 50)

    # Mostrar mensaje de despedida
    print("\n¡Gracias por usar el sistema de registro de mascotas!")


# ==================== PUNTO DE ENTRADA DEL PROGRAMA ====================
"""
ESTRUCTURA ESTÁNDAR EN PYTHON:
- if __name__ == "__main__": es la mejor práctica
- Se ejecuta SOLO si el archivo es el principal
- NO se ejecuta si el archivo es importado como módulo

VENTAJAS:
✓ Permite reutilizar código en otros programas
✓ Evita ejecutar código innecesariamente
✓ Código más profesional y estándar
"""

if __name__ == "__main__":
    # Si este archivo se ejecuta directamente, se llama a programa_principal()
    programa_principal()
