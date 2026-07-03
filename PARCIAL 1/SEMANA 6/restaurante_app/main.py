# Punto de entrada principal del sistema restaurante
# Demuestra la creación de objetos, herencia, encapsulación y polimorfismo

from modelos import Platillo, Bebida
from servicios import Restaurante


def main():
    """
    Función principal que ejecuta el sistema de gestión de productos del restaurante.
    Demuestra:
    - Herencia: Platillo y Bebida heredan de Producto
    - Encapsulación: Atributos privados con getters/setters
    - Polimorfismo: mostrar_informacion() personalizado por tipo
    """
    
    # Crear instancia del restaurante
    restaurante = Restaurante("Restaurante Gourmet")
    
    print("\n" + "="*60)
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS - RESTAURANTE")
    print("="*60 + "\n")
    
    # Crear dos objetos de tipo Platillo
    platillo1 = Platillo(
        nombre="Filete Encebollado",
        precio=18.50,
        tipo_platillo="Principal",
        tiempo_preparacion=15,
        disponibilidad=True
    )
    
    platillo2 = Platillo(
        nombre="Pasta Carbonara",
        precio=12.00,
        tipo_platillo="Principal",
        tiempo_preparacion=12,
        disponibilidad=True
    )
    
    # Crear dos objetos de tipo Bebida
    bebida1 = Bebida(
        nombre="Jugo Natural de Naranja",
        precio=4.50,
        tipo_bebida="Refrescante",
        volumen_ml=300,
        disponibilidad=True
    )
    
    bebida2 = Bebida(
        nombre="Vino Tinto Reserva",
        precio=8.00,
        tipo_bebida="Alcohólica",
        volumen_ml=150,
        disponibilidad=True
    )
    
    # Agregar todos los productos al restaurante
    print("Agregando productos al restaurante...\n")
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)
    
    # Mostrar el menú completo (demuestra polimorfismo)
    restaurante.mostrar_menu_completo()
    
    # Demostración de encapsulación: modificar precio con validación
    print("\n--- Demostrando Encapsulación ---\n")
    print("Intentando cambiar el precio del Filete Encebollado:\n")
    platillo1.cambiar_precio(22.00)
    
    print("\nIntentando cambiar el precio del Jugo de Naranja a valor inválido:")
    try:
        bebida1.cambiar_precio(-5.00)  # Esto generará un error por validación
    except ValueError as error:
        print(f"✗ Error capturado: {error}")
    
    # Demostración de encapsulación: modificar disponibilidad
    print("\n--- Demostrando Cambios de Disponibilidad ---\n")
    bebida2.cambiar_disponibilidad(False)
    
    # Mostrar solo los productos disponibles
    restaurante.mostrar_disponibles()
    
    # Demostración de búsqueda de productos
    print("\n--- Búsqueda de Productos ---\n")
    producto_buscado = restaurante.buscar_producto("Pasta Carbonara")
    if producto_buscado:
        print(f"✓ Producto encontrado: {producto_buscado.obtener_nombre()}")
        print(f"  Precio: ${producto_buscado.obtener_precio():.2f}")
    else:
        print("✗ Producto no encontrado")
    
    # Demostración de métodos específicos de cada clase hija
    print("\n--- Métodos Específicos de Clases Hijas ---\n")
    print(f"Tipo de platillo: {platillo1.obtener_tipo_platillo()}")
    print(f"Tiempo de preparación: {platillo1.obtener_tiempo_preparacion()} minutos")
    print()
    print(f"Tipo de bebida: {bebida1.obtener_tipo_bebida()}")
    print(f"Volumen: {bebida1.obtener_volumen()} ml")
    
    # Resumen final
    print(f"\n{'='*60}")
    print(f"  RESUMEN FINAL")
    print(f"{'='*60}")
    print(f"Total de productos en el restaurante: {restaurante.obtener_cantidad_productos()}")
    print(f"Nombre del restaurante: {restaurante.nombre_restaurante}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
