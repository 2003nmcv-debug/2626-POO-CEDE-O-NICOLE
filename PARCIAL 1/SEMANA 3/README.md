# 📚 SEMANA 3: Programación Orientada a Objetos vs Programación Tradicional

## 🎯 Objetivo General

Comprender y comparar dos paradigmas fundamentales de programación:
- **Programación Orientada a Objetos (POO)**: Enfoque moderno basado en clases y objetos
- **Programación Tradicional (Procedural)**: Enfoque clásico basado en funciones

---

## 📁 Estructura del Proyecto

```
SEMANA 3/
├── programación_poo/                 # Enfoque con clases y objetos
│   ├── mascota.py                   # Define la clase Mascota
│   ├── main.py                      # Programa principal con POO
│   └── __pycache__/                 # Archivos compilados automáticos
├── programación_tradicional/        # Enfoque con funciones y diccionarios
│   └── tradicional.py               # Programa sin usar clases
└── README.md                        # Este archivo
```

---

## 🏗️ PROGRAMACIÓN ORIENTADA A OBJETOS (POO)

### 📂 Ubicación de Archivos
- `programación_poo/mascota.py` - Definición de la clase
- `programación_poo/main.py` - Programa principal

### 🔑 Conceptos Clave Implementados

#### 1️⃣ **La Clase Mascota**

```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
```

**¿Qué es una clase?**
- Plantilla/molde para crear objetos
- Agrupa datos (atributos) con funcionalidad (métodos)
- Define el "tipo" de objeto que vamos a crear

**¿Qué es un objeto?**
- Un ejemplar específico de una clase
- Tiene sus propios atributos con valores únicos
- Puede ejecutar métodos de la clase

#### 2️⃣ **Método Constructor: `__init__`**

```python
def __init__(self, nombre, especie, edad):
    """Se ejecuta automáticamente al crear un objeto"""
    self.nombre = nombre
    self.especie = especie
    self.edad = edad
```

**Función:**
- Se ejecuta automáticamente cuando se crea un nuevo objeto
- Inicializa los ATRIBUTOS de la instancia
- Cada objeto obtiene sus propios valores

**Parámetro `self`:**
- Referencia al objeto actual
- Permite acceder a atributos y métodos
- NO se incluye al llamar el constructor

#### 3️⃣ **Métodos de Instancia**

**Método: `mostrar_informacion()`**
```python
def mostrar_informacion(self):
    print(f"Nombre: {self.nombre}")
    print(f"Especie: {self.especie}")
    print(f"Edad: {self.edad} años")
```

**Método: `hacer_sonido()`**
```python
def hacer_sonido(self):
    sonidos = {"perro": "¡Guau!", "gato": "¡Miau!"}
    sonido = sonidos.get(self.especie.lower(), "Sonido desconocido")
    print(f"{self.nombre} hace: {sonido}")
```

**Características:**
- Tienen acceso a `self` para usar los atributos
- Encapsulan lógica relacionada con objetos
- Cada objeto ejecuta el método CON SUS DATOS

#### 4️⃣ **Creación de Objetos en main.py**

```python
# Crear tres objetos independientes de la clase Mascota
mascota1 = Mascota("Max", "Perro", 3)
mascota2 = Mascota("Luna", "Gato", 2)
mascota3 = Mascota("Tweety", "Pájaro", 1)

# Cada objeto es COMPLETAMENTE INDEPENDIENTE
# Cambios en mascota1 NO afectan mascota2

# Llamar métodos
mascota1.mostrar_informacion()  # Usa datos de mascota1
mascota2.mostrar_informacion()  # Usa datos de mascota2
```

#### 5️⃣ **Procesamiento de Colecciones de Objetos**

```python
# Agrupar múltiples objetos en una lista
mascotas = [mascota1, mascota2, mascota3]

# Iterar sobre los objetos
for i, mascota in enumerate(mascotas, 1):
    print(f"{i}. {mascota.nombre} - {mascota.especie}")
```

### ✅ Ventajas de la POO

| Ventaja | Explicación |
|---------|------------|
| **Encapsulación** | Datos y métodos juntos en una clase |
| **Reutilización** | Una clase se puede instanciar múltiples veces |
| **Mantenibilidad** | Cambios centralizados en la clase |
| **Escalabilidad** | Fácil agregar nuevas clases y funcionalidad |
| **Organización** | Código más legible y estructurado |
| **Independencia** | Cada objeto es independiente |

### 🚀 Cómo Ejecutar POO

```bash
cd programación_poo
python main.py
```

**Salida esperada:**
```
==================================================
SISTEMA DE REGISTRO DE MASCOTAS - POO
==================================================

>>> CREANDO OBJETOS (INSTANCIAS)...
   ✓ Mascota 1 creada: Max (Perro)
   ✓ Mascota 2 creada: Luna (Gato)
   ✓ Mascota 3 creada: Tweety (Pájaro)

...información de cada mascota...

...resumen final...
```

---

## 🔄 PROGRAMACIÓN TRADICIONAL (PROCEDURAL)

### 📂 Ubicación de Archivos
- `programación_tradicional/tradicional.py` - Todo en un archivo

### 🔑 Conceptos Clave Implementados

#### 1️⃣ **Usando Diccionarios para Datos**

```python
# En lugar de crear una clase, usamos un diccionario
mascota = {
    "nombre": "Max",
    "especie": "Perro",
    "edad": 3,
    "color": "Negro",
    "peso": 25
}

# Acceso a datos con CLAVES (strings)
print(mascota['nombre'])  # Imprime: Max
print(mascota['especie']) # Imprime: Perro
```

**Diferencia con Objetos:**
- Diccionario: `mascota['nombre']` (clave como string)
- Objeto: `mascota.nombre` (atributo directo)

#### 2️⃣ **Funciones Independientes**

**Función: `registrar_mascota()`**
```python
def registrar_mascota():
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = input("Edad: ")
    
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }
    return mascota
```

**Características:**
- Datos separados de funciones
- Cada función hace UNA cosa
- Requiere pasar datos explícitamente

**Función: `mostrar_mascota(mascota)`**
```python
def mostrar_mascota(mascota):
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    # Acceso a diccionario con claves
```

**Función: `programa_principal()`**
```python
def programa_principal():
    continuar = True
    mascotas = []  # Lista de diccionarios
    
    while continuar:
        mascota = registrar_mascota()
        mascotas.append(mascota)
        mostrar_mascota(mascota)
        
        respuesta = input("¿Registrar otra? ")
        if respuesta != "si":
            continuar = False
```

#### 3️⃣ **Control de Flujo con Variables**

```python
# Variable de control
continuar = True

# Bucle while
while continuar:
    # ... código ...
    
    # Cambiar variable
    if condicion:
        continuar = False  # Sale del bucle
```

#### 4️⃣ **Procesamiento de Listas de Diccionarios**

```python
mascotas = []  # Lista vacía

# Agregar diccionarios
mascota1 = {"nombre": "Max", "especie": "Perro"}
mascota2 = {"nombre": "Luna", "especie": "Gato"}
mascotas.append(mascota1)
mascotas.append(mascota2)

# Iterar
for i, mascota in enumerate(mascotas, 1):
    print(f"{i}. {mascota['nombre']}")
```

### ⚠️ Limitaciones de Programación Tradicional

| Limitación | Problema | Ejemplo |
|-----------|----------|---------|
| **Separación datos/lógica** | Difícil ver relación entre datos y funciones | `mascota['nombre']` vs `mascota.nombre` |
| **Repetición de código** | Funciones similares duplicadas | Dos funciones para mostrar diferentes tipos de datos |
| **Difícil mantenimiento** | Cambios dispersos en múltiples lugares | Modificar formato: cambiar múltiples funciones |
| **Escalabilidad limitada** | No práctico para proyectos grandes | Cientos de funciones sin organización |
| **Sin protección de datos** | Cualquiera puede modificar el diccionario | `mascota['edad'] = "inválido"` no hay validación |

### 🚀 Cómo Ejecutar Programación Tradicional

```bash
cd programación_tradicional
python tradicional.py
```

**Proceso Interactivo:**
```
==================================================
BIENVENIDO A LA TIENDA DE MASCOTAS
==================================================

Por favor, ingrese los datos de su mascota:

Nombre de la mascota: Max
Especie de la mascota: perro
Edad de la mascota: 3
Color de la mascota: Negro
Peso de la mascota: 25

==================================================
INFORMACIÓN DE LA MASCOTA REGISTRADA
==================================================

Nombre:   Max
Especie:  perro
Edad:     3 años
Color:    Negro
Peso:     25 kg

¿Desea registrar otra mascota? (si/no): no

¡Gracias por usar el sistema!
```

---

## 🔀 Comparación Detallada: POO vs Tradicional

### 📊 Tabla Comparativa

| Aspecto | POO | Tradicional |
|--------|-----|------------|
| **Organización** | Clases agrupan datos y métodos | Funciones y datos separados |
| **Acceso a datos** | `mascota.nombre` | `mascota['nombre']` |
| **Crear objeto** | `mascota = Mascota("Max", "Perro", 3)` | `mascota = {"nombre": "Max", ...}` |
| **Llamar método** | `mascota.mostrar_info()` | `mostrar_mascota(mascota)` |
| **Reutilización** | Instanciar clase múltiples veces | Crear múltiples diccionarios |
| **Lógica** | Encapsulada en métodos | Distribuida en funciones |
| **Escalabilidad** | ⭐⭐⭐⭐⭐ Excelente | ⭐⭐ Limitada |
| **Curva aprendizaje** | ⭐⭐⭐ Media | ⭐⭐ Baja |
| **Para principiantes** | ⭐⭐⭐ Bueno | ⭐⭐⭐⭐ Mejor |
| **Para proyectos grandes** | ⭐⭐⭐⭐⭐ Ideal | ⭐ Difícil |

### 💡 Comparación de Código

#### Creación y Uso

**POO:**
```python
# Crear objeto
mascota = Mascota("Max", "Perro", 3)

# Usar métodos
mascota.mostrar_informacion()
mascota.hacer_sonido()
```

**Tradicional:**
```python
# Crear diccionario
mascota = {
    "nombre": "Max",
    "especie": "Perro",
    "edad": 3
}

# Llamar funciones
mostrar_mascota(mascota)
hacer_sonido(mascota)
```

#### Extensibilidad - Agregar Método Nuevo

**POO - Muy fácil:**
```python
class Mascota:
    # ...código existente...
    
    def calcular_edad_humana(self):
        """Nuevo método"""
        return self.edad * 7
```

**Tradicional - Más complejo:**
```python
# Crear nueva función que reciba el diccionario
def calcular_edad_humana(mascota):
    return int(mascota['edad']) * 7
```

---

## 🎓 Conceptos Fundamentales de POO

### 1. **Encapsulación**
- Agrupar datos (atributos) con funcionalidad (métodos)
- La clase `Mascota` encapsula todo lo relacionado con una mascota
- Cambios internos no afectan código externo

### 2. **Abstracción**
- Modelo simplificado del mundo real
- No necesita todos los detalles de una mascota real
- Solo los necesarios para el problema

### 3. **Modularidad**
- Código organizado en unidades independientes
- Cada clase tiene responsabilidad clara
- Fácil de entender y mantener

### 4. **Reutilización**
- Una clase puede usarse múltiples veces
- Instanciar objetos con diferentes valores
- Reduce duplicación de código

### 5. **Mantenibilidad**
- Cambios centralizados en la clase
- Una modificación afecta a todos los objetos
- Código más fácil de actualizar

---

## 📋 Estructura de Archivos Detallada

### `programación_poo/mascota.py`
```python
"""Módulo que define la clase Mascota"""

class Mascota:
    # Constructor
    def __init__(self, nombre, especie, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    # Métodos
    def mostrar_informacion(self):
        # Lógica de presentación
        pass
    
    def hacer_sonido(self):
        # Lógica de comportamiento
        pass
```

**Responsabilidades:**
- Define la estructura de una mascota
- Centraliza lógica relacionada
- Proporciona interfaz clara

### `programación_poo/main.py`
```python
"""Programa principal - Uso de la clase"""

from mascota import Mascota  # Importar clase

def main():
    # Crear objetos
    mascota1 = Mascota("Max", "Perro", 3)
    mascota2 = Mascota("Luna", "Gato", 2)
    
    # Usar objetos
    mascota1.mostrar_informacion()
    mascota2.hacer_sonido()
    
    # Procesar colección
    mascotas = [mascota1, mascota2]
    for mascota in mascotas:
        print(mascota.nombre)

if __name__ == "__main__":
    main()
```

**Responsabilidades:**
- Punto de entrada del programa
- Crear instancias de clases
- Coordinar ejecución

### `programación_tradicional/tradicional.py`
```python
"""Programa completo en enfoque procedural"""

def registrar_mascota():
    # Solicitar datos
    # Retornar diccionario
    pass

def mostrar_mascota(mascota):
    # Recibir diccionario
    # Mostrar información
    pass

def programa_principal():
    # Inicializar variables
    # Bucle principal
    # Procesar datos
    pass

if __name__ == "__main__":
    programa_principal()
```

**Responsabilidades:**
- Funciones independientes para cada tarea
- Paso explícito de datos
- Control de flujo centralizado

---

## 🎯 Casos de Uso Recomendados

### ✅ Usar POO Cuando:
- Proyecto grande o complejo
- Múltiples tipos de entidades (Mascota, Dueño, Clínica)
- Expansión futura probable
- Equipo de múltiples desarrolladores
- Necesidad de reutilización de código
- Proyecto a largo plazo

### ✅ Usar Programación Tradicional Cuando:
- Scripts simples y rápidos
- Lógica lineal sin repetición
- Procesamiento de datos simple
- Aprendizaje de conceptos básicos
- Prototipado rápido
- Proyecto único sin mantenimiento

---

## 💻 Conceptos Python Importantes

### 1. **Módulos e Importación**
```python
# Importar clase de otro módulo
from mascota import Mascota

# Usar la clase
mi_mascota = Mascota("Max", "Perro", 3)
```

### 2. **Punto de Entrada Estándar**
```python
if __name__ == "__main__":
    # Código solo se ejecuta si el archivo es principal
    # NO se ejecuta si es importado como módulo
    main()
```

**Beneficio:**
- Permite reutilizar código en otros programas
- Estructura profesional y estándar

### 3. **Métodos Especiales en Python**
```python
# __init__: Constructor, se ejecuta al crear objeto
def __init__(self, parametros):
    # Inicializar atributos
    pass

# Parámetro self: referencia al objeto actual
def metodo(self):
    self.atributo  # Acceder a atributo
```

### 4. **Diccionarios**
```python
diccionario = {
    "clave1": valor1,
    "clave2": valor2
}

# Acceso
diccionario["clave1"]        # Acceso directo
diccionario.get("clave1")    # Con valor por defecto

# Iteración
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
```

### 5. **Listas y Enumerate**
```python
lista = [1, 2, 3, 4]

# Iterate con índice
for i, elemento in enumerate(lista, 1):  # 1 = inicio en 1, no en 0
    print(f"{i}: {elemento}")
    
# Resultado:
# 1: 1
# 2: 2
# 3: 3
# 4: 4
```

---

## 🏆 Resumen de Aprendizajes

### Semana 3 - Lo que aprendimos:

✅ **Conceptos de POO:**
- Clases y objetos
- Atributos de instancia
- Métodos y `self`
- Constructor `__init__`
- Instanciación

✅ **Conceptos de Programación Tradicional:**
- Funciones independientes
- Diccionarios para datos
- Paso explícito de parámetros
- Control de flujo con variables

✅ **Comparación:**
- Diferencias fundamentales
- Ventajas y desventajas
- Casos de uso adecuados
- Escalabilidad

✅ **Python:**
- Módulos e importación
- Punto de entrada `if __name__`
- Estructuras de datos
- Buenas prácticas

---

## 📚 Recursos Adicionales

- **Python Oficial:** https://www.python.org/
- **Documentación Python:** https://docs.python.org/3/
- **PEP 8 - Guía de estilo:** https://www.python.org/dev/peps/pep-0008/
- **Real Python - POO:** https://realpython.com/object-oriented-programming-python/

---

## 📝 Notas Importantes

1. **Todo en Python es un Objeto**
   - Números, strings, listas, funciones: todo son objetos
   - Python es un lenguaje orientado a objetos

2. **`self` es Obligatorio**
   - Referencia a la instancia dentro de métodos
   - Se omite al LLAMAR métodos

3. **Atributos vs Métodos**
   - Atributos: datos (nombre, edad)
   - Métodos: funciones (mostrar_info, hacer_sonido)

4. **Independencia de Objetos**
   - Cada instancia es independiente
   - Cambios en uno no afectan otros

5. **Encapsulación es Poder**
   - Agrupar datos con lógica
   - Base para POO avanzada

---

## 🎓 Conclusión

La **Programación Orientada a Objetos** es más poderosa y escalable que la programación procedural, pero ambas tienen su lugar. Para proyectos simples, la programación tradicional es suficiente e incluso preferible por su simplicidad. Para proyectos complejos y a largo plazo, POO es fundamental.

**El mejor programador entiende ambas y elige la herramienta correcta para cada problema.**

---

**Autor:** Semana 3 - POO vs Programación Tradicional  
**Fecha:** 2026  
**Nivel:** Principiante - Intermedio  
**Estado:** ✅ Completo

