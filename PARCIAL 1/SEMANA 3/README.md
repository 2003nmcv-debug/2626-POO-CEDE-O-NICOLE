# 📚 SEMANA 3 - Programación Tradicional vs Programación Orientada a Objetos

## 🎯 Descripción General

En la **Semana 3** aprendimos a desarrollar la misma solución de dos formas fundamentalmente diferentes:

1. **Programación Tradicional** (Procedural): Usando funciones y estructuras de datos simples
2. **Programación Orientada a Objetos (POO)**: Usando clases y objetos

**Problema a resolver**: Sistema de Registro y Visualización de Información de Mascotas

> **Objetivo principal**: Entender cuándo y por qué usar cada paradigma de programación

---

## 📁 Estructura del Proyecto

```
SEMANA 3/
│
├── README.md (Este archivo - Visión General)
│
├── programación_tradicional/
│   ├── tradicional.py          ← Solución con funciones
│   └── README.md               ← Documentación detallada
│
└── programación_poo/
    ├── mascota.py              ← Clase Mascota
    ├── main.py                 ← Programa principal
    └── README.md               ← Documentación detallada
```

---

## 📖 Índice de Contenidos

- [Programación Tradicional](#-programación-tradicional)
- [Programación Orientada a Objetos](#-programación-orientada-a-objetos)
- [Comparativa Detallada](#-comparativa-detallada)
- [Conceptos Clave de POO](#-conceptos-clave-de-poo)
- [Cuándo Usar Cada Enfoque](#-cuándo-usar-cada-enfoque)
- [Cómo Ejecutar los Programas](#-cómo-ejecutar-los-programas)
- [Conclusiones](#-conclusiones)

---

## 🔵 Programación Tradicional

### ¿Qué es?

Un enfoque **procedural** donde el código se organiza en **funciones** independientes que procesan datos almacenados en **estructuras de datos simples** (diccionarios, listas, tuplas).

### Características

📌 **Funciones independientes**: Cada función realiza una tarea específica  
📌 **Separación de datos y comportamiento**: Los datos están en diccionarios, las funciones los procesan  
📌 **Flujo secuencial**: El programa sigue un paso a paso claro  
📌 **Paso de parámetros**: Los datos se pasan entre funciones  

### Ejemplo de Estructura

```python
# Función 1: Obtener datos
def registrar_mascota():
    mascota = {
        "nombre": input("Nombre: "),
        "especie": input("Especie: "),
        "edad": input("Edad: ")
    }
    return mascota  # Retorna diccionario

# Función 2: Mostrar datos
def mostrar_mascota(mascota):  # Recibe diccionario como parámetro
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")

# Función 3: Controlar flujo
def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)
```

### Ventajas ✅

1. **Simplicidad**: Código lineal y fácil de entender
2. **Rápida implementación**: Menos boilerplate
3. **Ideal para scripts**: Perfecta para automatizaciones pequeñas
4. **Bajo acoplamiento inicial**: Funciones independientes
5. **Fácil de debuggear**: Flujo secuencial claro

### Desventajas ❌

1. **Escalabilidad limitada**: Difícil en proyectos grandes
2. **Código repetitivo**: Si tienes múltiples mascotas, repites lógica
3. **Mantenimiento complicado**: Cambios afectan múltiples lugares
4. **Pobre organización**: Demasiadas funciones sueltas
5. **Sin reutilización de estado**: Necesitas pasar datos constantemente

### Cuándo usarla

✅ Proyectos pequeños y simples  
✅ Scripts de una sola tarea  
✅ Prototipado rápido  
✅ Equipos nuevos en programación  

---

## 🟣 Programación Orientada a Objetos

### ¿Qué es?

Un enfoque donde el código se organiza en **clases** que **encapsulan datos (atributos) y comportamiento (métodos)** de forma integrada.

### Características

📌 **Clases y Objetos**: Una clase es el molde, un objeto es la instancia  
📌 **Datos y comportamiento juntos**: Atributos y métodos en la misma clase  
📌 **Reutilización de objetos**: Creas múltiples instancias del mismo tipo  
📌 **Abstracción**: Ocultas la complejidad interna  

### Ejemplo de Estructura

```python
# Clase: Define el molde
class Mascota:
    # Constructor: Inicializa atributos
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre      # Atributo
        self.especie = especie    # Atributo
        self.edad = edad          # Atributo
    
    # Método 1: Mostrar información
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
    
    # Método 2: Hacer sonido
    def hacer_sonido(self):
        print(f"{self.nombre} emite sonidos")

# Crear objetos
mascota1 = Mascota("Firulais", "Perro", 3)
mascota2 = Mascota("Whiskers", "Gato", 2)

# Usar objetos
mascota1.mostrar_informacion()
mascota1.hacer_sonido()
```

### Ventajas ✅

1. **Excelente organización**: Datos y métodos relacionados juntos
2. **Reutilización efectiva**: Creas múltiples objetos sin repetir lógica
3. **Mantenimiento sencillo**: Cambios en un lugar afectan a todos
4. **Escalabilidad alta**: Fácil agregar nuevas clases y funcionalidades
5. **Refleja la realidad**: Los objetos del código representan objetos reales

### Desventajas ❌

1. **Curva de aprendizaje**: Más conceptos que memorizar
2. **Complejidad inicial**: Para problemas muy simples es "overkill"
3. **Más boilerplate**: Necesitas constructores, self, etc.
4. **Overhead mínimo**: Ligeramente más lento en ciertos casos

### Cuándo usarla

✅ Proyectos grandes y complejos  
✅ Código que necesita mantenimiento a largo plazo  
✅ Múltiples tipos de objetos similares  
✅ Trabajo en equipo  

---

## 📊 Comparativa Detallada

### Tabla Comparativa Principal

| Aspecto | Programación Tradicional | POO |
|---------|--------------------------|-----|
| **Unidad Base** | Función | Clase |
| **Almacenamiento de Datos** | Diccionarios/Listas | Atributos del Objeto |
| **Comportamiento** | Funciones separadas | Métodos en la clase |
| **Reutilización** | Llamadas a funciones | Creación de objetos |
| **Extensibilidad** | Limitada | Alta |
| **Complejidad** | Baja | Media |
| **Escalabilidad** | Baja-Media | Alta |
| **Ideal Para** | Pequeños scripts | Proyectos grandes |

### Comparación Visual

#### Enfoque Tradicional: DATOS y COMPORTAMIENTO SEPARADOS

```
Datos:
┌─────────────────┐
│ Diccionario     │
│ nombre: "..."   │
│ especie: "..."  │
│ edad: ...       │
└─────────────────┘

         ↓↑ (paso de parámetros)

Comportamiento:
┌─────────────────────┐
│ def registrar()     │
│ def mostrar()       │
│ def hacer_sonido()  │
└─────────────────────┘
```

#### Enfoque POO: DATOS y COMPORTAMIENTO JUNTOS

```
┌─────────────────────────────────┐
│         Clase Mascota           │
├─────────────────────────────────┤
│ Atributos:                      │
│  - nombre: String               │
│  - especie: String              │
│  - edad: Int                    │
├─────────────────────────────────┤
│ Métodos:                        │
│  - __init__()                   │
│  - mostrar_informacion()        │
│  - hacer_sonido()               │
└─────────────────────────────────┘
         ↓
    Objeto 1: mascota1
    Objeto 2: mascota2
    Objeto 3: mascota3
```

---

## 🎯 Conceptos Clave de POO

### 1. **CLASE**

Una clase es un **plano o plantilla** para crear objetos. Define qué datos tendrán y qué acciones podrán hacer.

```python
class Mascota:                    # Nombre de la clase
    def __init__(self, ...):      # Constructor
        self.nombre = ...         # Atributos
    def mostrar_informacion(self): # Métodos
        pass
```

**Analógico**: Si una clase fuera un plano arquitectónico, los objetos serían las casas construidas con ese plano.

### 2. **OBJETO (Instancia)**

Un objeto es una **copia específica y única** creada a partir de una clase.

```python
mascota1 = Mascota("Firulais", "Perro", 3)  # Objeto 1
mascota2 = Mascota("Whiskers", "Gato", 2)   # Objeto 2
```

Cada objeto tiene sus propios valores de atributos, pero comparte la misma estructura.

### 3. **ATRIBUTOS**

Un atributo es una **variable que pertenece a un objeto** y almacena información sobre él.

```python
self.nombre = "Firulais"    # Atributo
self.especie = "Perro"      # Atributo
self.edad = 3               # Atributo
```

**Acceso a atributos**:
```python
print(mascota1.nombre)      # Acceso directo: "Firulais"
print(mascota2.especie)     # Acceso directo: "Gato"
```

### 4. **MÉTODOS**

Un método es una **función que pertenece a una clase** y actúa sobre los objetos.

```python
def mostrar_informacion(self):  # self = referencia al objeto
    print(self.nombre)          # Acceso a atributo
    print(self.especie)
```

**Diferencia clave**:
- **Función**: Independiente, recibe parámetros
- **Método**: Pertenece a una clase, tiene acceso a `self`

**Ejecución de métodos**:
```python
mascota1.mostrar_informacion()   # El objeto ejecuta su método
mascota1.hacer_sonido()
```

### 5. **ABSTRACCIÓN**

La abstracción es **ocultar la complejidad interna** que el usuario no necesita conocer.

```python
# El usuario solo llama:
mascota.hacer_sonido()

# Sin necesidad de saber que internamente:
# 1. Crea un diccionario de sonidos
# 2. Valida la especie
# 3. Obtiene el sonido correspondiente
# 4. Lo imprime con formato personalizado
```

---

## 🔄 Ejemplo Práctico: Agregar Nueva Funcionalidad

Imagina que quieres que la mascota pueda **interactuar (jugar)**.

### Con Programación Tradicional

```python
# Necesitas crear UNA NUEVA FUNCIÓN
def hacer_jugar(mascota):
    print(f"{mascota['nombre']} está jugando!")

# Y MODIFICAR main() para usarla
def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)
    hacer_jugar(mascota)           # ← Nueva línea
```

**Problema**: Más funciones sueltas, código menos organizado.

### Con Programación Orientada a Objetos

```python
# SOLO AGREGAS UN MÉTODO a la clase
class Mascota:
    # ... atributos ...
    
    def jugar(self):  # ← Nuevo método
        print(f"{self.nombre} está jugando!")

# El main NO necesita cambios
def main():
    mascota = Mascota("Firulais", "Perro", 3)
    mascota.mostrar_informacion()
    mascota.hacer_sonido()
    mascota.jugar()               # ← Ahora disponible para todos
```

**Ventaja**: El objeto "sabe" cómo jugar automáticamente.

---

## 🚀 Cómo Ejecutar los Programas

### Solución Tradicional

```bash
# Navega a la carpeta
cd programación_tradicional

# Ejecuta el programa
python tradicional.py

# El programa te pedirá:
# - Nombre de la mascota
# - Especie
# - Edad
# - Color
# - Peso
```

### Solución Orientada a Objetos

```bash
# Navega a la carpeta
cd programación_poo

# Ejecuta el programa
python main.py

# El programa creará 3 mascotas automáticamente
# y mostrará su información y comportamiento
```

---

## 💡 Cuándo Usar Cada Enfoque

### Usa Programación Tradicional Si:
- ✅ El proyecto es **pequeño y simple**
- ✅ Necesitas **prototipado rápido**
- ✅ Trabajas solo o en equipo muy pequeño
- ✅ El código es **de corta duración**
- ✅ Es un **script o automatización**

### Usa Programación Orientada a Objetos Si:
- ✅ El proyecto es **grande y complejo**
- ✅ Habrá **múltiples tipos** de objetos similares
- ✅ Necesitas **código reutilizable**
- ✅ Se requiere **mantenimiento a largo plazo**
- ✅ Trabajas en **equipo grande**

---

## 📚 Conceptos Relacionados

### Encapsulamiento
Agrupar datos (atributos) y métodos relacionados en una clase.

```python
class Mascota:
    # TODO lo relacionado con una mascota aquí
    self.nombre
    self.especie
    def mostrar_informacion(self)
    def hacer_sonido(self)
```

### Constructor (`__init__`)
Método especial que se ejecuta automáticamente al crear un objeto.

```python
def __init__(self, nombre, especie, edad):
    self.nombre = nombre          # Inicializa atributo
    self.especie = especie
    self.edad = edad
```

### Self
Referencia al objeto en el que estás trabajando dentro de sus métodos.

```python
def mostrar_informacion(self):
    print(self.nombre)  # self = el objeto mismo
```

---

## 🎓 Objetivos Alcanzados

### ✅ Aplicaciones de Programación Tradicional
- [x] Crear funciones para registrar datos
- [x] Crear funciones para mostrar datos
- [x] Solicitar datos mediante teclado (input)
- [x] Usar diccionarios para almacenar datos
- [x] Mostrar información de forma organizada
- [x] **Sin usar clases ni objetos**

### ✅ Aplicaciones de Programación Orientada a Objetos
- [x] Crear una clase llamada Mascota
- [x] Definir atributos (nombre, especie, edad)
- [x] Implementar métodos (mostrar_información, hacer_sonido)
- [x] Crear objetos (instancias)
- [x] Separar en múltiples archivos (mascota.py y main.py)
- [x] Demostrar concepto de abstracción
- [x] Ejecutar métodos de los objetos
- [x] Acceder a atributos de los objetos

---

## 🔗 Documentación Adicional

Cada carpeta tiene su propio README.md con documentación detallada:

- 📄 **programación_tradicional/README.md**: Máximo detalle sobre funciones y diccionarios
- 📄 **programación_poo/README.md**: Máximo detalle sobre clases, objetos y POO

---

## 🏁 Conclusiones Importantes

### 1. **No hay un "mejor" enfoque**
Ambos son válidos según el contexto y problemática a resolver.

### 2. **La elección depende del problema**
- Problemas pequeños → Programación Tradicional
- Proyectos grandes → Programación Orientada a Objetos

### 3. **POO es estándar en la industria**
La mayoría de proyectos profesionales utilizan objetos.

### 4. **Dominar ambos te hace versátil**
Un buen programador entiende y puede usar ambos paradigmas.

### 5. **A menudo se combinan**
Muchos proyectos usan ambos enfoques en diferentes partes.

---

## 📝 Resumen Visual

```
PROBLEMA: Sistema de Mascotas

│
├─ SOLUCIÓN TRADICIONAL (programación_tradicional/)
│  └─ Funciones + Diccionarios
│     ├─ registrar_mascota()
│     ├─ mostrar_mascota()
│     └─ main()
│
└─ SOLUCIÓN POO (programación_poo/)
   └─ Clase + Objetos
      ├─ Clase Mascota
      │  ├─ Atributos: nombre, especie, edad
      │  └─ Métodos: __init__(), mostrar_informacion(), hacer_sonido()
      └─ Objetos: mascota1, mascota2, mascota3
```

---

## 📖 Tabla de Archivos

| Archivo | Descripción | Tipo |
|---------|-------------|------|
| `programación_tradicional/tradicional.py` | Solución con funciones | Python |
| `programación_tradicional/README.md` | Documentación detallada | Markdown |
| `programación_poo/mascota.py` | Definición de clase | Python |
| `programación_poo/main.py` | Programa que usa la clase | Python |
| `programación_poo/README.md` | Documentación detallada | Markdown |
| `SEMANA 3/README.md` | Visión general (este archivo) | Markdown |

---

## 🎯 Lo Que Deberías Recordar

1. **Programación Tradicional**: Piensa en PASOS y FUNCIONES
2. **Programación Orientada a Objetos**: Piensa en ENTIDADES y OBJETOS
3. **Atributos**: Son las características del objeto
4. **Métodos**: Son las acciones que puede hacer el objeto
5. **Abstracción**: Oculta la complejidad interna
6. **Ambos paradigmas son importantes**: Aprende los dos

---

## 🏫 Próximas Semanas

Con lo aprendido en la Semana 3, estás preparado para:
- ✅ Entender y analizar código orientado a objetos
- ✅ Diseñar clases efectivas
- ✅ Implementar herencia y polimorfismo
- ✅ Trabajar con frameworks modernos (Django, Flask, etc.)
- ✅ Participar en proyectos de software real

---

**¡Excelente trabajo completando la Semana 3!** 🎉

*Ahora dominas dos paradigmas fundamentales de programación.*

---

*Documentación de SEMANA 3 - Programación Tradicional vs Programación Orientada a Objetos*  
*Nivel: Introductorio a Intermedio*  
*Fecha: Junio 2026*

