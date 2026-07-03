# Sistema de Gestión de Productos - Restaurante

**Estudiante:** Nicole Micaela Cedeño Vizhñay  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 6  
**Fecha:** Julio 2026

---

## 📋 Descripción del Sistema

El **Sistema de Gestión de Productos para Restaurante** es una aplicación desarrollada en Python que implementa los principios fundamentales de la Programación Orientada a Objetos (POO). Este sistema permite administrar productos disponibles en un restaurante, distinguiendo entre platillos y bebidas, aplicando herencia, encapsulación y polimorfismo para demostrar una arquitectura modular y escalable.

El proyecto toma como referencia metodológica el sistema de biblioteca presentado en la Semana 6 por el docente, adaptando sus principios a un contexto diferente (restaurante) sin copiar literalmente el código.

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase padre
│   ├── platillo.py          # Clase hija (herencia)
│   └── bebida.py            # Clase hija (herencia)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase de servicio
└── main.py                  # Punto de entrada
```

### Responsabilidad de cada componente:

- **`modelos/producto.py`**: Contiene la clase padre `Producto` con atributos comunes (nombre, precio, disponibilidad) y métodos de acceso controlado.

- **`modelos/platillo.py`**: Implementa la clase `Platillo` que hereda de `Producto`, añadiendo atributos específicos como tipo de platillo y tiempo de preparación.

- **`modelos/bebida.py`**: Implementa la clase `Bebida` que hereda de `Producto`, añadiendo atributos específicos como tipo de bebida y volumen en mililitros.

- **`servicios/restaurante.py`**: Define la clase `Restaurante` que actúa como servicio para administrar la lista de productos, con métodos para agregar, eliminar, buscar y mostrar productos.

- **`main.py`**: Archivo principal que demuestra el funcionamiento del sistema creando objetos, agregándolos al restaurante y mostrando los resultados en consola.

---

## 🔗 Relación de Herencia Aplicada

El proyecto implementa una **jerarquía de herencia de un nivel** siguiendo el patrón de especialización:

```
Producto (Clase Padre)
├── Platillo (Clase Hija)
└── Bebida (Clase Hija)
```

### Explicación de la herencia:

- **Producto** es la clase padre que encapsula los atributos comunes a todos los productos del restaurante:
  - `__nombre`: Nombre del producto
  - `__precio`: Precio del producto
  - `_disponibilidad`: Disponibilidad del producto

- **Platillo** es una clase hija que hereda de `Producto` y añade atributos específicos:
  - `tipo_platillo`: Tipo de comida (Entrada, Principal, Postre)
  - `tiempo_preparacion`: Tiempo en minutos que tarda la preparación

- **Bebida** es otra clase hija que hereda de `Producto` y añade atributos específicos:
  - `tipo_bebida`: Tipo de bebida (Refrescante, Alcohólica, Caliente)
  - `volumen_ml`: Volumen de la bebida en mililitros

### Uso de `super()`:

Ambas clases hijas utilizan `super().__init__()` en sus constructores para reutilizar la lógica de inicialización de la clase padre, evitando duplicación de código:

```python
class Platillo(Producto):
    def __init__(self, nombre, precio, tipo_platillo, tiempo_preparacion, disponibilidad=True):
        super().__init__(nombre, precio, disponibilidad)  # Reutiliza constructor padre
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion
```

---

## 🔐 Encapsulación: Atributo Protegido

El proyecto implementa **encapsulación en el atributo de precio** mediante los siguientes mecanismos:

### Atributo Privado:
- `__precio`: Declarado como privado (con doble guion) en la clase `Producto` para prevenir acceso directo desde fuera de la clase.

### Validación y Control:

Se implementó el método `_validar_precio()` que garantiza que:
- El precio sea mayor que cero
- Se lance una excepción `ValueError` si el precio es inválido

```python
def _validar_precio(self, precio):
    if precio <= 0:
        raise ValueError("El precio debe ser mayor a cero.")
    return precio
```

### Métodos de Acceso:

- **`obtener_precio()`**: Permite leer el precio del producto de forma segura
- **`cambiar_precio(nuevo_precio)`**: Permite modificar el precio solo si cumple con la validación

### Ejemplo de uso:
```python
platillo = Platillo("Filete", 18.50, "Principal", 15)
print(platillo.obtener_precio())  # Lectura segura: 18.50
platillo.cambiar_precio(25.00)     # Modificación validada
platillo.cambiar_precio(-5.00)     # Genera ValueError
```

Esta encapsulación protege la integridad de los datos y asegura que el precio siempre sea un valor válido.

---

## 🎭 Polimorfismo: Método `mostrar_informacion()`

El polimorfismo se demuestra mediante el **método `mostrar_informacion()`** que es:

1. **Definido en la clase padre `Producto`** con una implementación básica
2. **Sobrescrito en las clases hijas** con implementaciones especializadas

### Implementación en Producto (Clase Padre):
```python
def mostrar_informacion(self):
    """Muestra la información básica del producto."""
    estado = "Disponible" if self._disponibilidad else "No disponible"
    print(f"Nombre: {self.__nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}")
```

### Sobrescritura en Platillo:
```python
def mostrar_informacion(self):
    """Muestra información específica del platillo."""
    print(f"[PLATILLO]")
    print(f"  Nombre: {self.obtener_nombre()}")
    print(f"  Tipo: {self.tipo_platillo}")
    print(f"  Tiempo de preparación: {self.tiempo_preparacion} minutos")
    print(f"  Precio: ${self.obtener_precio():.2f}")
```

### Sobrescritura en Bebida:
```python
def mostrar_informacion(self):
    """Muestra información específica de la bebida."""
    print(f"[BEBIDA]")
    print(f"  Nombre: {self.obtener_nombre()}")
    print(f"  Tipo: {self.tipo_bebida}")
    print(f"  Volumen: {self.volumen_ml} ml")
    print(f"  Precio: ${self.obtener_precio():.2f}")
```

### Demostración de Polimorfismo:
En `main.py`, el polimorfismo se manifiesta al iterar sobre una lista heterogénea de productos y llamar a `mostrar_informacion()` en cada uno, obteniendo diferentes salidas según el tipo de objeto:

```python
for producto in self.productos:
    producto.mostrar_informacion()  # Cada tipo muestra su información de forma diferente
```

**Resultado:** Un único método `mostrar_informacion()` se comporta de manera diferente según si el objeto es un `Platillo` o una `Bebida`, demostrando el verdadero concepto de polimorfismo ("muchas formas").

---

## 📚 Reflexión: Importancia de POO en Proyectos Python Modulares

### ¿Por qué es importante aplicar POO en Python?

La Programación Orientada a Objetos es fundamental en Python moderno por las siguientes razones:

#### 1. **Modularidad y Organización**
La POO permite estructurar el código en módulos lógicos (clases y paquetes) que son fáciles de entender y mantener. En este proyecto, separar `Producto`, `Platillo` y `Bebida` en archivos diferentes facilita la navegación y el mantenimiento del código.

#### 2. **Reutilización de Código**
La herencia permite reutilizar código común sin duplicación. En lugar de escribir los atributos `nombre`, `precio` y métodos de validación dos veces (una para Platillo y otra para Bebida), se escriben una sola vez en la clase padre y se heredan.

#### 3. **Encapsulación y Protección de Datos**
Al encapsular atributos como `__precio`, protegemos la integridad de los datos. Las validaciones garantizan que solo valores válidos se asignen, evitando errores en tiempo de ejecución y mejorando la robustez del sistema.

#### 4. **Polimorfismo y Flexibilidad**
El polimorfismo permite que el código cliente (como la clase `Restaurante`) trabaje con una abstracción común (`Producto`) sin necesidad de conocer los detalles específicos de cada subclase. Esto hace el código más flexible y extensible.

#### 5. **Escalabilidad**
Si en el futuro se necesita agregar nuevos tipos de productos (Postres, Entrantes especiales), basta con crear nuevas clases que hereden de `Producto`. El código existente no requiere cambios significativos.

#### 6. **Mantenibilidad**
Los cambios en la lógica común solo necesitan hacerse una vez en la clase padre. Esto reduce la probabilidad de errores y facilita el mantenimiento del proyecto a largo plazo.

### Aplicación en este proyecto:

Este sistema demuestra cómo la POO transforma un conjunto de datos simples en una arquitectura robusta y escalable. Sin POO, el código sería procedural, con funciones dispersas y variables globales compartidas. Con POO, tenemos un sistema modular donde cada clase tiene una responsabilidad clara, los datos están protegidos y el comportamiento está bien definido.

La separación en paquetes (`modelos` y `servicios`) refleja la práctica profesional de organización de código, permitiendo que múltiples desarrolladores trabajen en paralelo y que el sistema escale sin problemas.

---

## 🚀 Cómo Ejecutar el Programa

### Requisitos:
- Python 3.6 o superior

### Instrucciones:

1. Navegar al directorio del proyecto:
   ```bash
   cd restaurante_app
   ```

2. Ejecutar el programa principal:
   ```bash
   python main.py
   ```

### Salida esperada:
El programa mostrará:
- Confirmación de agregación de productos
- Menú completo con información de cada producto (demostrando polimorfismo)
- Ejemplos de encapsulación (cambio de precio con validación)
- Cambios de disponibilidad
- Listado de productos disponibles
- Búsqueda de productos
- Información de métodos específicos de clases hijas
- Resumen final

---

## 📝 Conclusión

Este proyecto demuestra la aplicación efectiva de los cuatro pilares de la Programación Orientada a Objetos:

1. ✅ **Abstracción**: Representación simplificada de productos del restaurante
2. ✅ **Encapsulación**: Protección del atributo `__precio` con validación
3. ✅ **Herencia**: Relación jerárquica entre Producto, Platillo y Bebida
4. ✅ **Polimorfismo**: Método `mostrar_informacion()` con comportamiento específico por tipo

La arquitectura modular propuesta facilita el mantenimiento, escalabilidad y comprensión del código, sentando las bases para sistemas más complejos en proyectos Python profesionales.

---

**Semana 6 - Programación Orientada a Objetos**  
Nicole Micaela Cedeño Vizhñay
