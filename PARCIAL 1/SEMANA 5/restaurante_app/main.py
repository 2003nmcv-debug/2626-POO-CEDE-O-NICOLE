"""
Punto de entrada del sistema de gestión de restaurante.
Demuestra la creación de objetos y su gestión a través del servicio Restaurante.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    """Función principal que ejecuta el sistema de gestión del restaurante."""
    
    # Crear instancia del restaurante
    restaurante: Restaurante = Restaurante("Buen Sabor")
    
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*60)
    
    # ==================== CREAR PRODUCTOS ====================
    # Crear objetos de tipo Producto
    producto_1: Producto = Producto(
        id_producto=101,
        nombre="Pizza Margherita",
        descripcion="Pizza clásica con queso y tomate",
        precio=25000.00,
        disponible=True
    )
    
    producto_2: Producto = Producto(
        id_producto=102,
        nombre="Hamburguesa Premium",
        descripcion="Hamburguesa con carne de res, queso cheddar y tocino",
        precio=18000.00,
        disponible=True
    )
    
    producto_3: Producto = Producto(
        id_producto=103,
        nombre="Jugo Natural de Naranja",
        descripcion="Jugo fresco recién exprimido",
        precio=5000.00,
        disponible=False
    )
    
    producto_4: Producto = Producto(
        id_producto=104,
        nombre="Ensalada Cesar",
        descripcion="Lechuga, pollo, queso parmesano y aderezo especial",
        precio=15000.00,
        disponible=True
    )
    
    # Agregar productos al restaurante
    restaurante.agregar_producto(producto_1)
    restaurante.agregar_producto(producto_2)
    restaurante.agregar_producto(producto_3)
    restaurante.agregar_producto(producto_4)
    
    print("\n[OK] Productos registrados en el sistema")
    
    # ==================== CREAR CLIENTES ====================
    # Crear objetos de tipo Cliente
    cliente_1: Cliente = Cliente(
        id_cliente=201,
        nombre="Carlos Rodriguez",
        email="carlos@email.com",
        telefono="3101234567",
        miembro_premium=True
    )
    
    cliente_2: Cliente = Cliente(
        id_cliente=202,
        nombre="Maria Garcia",
        email="maria@email.com",
        telefono="3107654321",
        miembro_premium=False
    )
    
    cliente_3: Cliente = Cliente(
        id_cliente=203,
        nombre="Juan Lopez",
        email="juan@email.com",
        telefono="3109876543",
        miembro_premium=True
    )
    
    cliente_4: Cliente = Cliente(
        id_cliente=204,
        nombre="Ana Martinez",
        email="ana@email.com",
        telefono="3105555555",
        miembro_premium=False
    )
    
    # Agregar clientes al restaurante
    restaurante.agregar_cliente(cliente_1)
    restaurante.agregar_cliente(cliente_2)
    restaurante.agregar_cliente(cliente_3)
    restaurante.agregar_cliente(cliente_4)
    
    print("[OK] Clientes registrados en el sistema")
    
    # ==================== MOSTRAR INFORMACIÓN ====================
    # Listar todos los productos
    restaurante.listar_productos()
    
    # Listar todos los clientes
    restaurante.listar_clientes()
    
    # Mostrar resumen del restaurante
    restaurante.obtener_resumen()
    
    # ==================== OPERACIONES ADICIONALES ====================
    print(f"\n{'='*60}")
    print("OPERACIONES ADICIONALES")
    print(f"{'='*60}")
    
    # Cambiar disponibilidad de un producto
    print("\n>> Actualizando disponibilidad del Jugo Natural...")
    producto_3.cambiar_disponibilidad(True)
    print(f"  {producto_3.obtener_informacion_corta()} - Ahora disponible")
    
    # Cambiar estado premium de un cliente
    print("\n>> Actualizando estado premium del cliente Maria Garcia...")
    cliente_2.cambiar_estado_premium(True)
    print(f"  {cliente_2.obtener_informacion_corta()}")
    
    # Buscar un cliente específico
    print("\n>> Buscando cliente con ID 203...")
    cliente_encontrado: Cliente | None = restaurante.buscar_cliente(203)
    if cliente_encontrado:
        print(f"  Encontrado: {cliente_encontrado.obtener_informacion_corta()}")
    
    # Eliminar un producto
    print("\n>> Eliminando producto con ID 103 del inventario...")
    if restaurante.eliminar_producto(103):
        print("  Producto eliminado exitosamente")
    
    # Mostrar resumen final
    print(f"\n{'='*60}")
    print("RESUMEN FINAL DESPUÉS DE OPERACIONES")
    print(f"{'='*60}")
    restaurante.obtener_resumen()
    
    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()
