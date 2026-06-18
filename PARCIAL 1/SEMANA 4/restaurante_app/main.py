# Programa principal - Sistema de Gestión de Restaurante
# Importamos las clases necesarias
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """
    Función principal que demuestra el funcionamiento del sistema de gestión de restaurante.
    Crea objetos de las clases Producto, Cliente y Restaurante, y ejecuta sus métodos.
    """

    # Mostrar encabezado del programa
    print("\n" + "=" * 70)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE - PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=" * 70)

    # ============================================================================
    # PASO 1: Crear el objeto principal Restaurante
    # ============================================================================
    restaurante = Restaurante("La Buena Mesa")
    print(f"\n✓ Restaurante creado: {restaurante}")

    # ============================================================================
    # PASO 2: Crear objetos Producto y agregarlos al restaurante
    # ============================================================================
    print("\n--- CREANDO PRODUCTOS ---")

    # Crear productos (platos y bebidas)
    producto1 = Producto("Lomo a la Pimienta", "Plato Principal", 45.50)
    producto2 = Producto("Ceviche Peruano", "Entrada", 35.00)
    producto3 = Producto("Causa Limeña", "Entrada", 28.00)
    producto4 = Producto("Ají de Gallina", "Plato Principal", 38.75)
    producto5 = Producto("Chicha Morada", "Bebida", 8.50)
    producto6 = Producto("Flan Casero", "Postre", 15.00)

    # Agregar productos al restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)
    restaurante.agregar_producto(producto5)
    restaurante.agregar_producto(producto6)

    print("✓ Se han agregado 6 productos al catálogo")

    # ============================================================================
    # PASO 3: Crear objetos Cliente y registrarlos en el restaurante
    # ============================================================================
    print("\n--- REGISTRANDO CLIENTES ---")

    # Crear clientes
    cliente1 = Cliente("Juan Pérez", "987654321", "12345678", es_miembro_vip=False)
    cliente2 = Cliente("María García", "987654322", "87654321", es_miembro_vip=True)
    cliente3 = Cliente("Carlos López", "987654323", "11223344", es_miembro_vip=False)
    cliente4 = Cliente("Ana Rodríguez", "987654324", "55667788", es_miembro_vip=True)

    # Registrar clientes en el restaurante
    restaurante.registrar_cliente(cliente1)
    restaurante.registrar_cliente(cliente2)
    restaurante.registrar_cliente(cliente3)
    restaurante.registrar_cliente(cliente4)

    print("✓ Se han registrado 4 clientes en el sistema")

    # ============================================================================
    # PASO 4: Mostrar el catálogo de productos
    # ============================================================================
    restaurante.listar_productos()

    # ============================================================================
    # PASO 5: Mostrar los clientes registrados
    # ============================================================================
    restaurante.listar_clientes()

    # ============================================================================
    # PASO 6: Buscar y mostrar información de un producto específico
    # ============================================================================
    print("\n--- BÚSQUEDA DE PRODUCTO ---")
    producto_buscado = restaurante.buscar_producto("Ceviche Peruano")
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado}")
    else:
        print("Producto no encontrado en el catálogo")

    # ============================================================================
    # PASO 7: Demostración del método especial __str__() y acceso a atributos
    # ============================================================================
    print("\n--- ACCESO A ATRIBUTOS Y MÉTODO __str__() ---")
    print(f"Nombre del restaurante: {restaurante.nombre}")
    print(f"Información del primer producto: {str(producto1)}")
    print(f"Información del primer cliente: {str(cliente1)}")

    # ============================================================================
    # PASO 8: Aplicar descuento VIP a algunos clientes
    # ============================================================================
    print("\n--- CÁLCULO DE DESCUENTOS VIP ---")
    monto_pedido = 100.00

    print(f"\nMonto original del pedido: S/. {monto_pedido:.2f}")
    print(f"Monto para {cliente1.nombre} (Regular): S/. {cliente1.aplicar_descuento_vip(monto_pedido):.2f}")
    print(f"Monto para {cliente2.nombre} (VIP): S/. {cliente2.aplicar_descuento_vip(monto_pedido):.2f}")

    # ============================================================================
    # PASO 9: Cambiar disponibilidad de un producto
    # ============================================================================
    print("\n--- CAMBIO DE DISPONIBILIDAD DE PRODUCTO ---")
    print(f"Estado inicial de {producto5.nombre}: {producto5}")
    producto5.actualizar_disponibilidad()
    print(f"Estado después de cambio: {producto5}")

    # ============================================================================
    # PASO 10: Mostrar resumen final del restaurante
    # ============================================================================
    restaurante.obtener_resumen()

    # ============================================================================
    # PASO 11: Mostrar mensaje de cierre
    # ============================================================================
    print("\n" + "=" * 70)
    print("¡Gracias por usar el Sistema de Gestión de Restaurante!")
    print("=" * 70 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

