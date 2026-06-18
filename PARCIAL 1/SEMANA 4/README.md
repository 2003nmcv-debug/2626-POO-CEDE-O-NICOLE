# Sistema de Gestión de Restaurante - Semana 4

## Descripción General

Este proyecto es un **sistema básico de gestión de restaurante** desarrollado en Python utilizando **Programación Orientada a Objetos (POO)**. El objetivo es demostrar cómo organizar un proyecto en módulos, separar responsabilidades y comunicar archivos mediante importaciones.

El sistema permite gestionar:
- **Productos**: Platos, bebidas y postres disponibles en el restaurante
- **Clientes**: Personas que realizan pedidos, con categorización VIP y regular
- **Operaciones del Restaurante**: Agregar productos, registrar clientes, listar información, aplicar descuentos, etc.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase que representa un producto
│   └── cliente.py            # Clase que representa un cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py        # Clase que gestiona el restaurante
└── main.py                   # Punto de entrada del programa
```

### Explicación de carpetas

- **modelos/**: Contiene las clases que representan las entidades principales del sistema
- **servicios/**: Contiene la clase que gestiona las operaciones del restaurante
- **main.py**: Archivo principal que demuestra el funcionamiento del sistema

---

## Clases Implementadas

### 1. Clase `Producto` (`modelos/producto.py`)

Representa un producto disponible en el restaurante.

#### Atributos:
- `nombre` (str): El nombre del producto
- `tipo` (str): Categoría del producto (Entrada, Plato Principal, Bebida, Postre, etc.)
- `precio` (float): Precio unitario del producto
- `disponible` (bool): Estado de disponibilidad (por defecto `True`)

#### Métodos:
- `__init__(nombre, tipo, precio, disponible=True)`: Constructor
- `obtener_info()`: Retorna información formateada del producto
- `actualizar_disponibilidad()`: Cambia el estado de disponibilidad
- `__str__()`: Representación en texto del producto

#### Ejemplo:
```python
producto = Producto("Ceviche Peruano", "Entrada", 35.00)
print(producto)  # Ceviche Peruano (Entrada) - S/. 35.00 - [Disponible]
```

---

### 2. Clase `Cliente` (`modelos/cliente.py`)

Representa un cliente del restaurante.

#### Atributos:
- `nombre` (str): Nombre completo del cliente
- `numero_telefono` (str): Teléfono de contacto
- `numero_documento` (str): Número de identificación
- `es_miembro_vip` (bool): Indica si es miembro VIP (por defecto `False`)

#### Métodos:
- `__init__(nombre, numero_telefono, numero_documento, es_miembro_vip=False)`: Constructor
- `registrar_cliente()`: Retorna mensaje de registro
- `aplicar_descuento_vip(monto_original)`: Calcula descuento del 10% si es VIP
- `obtener_info()`: Retorna información formateada del cliente
- `__str__()`: Representación en texto del cliente

#### Ejemplo:
```python
cliente_vip = Cliente("María García", "987654322", "87654321", es_miembro_vip=True)
print(cliente_vip)  # María García (VIP) - Doc: 87654321 - Tel: 987654322
monto_con_descuento = cliente_vip.aplicar_descuento_vip(100.00)  # 90.0
```

---

### 3. Clase `Restaurante` (`servicios/restaurante.py`)

Gestiona las operaciones principales del restaurante.

#### Atributos:
- `nombre` (str): Nombre del restaurante
- `productos` (list): Lista de productos disponibles
- `clientes_registrados` (list): Lista de clientes registrados

#### Métodos:
- `__init__(nombre)`: Constructor
- `agregar_producto(producto)`: Añade un producto al catálogo
- `registrar_cliente(cliente)`: Registra un cliente en el sistema
- `listar_productos()`: Muestra todos los productos de forma organizada
- `listar_clientes()`: Muestra todos los clientes registrados
- `buscar_producto(nombre_producto)`: Busca un producto por nombre
- `obtener_resumen()`: Muestra un resumen del estado del restaurante
- `__str__()`: Representación en texto del restaurante

#### Ejemplo:
```python
restaurante = Restaurante("La Buena Mesa")
restaurante.agregar_producto(Producto("Lomo a la Pimienta", "Plato Principal", 45.50))
restaurante.registrar_cliente(Cliente("Juan Pérez", "987654321", "12345678"))
restaurante.listar_productos()
restaurante.listar_clientes()
restaurante.obtener_resumen()
```

---

## Funcionalidades del Sistema

El sistema demuestra las siguientes funcionalidades:

✅ **Creación de objetos** de las tres clases principales
✅ **Gestión de catálogo**: Agregar productos al restaurante
✅ **Gestión de clientes**: Registrar clientes en el sistema
✅ **Listado de información**: Mostrar productos y clientes de forma organizada
✅ **Búsqueda**: Buscar productos por nombre
✅ **Cálculo de descuentos**: Aplicar descuento VIP (10%) a clientes especiales
✅ **Control de disponibilidad**: Cambiar el estado de disponibilidad de productos
✅ **Resumen del sistema**: Mostrar estadísticas del restaurante
✅ **Método `__str__()`**: Representación de objetos como texto
✅ **Importaciones correctas**: Comunicación entre módulos mediante imports

---

## Cómo Ejecutar el Programa

### Opción 1: Ejecución desde la terminal
```bash
cd C:\Users\USER\PycharmProjects\2626-POO-CEDE-O-NICOLE\PARCIAL 1\SEMANA 4\restaurante_app
python main.py
```

### Opción 2: Ejecución desde PyCharm
1. Abre el proyecto en PyCharm
2. Navega a la carpeta `SEMANA 4/restaurante_app`
3. Haz clic derecho en `main.py`
4. Selecciona "Run 'main.py'"

---

## Salida Esperada del Programa

```
======================================================================
SISTEMA DE GESTIÓN DE RESTAURANTE - PROGRAMACIÓN ORIENTADA A OBJETOS
======================================================================

✓ Restaurante creado: Restaurante: La Buena Mesa | Productos: 0 | Clientes: 0

--- CREANDO PRODUCTOS ---
✓ Se han agregado 6 productos al catálogo

--- REGISTRANDO CLIENTES ---
✓ Se han registrado 4 clientes en el sistema

======================================================================
CATÁLOGO DE PRODUCTOS - La Buena Mesa
======================================================================
1. Lomo a la Pimienta (Plato Principal) - S/. 45.50 - [Disponible]
2. Ceviche Peruano (Entrada) - S/. 35.00 - [Disponible]
...
======================================================================

======================================================================
CLIENTES REGISTRADOS - La Buena Mesa
======================================================================
1. Juan Pérez (Regular) - Doc: 12345678 - Tel: 987654321
2. María García (VIP) - Doc: 87654321 - Tel: 987654322
...
======================================================================

--- BÚSQUEDA DE PRODUCTO ---
Producto encontrado: Ceviche Peruano (Entrada) - S/. 35.00 - [Disponible]

--- ACCESO A ATRIBUTOS Y MÉTODO __str__() ---
Nombre del restaurante: La Buena Mesa
Información del primer producto: Lomo a la Pimienta (Plato Principal) - S/. 45.50 - [Disponible]
Información del primer cliente: Juan Pérez (Regular) - Doc: 12345678 - Tel: 987654321

--- CÁLCULO DE DESCUENTOS VIP ---
Monto original del pedido: S/. 100.00
Monto para Juan Pérez (Regular): S/. 100.00
Monto para María García (VIP): S/. 90.00

--- CAMBIO DE DISPONIBILIDAD DE PRODUCTO ---
Estado inicial de Chicha Morada: Chicha Morada (Bebida) - S/. 8.50 - [Disponible]
Estado después de cambio: Chicha Morada (Bebida) - S/. 8.50 - [No disponible]

======================================================================
RESUMEN DEL RESTAURANTE: La Buena Mesa
======================================================================
Total de productos en catálogo: 6
Total de clientes registrados: 4
Productos disponibles: 5
Clientes VIP: 2
======================================================================

======================================================================
¡Gracias por usar el Sistema de Gestión de Restaurante!
======================================================================
```

---

## Requisitos Cumplidos

✅ Estructura de carpetas correcta (modelos, servicios, main.py)
✅ Clase `Producto` en `modelos/producto.py`
✅ Clase `Cliente` en `modelos/cliente.py`
✅ Clase `Restaurante` en `servicios/restaurante.py`
✅ Constructor `__init__()` en todas las clases
✅ Atributos pertinentes para el contexto del restaurante
✅ Métodos para gestionar y mostrar información
✅ Método especial `__str__()` en las clases principales
✅ Importaciones correctas entre archivos (`from modelos.producto import Producto`, etc.)
✅ Creación de objetos desde `main.py`
✅ Agregación de objetos al servicio principal
✅ Visualización organizada de información en consola
✅ Comentarios explicativos en el código
✅ No es una copia literal del ejemplo de biblioteca

---

## Conceptos POO Demostrados

### 1. **Encapsulación**
- La clase `Restaurante` gestiona listas internas de productos y clientes
- Los métodos proporcionan interfaz controlada para acceder a esos datos

### 2. **Abstracción**
- Cada clase representa una entidad del dominio del problema
- Los detalles internos se ocultan, exponiendo solo lo necesario

### 3. **Modularización**
- El código se organiza en módulos separados (modelos y servicios)
- Cada módulo tiene una responsabilidad clara

### 4. **Importaciones y Reutilización**
- Las clases se importan en otros módulos según sea necesario
- El archivo `main.py` orquesta la interacción entre todos los módulos

### 5. **Métodos Especiales**
- `__init__()`: Constructor para inicializar objetos
- `__str__()`: Representación legible de los objetos

---

## Posibles Extensiones Futuras

- Agregar clase `Pedido` para registrar pedidos específicos
- Implementar métodos para calcular ingresos totales
- Agregar categorización de productos por tipo
- Implementar sistema de reservas
- Agregar base de datos para persistencia de datos

---

## Reflexión sobre Modularización y Separación de Responsabilidades

La modularización del software es un principio fundamental en la ingeniería de software que permite crear sistemas más mantenibles, escalables y robustos. En este proyecto, se demuestra la importancia de este concepto mediante la separación clara de responsabilidades en tres módulos principales:

### ¿Por qué es importante modularizar?

1. **Responsabilidad Única**: Cada clase tiene una única razón para cambiar. La clase `Producto` solo se ocupa de los atributos del producto, `Cliente` de los datos del cliente, y `Restaurante` de gestionar las operaciones del sistema.

2. **Mantenibilidad**: Cuando el código está organizado en módulos, es más fácil identificar dónde está un problema y solucionarlo sin afectar otras partes del sistema.

3. **Reutilización**: Las clases pueden reutilizarse en otros contextos. Por ejemplo, la clase `Producto` podrían utilizarse en un sistema de tienda online, mientras que `Cliente` podría usarse en un sistema de membresía.

4. **Colaboración en Equipo**: En proyectos grandes, varios desarrolladores pueden trabajar en módulos diferentes simultáneamente sin conflictos.

5. **Escalabilidad**: Agregar nuevas funcionalidades es más simple cuando el código está bien organizado. Por ejemplo, agregar una clase `Pedido` en `modelos/pedido.py` sería directo gracias a la estructura modular existente.

6. **Testing**: Es más fácil escribir pruebas unitarias cuando cada módulo tiene responsabilidades claras.

En este proyecto, la separación entre `modelos` (entidades del dominio) y `servicios` (lógica de negocio) permite que si algún day necesitamos agregar persistencia en base de datos, solo modificaríamos la clase `Restaurante` sin tocar las clases de modelo.

---

## Autor
**Nicole Micaela Cedeño Vizhñay**

## Fecha
2026-06-17

