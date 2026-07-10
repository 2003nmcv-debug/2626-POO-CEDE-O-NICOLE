from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Menú interactivo para gestionar productos y clientes

def mostrar_menu():
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def main():
    servicio = Restaurante()

    # Preguntar al inicio si se desean cargar datos de ejemplo (didáctico)
    cargar = input("¿Cargar datos de ejemplo didácticos? (s/n): ").strip().lower()
    if cargar == 's':
        servicio.cargar_ejemplos()
        print(f"Se cargaron {len(servicio.listar_productos())} productos y {len(servicio.listar_clientes())} clientes de ejemplo.\n")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Registrar producto desde consola
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría del producto: ")
                precio = input("Precio: ")
                disponible_input = input("Disponible (s/n): ").strip().lower()
                disponible = disponible_input == "s"

                producto = Producto(nombre, categoria, precio, disponible)
                servicio.registrar_producto(producto)
                print("Producto registrado correctamente.\n")
            except Exception as e:
                print(f"Error: {e}\n")

        elif opcion == "2":
            productos = servicio.listar_productos()
            if not productos:
                print("No hay productos registrados.\n")
            else:
                print("Listado de productos:\n")
                for p in productos:
                    print(p.mostrar_informacion())
                print()

        elif opcion == "3":
            termino = input("Ingrese nombre o parte del nombre a buscar: ")
            encontrados = servicio.buscar_producto(termino)
            if not encontrados:
                print("No se encontraron productos.\n")
            else:
                print(f"Se encontraron {len(encontrados)} producto(s):\n")
                for p in encontrados:
                    print(p.mostrar_informacion())
                print()

        elif opcion == "4":
            try:
                id_cliente = input("ID del cliente: ")
                nombre = input("Nombre del cliente: ")
                correo = input("Correo del cliente: ")

                cliente = Cliente(id_cliente=id_cliente, nombre=nombre, correo=correo)
                servicio.registrar_cliente(cliente)
                print("Cliente registrado correctamente.\n")
            except Exception as e:
                print(f"Error: {e}\n")

        elif opcion == "5":
            clientes = servicio.listar_clientes()
            if not clientes:
                print("No hay clientes registrados.\n")
            else:
                print("Listado de clientes:\n")
                for c in clientes:
                    print(f"ID: {c.id_cliente} | Nombre: {c.nombre} | Correo: {c.correo}")
                print()

        elif opcion == "6":
            id_buscar = input("Ingrese ID del cliente a buscar: ")
            cliente = servicio.buscar_cliente_por_id(id_buscar)
            if cliente:
                print(f"ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}\n")
            else:
                print("Cliente no encontrado.\n")

        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")


if __name__ == "__main__":
    main()
