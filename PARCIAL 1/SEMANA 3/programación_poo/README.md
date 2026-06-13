# Programación Orientada a Objetos - Sistema de Mascotas

Este archivo documenta la **solución de programación orientada a objetos (POO)** para el registro y visualización de información de mascotas.

## 📌 Descripción

Implementa un sistema de mascotas demostrando todos los conceptos fundamentales de **Programación Orientada a Objetos**:
- ✅ **Clases**: Moldes para crear objetos
- ✅ **Objetos**: Instancias de las clases
- ✅ **Atributos**: Datos del objeto
- ✅ **Métodos**: Comportamiento del objeto
- ✅ **Abstracción**: Ocultamiento de complejidad

## 📁 Estructura del Proyecto

```
programación_poo/
├── mascota.py        # Definición de la clase Mascota
├── main.py           # Programa principal
└── README.md         # Este archivo
```

## 🎯 Objetivo

Demostrar:
1. Definición de una **clase** con atributos y métodos
2. Creación de múltiples **objetos**
3. Acceso a **atributos** de los objetos
4. Ejecución de **métodos**
5. Separación en múltiples archivos

## 🏗️ Arquitectura del Código

### 1. Archivo `mascota.py` - Definición de la Clase

**Define la clase `Mascota`** con todos sus atributos y métodos:

```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        # Atributos
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def mostrar_informacion(self):
        # Método para mostrar información
        
    def hacer_sonido(self):
        # Método para emitir sonido
```

#### Atributos de la Clase:
- **`nombre`** (str): El nombre de la mascota
- **`especie`** (str): Tipo de animal (Perro, Gato, Pájaro, etc.)
- **`edad`** (int): La edad en años

#### Métodos de la Clase:

**`__init__(nombre, especie, edad)`** - Constructor
- Se ejecuta automaticamente al crear una instancia
- Inicializa los atributos con los valores proporcionados
- `self` es la referencia al objeto mismo

**`mostrar_informacion()`** - Método de visualización
- Muestra los datos de la mascota de forma organizada
- Accede a los atributos usando `self.nombre`, `self.especie`, `self.edad`

**`hacer_sonido()`** - Método de comportamiento
- Emite un sonido basado en la especie de la mascota
- Demuestra **abstracción**: encapsula la lógica interna
- Usa un diccionario de sonidos según la especie

### 2. Archivo `main.py` - Programa Principal

**Usa la clase Mascota** para crear y manipular objetos:

```python
from mascota import Mascota

def main():
    # Crear objetos
    mascota1 = Mascota("Firulais", "Perro", 3)
    mascota2 = Mascota("Whiskers", "Gato", 2)
    
    # Usar los objetos
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
```

## 📊 Flujo del Programa

```
Inicio
  ↓
┌─ Crear Objeto 1 ──────────────────┐
│ mascota1 = Mascota(...)           │
│ Llama a __init__ automáticamente  │
└───────────────────────────────────┘
  ↓
┌─ Crear Objeto 2 ──────────────────┐
│ mascota2 = Mascota(...)           │
├───────────────────────────────────┤
│ Cada objeto tiene sus propios     │
│ valores de atributos              │
└───────────────────────────────────┘
  ↓
┌─ Ejecutar Métodos ────────────────┐
│ mascota1.mostrar_informacion()    │
│ mascota1.hacer_sonido()           │
│ mascota2.mostrar_informacion()    │
│ mascota2.hacer_sonido()           │
└───────────────────────────────────┘
  ↓
Fin
```

## 🎓 Conceptos Fundamentales

### 1. CLASE

Una clase es un **plano o de plantilla** para crear objetos.

```python
class Mascota:
    pass
```

**Analogía**: Una clase es como un plano arquitectónico; los objetos son las casas construidas con ese plano.

### 2. OBJETO (INSTANCIA)

Un objeto es una **copia específica y única** creada a partir de una clase.

```python
mascota1 = Mascota("Firulais", "Perro", 3)
mascota2 = Mascota("Whiskers", "Gato", 2)
```

Cada objeto tiene sus **propios valores** de atributos.

### 3. ATRIBUTO

Un atributo es una **variable que pertenece a un objeto**.

```python
self.nombre = "Firulais"
self.especie = "Perro"
self.edad = 3
```

**Acceso a atributos**:
```python
print(mascota1.nombre)      # "Firulais"
print(mascota2.especie)     # "Gato"
```

### 4. MÉTODO

Un método es una **función que pertenece a una clase** y actúa sobre los datos.

```python
def mostrar_informacion(self):
    print(f"Nombre: {self.nombre}")
```

**Ejecución de métodos**:
```python
mascota1.mostrar_informacion()
mascota1.hacer_sonido()
```

### 5. ABSTRACCIÓN

La abstracción es **ocultar la complejidad interna**.

```python
# El usuario solo llama:
mascota.hacer_sonido()

# Sin conocer los detalles internos de cómo funciona
```

## 🚀 Cómo Ejecutar

### Requisitos
- Python 3.x

### Pasos

1. Abre una terminal
2. Navega a la carpeta:
   ```bash
   cd programación_poo
   ```
3. Ejecuta:
   ```bash
   python main.py
   ```

### Salida Esperada

```
==================================================
TIENDA DE MASCOTAS - PROGRAMACIÓN ORIENTADA A OBJETOS
==================================================

--- MASCOTA 1 ---

==================================================
INFORMACIÓN DE LA MASCOTA
==================================================
Nombre:  Firulais
Especie: Perro
Edad:    3 años
==================================================

Firulais dice: ¡Guau guau!
```

## 💡 Ventajas de POO

✅ **Organización superior**: Datos y comportamiento juntos  
✅ **Reutilización efectiva**: Creas múltiples objetos  
✅ **Mantenimiento sencillo**: Cambios en un lugar  
✅ **Escalabilidad**: Agregar nuevas funcionalidades es fácil  
✅ **Realismo**: El código refleja objetos del mundo real  

## 🔧 Extensiones Posibles

### Agregar Nuevos Atributos
```python
class Mascota:
    def __init__(self, nombre, especie, edad, color, peso):
        # ... todos los atributos ...
```

### Agregar Nuevos Métodos
```python
class Mascota:
    def alimentar(self):
        print(f"{self.nombre} está comiendo...")
    
    def jugar(self):
        print(f"{self.nombre} está jugando...")
```

### Usar Herencia
```python
class Perro(Mascota):
    def traer_objeto(self):
        print(f"{self.nombre} trae el objeto")

class Gato(Mascota):
    def ronronear(self):
        print(f"{self.nombre} ronronea")
```

## 📝 Ejemplo Paso a Paso

### Paso 1: Crear un Objeto

```python
mascota1 = Mascota("Firulais", "Perro", 3)
```

**Lo que sucede internamente**:
1. Python crea un nuevo objeto de la clase Mascota
2. Llama automáticamente al constructor `__init__`
3. Asigna valores a los atributos
4. Retorna el objeto

### Paso 2: Acceder a Atributos

```python
print(mascota1.nombre)      # "Firulais"
print(mascota1.especie)     # "Perro"
print(mascota1.edad)        # 3
```

### Paso 3: Ejecutar Métodos

```python
mascota1.mostrar_informacion()
mascota1.hacer_sonido()
```

## 🎯 Resumen

La **Programación Orientada a Objetos**:
- ✅ Organiza código en **clases y objetos**
- ✅ Agrupa datos y comportamiento
- ✅ Facilita reutilización código
- ✅ Mejora mantenibilidad
- ✅ Escala bien a proyectos grandes

---

*Documentación de Programación Orientada a Objetos - Semana 3*

