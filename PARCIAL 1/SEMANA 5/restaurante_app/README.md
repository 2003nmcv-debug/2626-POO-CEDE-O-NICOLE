# Sistema de Gestión de Restaurante

## Descripción

Sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Demuestra el uso de clases, objetos, tipos de datos básicos, listas, métodos especiales y convenciones de nomenclatura de Python.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante
└── main.py                  # Punto de entrada
```

## Clases Implementadas

### 1. Clase Producto (`modelos/producto.py`)

Representa un plato, bebida o artículo disponible en el restaurante.

**Atributos:**
- `id_producto: int` - Identificador único del producto
- `nombre: str` - Nombre descriptivo del producto
- `descripcion: str` - Descripción detallada
- `precio: float` - Precio en pesos
- `disponible: bool` - Estado de disponibilidad

**Métodos:**
- `__init__()` - Inicializa un nuevo producto
- `__str__()` - Representación legible del producto
- `cambiar_disponibilidad()` - Actualiza el estado de disponibilidad
- `obtener_informacion_corta()` - Retorna una representación breve

### 2. Clase Cliente (`modelos/cliente.py`)

Representa una persona registrada en el sistema del restaurante.

**Atributos:**
- `id_cliente: int` - Identificador único del cliente
- `nombre: str` - Nombre completo
- `email: str` - Correo electrónico
- `telefono: str` - Número de teléfono
- `miembro_premium: bool` - Estado de membresía premium

**Métodos:**
- `__init__()` - Inicializa un nuevo cliente
- `__str__()` - Representación legible del cliente
- `cambiar_estado_premium()` - Actualiza el estado de membresía
- `obtener_informacion_corta()` - Retorna una representación breve

### 3. Clase Restaurante (`servicios/restaurante.py`)

Administra las listas de productos y clientes del restaurante.

**Atributos:**
- `nombre: str` - Nombre del restaurante
- `productos: List[Producto]` - Lista de productos
- `clientes: List[Cliente]` - Lista de clientes

**Métodos:**
- `__init__()` - Inicializa el restaurante
- `agregar_producto()` - Agrega un producto a la lista
- `agregar_cliente()` - Agrega un cliente a la lista
- `eliminar_producto()` - Elimina un producto por ID
- `buscar_cliente()` - Busca un cliente por ID
- `listar_productos()` - Muestra todos los productos
- `listar_clientes()` - Muestra todos los clientes
- `contar_productos()` - Retorna la cantidad de productos
- `contar_clientes()` - Retorna la cantidad de clientes
- `obtener_resumen()` - Muestra un resumen del estado del restaurante

## Ejecutar el Programa

```bash
cd restaurante_app
python main.py
```

## Características Demonstradas

✓ **Programación Orientada a Objetos:**
  - Definición de clases con responsabilidades claras
  - Encapsulación de datos y comportamientos
  - Herencia implícita a través de patrones

✓ **Tipos de Datos:**
  - Tipos básicos: `str`, `int`, `float`, `bool`
  - Tipos compuestos: `List` para almacenar objetos

✓ **Convenciones de Python:**
  - **PascalCase** para nombres de clases: `Producto`, `Cliente`, `Restaurante`
  - **snake_case** para variables, métodos y archivos: `id_producto`, `agregar_cliente()`
  - Anotaciones de tipo: `nombre: str`, `precio: float`, `disponible: bool`

✓ **Métodos Especiales:**
  - `__init__()` para inicialización
  - `__str__()` para representación en string

✓ **Importaciones Modulares:**
  - Importación de clases desde módulos específicos
  - Organización clara en paquetes

✓ **Documentación:**
  - Docstrings descriptivos en clases y métodos
  - Comentarios en secciones principales
  - Identificadores descriptivos y autoexplicativos

## Ejemplo de Salida

El programa crea 4 productos y 4 clientes, luego:
1. Muestra el listado completo de productos
2. Muestra el listado completo de clientes
3. Muestra un resumen del restaurante
4. Realiza operaciones adicionales (cambios de estado, búsquedas, eliminaciones)
5. Muestra un resumen final actualizado

## Requisitos Cumplidos

- [x] Estructura modular con carpetas
- [x] Mínimo 2 clases en modelos
- [x] 1 clase en servicios
- [x] Constructores __init__()
- [x] Identificadores descriptivos
- [x] Convenciones de nombres Python
- [x] Tipos de datos básicos (str, int, float, bool)
- [x] Listas como tipo compuesto
- [x] Anotaciones de tipo
- [x] Métodos para gestionar información
- [x] Método __str__()
- [x] Importaciones correctas
- [x] Mínimo 2 objetos por modelo
- [x] Información mostrada en consola organizada
- [x] Comentarios explicativos

## Notas de Implementación

- No se copió literalmente del ejemplo docente de biblioteca
- Se implementó en contexto de restaurante con entidades relevantes
- Se evitaron nombres genéricos (x, dato, objeto, clase1, etc.)
- No se incluyen interfaces gráficas ni menús complejos
- El código es autodocumentado y fácil de entender
