# Introducción a la Programación Orientada a Objetos (POO)

## 📋 Descripción del Proyecto

Este proyecto educativo presenta una introducción completa a los conceptos fundamentales de **Programación Orientada a Objetos (POO)** en Python. El proyecto está organizando en semanas progresivas, donde cada semana introduce nuevos conceptos y ejemplos prácticos.

**Curso:** 2626 - Programación Orientada a Objetos  
**Centro:** CEDE O NICOLE  
**Nivel:** Iniciante

---

## 📁 Estructura del Proyecto

```
2626-POO-CEDE-O-NICOLE/
│
├── PARCIAL 1/
│   ├── SEMANA 2/
│   │   ├── TAREA SEMANA 2.md          # Documentación detallada de la clase CuentaBancaria
│   │   └── TAREA SEMANA 2.py          # Implementación de la clase CuentaBancaria
│   │
│   └── SEMANA 3/
│       ├── programación_poo/
│       │   ├── main.py                # Archivo principal - demostración de POO
│       │   └── mascota.py             # Clase Mascota con métodos y atributos
│       │
│       └── programación_tradicional/
│           └── tradicional.py         # Comparación: programación tradicional (sin POO)
│
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py                # Paquete de modelos
│   │   ├── producto.py                # Clase Producto
│   │   └── cliente.py                 # Clase Cliente
│   ├── servicios/
│   │   ├── __init__.py                # Paquete de servicios
│   │   └── restaurante.py             # Clase Restaurante
│   └── main.py                        # Programa principal
│
└── README.md                          # Este archivo

```

---

## 🍽️ PROYECTO: Sistema de Gestión de Restaurante

### 📌 Información del Estudiante
**Nombre:** Nicole Valentina Molina Corredor  
**Curso:** 2626 - Programación Orientada a Objetos  
**Centro:** CEDE O NICOLE

### 📝 Descripción del Sistema
Sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos. El sistema demuestra la aplicación de conceptos fundamentales como clases, objetos, tipos de datos básicos, listas, métodos especiales e importaciones modulares. El proyecto no replica el ejemplo docente de biblioteca, sino que implementa un contexto diferente con entidades relevantes al dominio de restaurantes.

**Objetivo:** Demostrar comprensión de POO mediante la implementación de un sistema modular que gestiona productos (platos, bebidas) y clientes registrados.

### 🏗️ Estructura del Proyecto Restaurante

```
restaurante_app/
├── modelos/
│   ├── __init__.py              # Paquete de modelos
│   ├── producto.py              # Clase Producto (2.15 KB)
│   └── cliente.py               # Clase Cliente (2.23 KB)
├── servicios/
│   ├── __init__.py              # Paquete de servicios
│   └── restaurante.py           # Clase Restaurante (4.08 KB)
├── main.py                      # Programa principal (4.65 KB)
└── README.md                    # Documentación interna
```

#### **Responsabilidad de cada componente:**

1. **modelos/producto.py - Clase Producto**
   - Representa un plato, bebida o artículo disponible
   - Encapsula datos y comportamiento de productos

2. **modelos/cliente.py - Clase Cliente**
   - Representa una persona registrada en el sistema
   - Gestiona información de contacto y estado de membresía

3. **servicios/restaurante.py - Clase Restaurante**
   - Administra colecciones de productos y clientes
   - Actúa como servicio central del sistema

4. **main.py**
   - Punto de entrada del programa
   - Demuestra creación de objetos y operaciones del sistema

### 📊 Tipos de Datos Utilizados en las Clases

#### **Clase Producto**
```python
id_producto: int              # Identificador único del producto
nombre: str                   # Nombre descriptivo del producto
descripcion: str              # Descripción detallada del producto
precio: float                 # Precio en pesos (con decimales)
disponible: bool              # Estado de disponibilidad (True/False)
```

#### **Clase Cliente**
```python
id_cliente: int               # Identificador único del cliente
nombre: str                   # Nombre completo del cliente
email: str                    # Correo electrónico
telefono: str                 # Número de teléfono
miembro_premium: bool         # Estado de membresía premium (True/False)
```

#### **Clase Restaurante**
```python
nombre: str                   # Nombre del restaurante
productos: List[Producto]     # Lista de productos disponibles
clientes: List[Cliente]       # Lista de clientes registrados
```

### 🎯 Métodos Implementados por Clase

**Clase Producto:**
- `__init__()` - Constructor con inicialización de atributos
- `__str__()` - Representación legible del producto
- `cambiar_disponibilidad(estado: bool)` - Actualiza disponibilidad
- `obtener_informacion_corta()` - Retorna resumen del producto

**Clase Cliente:**
- `__init__()` - Constructor con inicialización de atributos
- `__str__()` - Representación legible del cliente
- `cambiar_estado_premium(es_premium: bool)` - Modifica membresía
- `obtener_informacion_corta()` - Retorna resumen del cliente

**Clase Restaurante:**
- `agregar_producto()` - Agrega producto a la lista
- `agregar_cliente()` - Agrega cliente a la lista
- `eliminar_producto()` - Elimina producto por ID
- `buscar_cliente()` - Busca cliente por ID
- `listar_productos()` - Muestra todos los productos
- `listar_clientes()` - Muestra todos los clientes
- `obtener_resumen()` - Muestra estadísticas del restaurante

### ▶️ Cómo Ejecutar el Sistema

```bash
cd restaurante_app
python main.py
```

**Salida del programa:**
- Listado de 4 productos registrados con detalles
- Listado de 4 clientes registrados con información
- Resumen del restaurante (totales y estadísticas)
- Operaciones adicionales (cambios de estado, búsquedas, eliminaciones)

### 💡 Reflexión: Identificadores Descriptivos, Tipos de Datos y Listas en Python Modular

#### **Importancia de Identificadores Descriptivos**

Los identificadores descriptivos son fundamentales en la programación orientada a objetos moderna. Al utilizar nombres claros y significativos como `id_producto`, `cambiar_disponibilidad()` y `miembro_premium` en lugar de alternativas genéricas como `x`, `func1` o `flag`, se logra:

- **Autoexplicación del código:** Otros desarrolladores (e incluso uno mismo meses después) pueden entender el propósito sin necesidad de documentación exhaustiva
- **Mantenibilidad:** Cambios y depuración son más eficientes cuando el código es legible
- **Reducción de errores:** Nombres descriptivos previenen confusiones sobre qué representa cada variable
- **Profesionalismo:** El código sigue convenciones de la industria (snake_case para variables/métodos, PascalCase para clases)

En este proyecto se aplicaron identificadores descriptivos sistemáticamente: `restaurante` (nombre principal), `productos` (lista clara), `agregar_producto()` (acción descriptiva), evitando completamente nombres genéricos.

#### **Importancia de Tipos de Datos Adecuados**

La selección apropiada de tipos de datos es esencial para:

- **Integridad de datos:** Usar `float` para `precio` garantiza precisión decimal, mientras que `int` para IDs asegura valores enteros únicos
- **Validación automática:** El tipo `bool` para `disponible` y `miembro_premium` restringe los valores a True/False, evitando estados inválidos
- **Legibilidad:** Anotaciones de tipo como `precio: float` hacen explícita la naturaleza de cada atributo
- **Compatibilidad con herramientas:** Lenguajes tipados facilitan detección de errores antes de la ejecución

Este proyecto demuestra la cuidadosa selección de tipos: `str` para datos textuales (nombres, descripciones), `int` para contadores identificadores, `float` para cálculos monetarios, `bool` para estados binarios.

#### **Importancia de Listas en Proyectos Modulares**

Las listas son estructuras fundamentales que permiten:

- **Gestión de colecciones:** `self.productos: List[Producto]` almacena múltiples instancias de manera ordenada y accesible
- **Modularidad:** El servicio central (Restaurante) puede operar sobre colecciones sin acoplamiento a fuentes externas
- **Escalabilidad:** Operaciones como `listar_productos()` o `buscar_cliente()` funcionan independientemente del tamaño de la colección
- **Iteración eficiente:** Las listas permiten procesar múltiples objetos con `for` loops elegantes
- **Persistencia del estado:** Las listas mantienen estado entre operaciones en el programa

En la clase Restaurante, las listas tipadas `List[Producto]` y `List[Cliente]` demuestran que las colecciones pueden almacenar objetos específicos, no solo valores primitivos, permitiendo arquitecturas modulares cohesivas.

#### **Integración en Arquitectura Modular**

La modularización en carpetas (modelos/, servicios/) con importaciones correctas (`from modelos.producto import Producto`) es posible gracias a:

- Identificadores descriptivos que aclaran qué módulo contiene qué
- Tipos adecuados que definen contratos claros entre módulos
- Listas tipadas que comunican qué colecciones maneja cada componente

Este proyecto demuestra que Python modular exitoso es resultado de decisiones cuidadosas en nomenclatura, tipos de datos y estructuras de colecciones.

---

## 🎯 Contenido por Semana

### Semana 2: Introducción a las Clases y Objetos

#### Archivo: `PARCIAL 1/SEMANA 2/TAREA SEMANA 2.py`

**Tema:** Sistema de Gestión de Cuenta Bancaria

**Conceptos enseñados:**
- Definición de clases
- Atributos del objeto (nombre_titular, numero_cuenta, saldo)
- Constructor (`__init__`)
- Métodos de instancia (depositar, retirar, mostrar_saldo)
- Método especial `__str__` para representación en texto
- Uso de `self` en métodos

**Programa Principal:**
```python
# Crear una cuenta bancaria
cuenta = CuentaBancaria("Ana Pérez", "1234567890", 500.0)

# Realizar operaciones
cuenta.depositar(250.0)      # Suma dinero
cuenta.retirar(100.0)        # Retira dinero
cuenta.mostrar_saldo()       # Muestra el saldo actual
```

**Operaciones disponibles:**
- ✅ Depositar dinero (con validación)
- ✅ Retirar dinero (con validación de fondos)
- ✅ Consultar saldo

---

### Semana 3: POO vs Programación Tradicional

#### A) Programación Orientada a Objetos
**Archivo:** `PARCIAL 1/SEMANA 3/programación_poo/`

**Archivos:**
- `mascota.py` - Define la clase Mascota
- `main.py` - Usa la clase Mascota

**Tema:** Sistema de Registro de Mascotas con POO

**Concepto clave:** Las mascotas se representan como objetos con atributos y métodos

**Características:**
- Clase `Mascota` con atributos: nombre, especie, edad
- Método `mostrar_informacion()` - Presenta los datos de la mascota
- Método `hacer_sonido()` - Emite el sonido característico según la especie

**Ejemplo de uso:**
```python
# Instanciar objetos
mascota1 = Mascota("Max", "Perro", 3)
mascota2 = Mascota("Luna", "Gato", 2)

# Usar métodos del objeto
mascota1.mostrar_informacion()
mascota1.hacer_sonido()        # Output: Max (Perro) hace: ¡Guau guau!
```

#### B) Programación Tradicional (Sin POO)
**Archivo:** `PARCIAL 1/SEMANA 3/programación_tradicional/tradicional.py`

**Tema:** Sistema de Registro de Mascotas sin POO

**Concepto clave:** Uso de funciones y diccionarios en lugar de clases

**Características:**
- Funciones para registrar y mostrar información
- Diccionarios para almacenar datos de mascotas
- Bucles para manejar múltiples registros
- Permite comparar el enfoque tradicional con el enfoque POO

**Diferencias principales:**
| Aspecto | POO (Semana 3a) | Tradicional (Semana 3b) |
|--------|---|---|
| Estructura | Clases y objetos | Funciones y diccionarios |
| Datos | Atributos del objeto | Claves del diccionario |
| Comportamiento | Métodos del objeto | Funciones independientes |
| Organización | Encapsulación de datos | Datos fragmentados |

---

## 🚀 Cómo ejecutar los programas

### Requisitos previos
- Python 3.6 o superior
- Terminal o línea de comandos

### Ejecutar Semana 2
```bash
cd "PARCIAL 1/SEMANA 2"
python "TAREA SEMANA 2.py"
```

**Salida esperada:**
```
Cuenta bancaria de Ana Pérez
Número de cuenta: 1234567890
Saldo: $500.00
Depósito exitoso: $250.00
Retiro exitoso: $100.00
Saldo actual de Ana Pérez: $650.00
```

### Ejecutar Semana 3 - POO
```bash
cd "PARCIAL 1/SEMANA 3/programación_poo"
python main.py
```

**Salida esperada:**
```
==================================================
SISTEMA DE REGISTRO DE MASCOTAS - POO
==================================================

MAscota 1:
==================================================
INFORMACIÓN DE LA MASCOTA
==================================================
Nombre:   Max
Especie:  Perro
Edad:     3 años
...
```

### Ejecutar Semana 3 - Programación Tradicional
```bash
cd "PARCIAL 1/SEMANA 3/programación_tradicional"
python tradicional.py
```

---

## 📚 Conceptos Clave de POO

### 1. **Clase**
Una plantilla que define la estructura y comportamiento de los objetos.

### 2. **Objeto**
Una instancia de una clase - una entidad específica que existe en la memoria.

### 3. **Atributos**
Datos o propiedades que tiene un objeto (variables miembro).

### 4. **Métodos**
Funciones que definen el comportamiento de un objeto.

### 5. **Constructor (`__init__`)**
Método especial que se ejecuta al crear un objeto nuevo.

### 6. **`self`**
Referencia al objeto actual dentro de sus métodos.

### 7. **Métodos Especiales**
- `__str__()` - Define cómo se muestra el objeto al imprimirse
- `__init__()` - Constructor del objeto

---

## 💡 Ventajas de la Programación Orientada a Objetos

✅ **Modularidad** - Código organizado y reutilizable  
✅ **Encapsulación** - Datos y métodos agrupados cohesivamente  
✅ **Mantenibilidad** - Código más fácil de entender y modificar  
✅ **Escalabilidad** - Facilita agregar nuevas funcionalidades  
✅ **Reutilización** - Las clases pueden usarse en múltiples proyectos

---

## 🔍 Comparación: POO vs Tradicional

### Ejemplo: Mascota "Max"

**Enfoque POO:**
```python
mascota = Mascota("Max", "Perro", 3)
mascota.hacer_sonido()  # Métodos integrados en el objeto
```

**Enfoque Tradicional:**
```python
mascota = {"nombre": "Max", "especie": "Perro", "edad": 3}
# Necesitas funciones separadas para realizar acciones
```

---

## 📝 Notas de Estudio

- Cada semana se agregan comentarios en el código para facilitar el aprendizaje
- Los programas incluyen validación de datos y manejo de errores básicos
- Los ejemplos prácticos permiten entender los conceptos de forma inmediata
- Se proporciona documentación tanto de código como de base de datos

---

## 👨‍🎓 Objetivo Educativo

Al completar este proyecto comprenderás:
1. ✅ Qué es una clase y para qué sirve
2. ✅ Cómo crear e instanciar objetos
3. ✅ La diferencia entre atributos y métodos
4. ✅ El propósito del constructor
5. ✅ Las ventajas de POO sobre programación tradicional
6. ✅ Cómo encapsular datos y comportamiento

---

## 📞 Soporte

Para dudas o sugerencias sobre este proyecto, revisa:
- Los comentarios incluidos en cada archivo Python
- La documentación en `TAREA SEMANA 2.md` (Semana 2)
- Los ejemplos prácticos de ejecución

---

## 📄 Licencia

Proyecto educativo. Disponible para uso académico.

---

**Última actualización:** 2026  
**Estado:** Completado para PARCIAL 1 (Semanas 2-3)
