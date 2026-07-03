# Clase de servicio: Restaurante
# Administra la lista de productos del restaurante

class Restaurante:
    """
    Clase de servicio que administra los productos disponibles en el restaurante.
    Proporciona métodos para agregar, eliminar y mostrar productos.
    """
    
    def __init__(self, nombre_restaurante):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre_restaurante (str): Nombre del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.productos = []  # Lista que almacena todos los productos
    
    def agregar_producto(self, producto):
        """
        Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Objeto de tipo Producto, Platillo o Bebida
        """
        self.productos.append(producto)
        print(f"✓ '{producto.obtener_nombre()}' agregado al restaurante.")
    
    def eliminar_producto(self, nombre_producto):
        """
        Elimina un producto de la lista por su nombre.
        
        Args:
            nombre_producto (str): Nombre del producto a eliminar
        """
        for producto in self.productos:
            if producto.obtener_nombre().lower() == nombre_producto.lower():
                self.productos.remove(producto)
                print(f"✓ '{nombre_producto}' eliminado del restaurante.")
                return
        print(f"✗ Producto '{nombre_producto}' no encontrado.")
    
    def buscar_producto(self, nombre_producto):
        """
        Busca un producto por su nombre.
        
        Args:
            nombre_producto (str): Nombre del producto a buscar
        
        Returns:
            Producto: El objeto producto encontrado, o None si no existe
        """
        for producto in self.productos:
            if producto.obtener_nombre().lower() == nombre_producto.lower():
                return producto
        return None
    
    def obtener_cantidad_productos(self):
        """Retorna la cantidad total de productos registrados."""
        return len(self.productos)
    
    def mostrar_menu_completo(self):
        """
        Muestra la información de todos los productos registrados.
        Demuestra polimorfismo: cada producto muestra su información de manera diferente.
        """
        print(f"\n{'='*60}")
        print(f"  MENÚ DEL RESTAURANTE: {self.nombre_restaurante.upper()}")
        print(f"{'='*60}")
        
        if not self.productos:
            print("\nNo hay productos registrados.")
        else:
            print(f"\nTotal de productos: {self.obtener_cantidad_productos()}")
            print(f"{'-'*60}")
            
            # Polimorfismo: cada objeto muestra su información según su tipo
            for producto in self.productos:
                producto.mostrar_informacion()
            
            print(f"\n{'='*60}\n")
    
    def mostrar_disponibles(self):
        """
        Muestra solo los productos que están disponibles.
        """
        productos_disponibles = [p for p in self.productos if p.obtener_disponibilidad()]
        
        print(f"\n{'='*60}")
        print(f"  PRODUCTOS DISPONIBLES - {self.nombre_restaurante.upper()}")
        print(f"{'='*60}")
        
        if not productos_disponibles:
            print("\nNo hay productos disponibles en este momento.")
        else:
            print(f"\nTotal disponibles: {len(productos_disponibles)}")
            print(f"{'-'*60}")
            
            for producto in productos_disponibles:
                producto.mostrar_informacion()
            
            print(f"\n{'='*60}\n")
