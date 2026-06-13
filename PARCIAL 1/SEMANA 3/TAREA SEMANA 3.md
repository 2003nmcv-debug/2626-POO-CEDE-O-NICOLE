# 📝 TAREA SEMANA 3 - Explicación de Programación Tradicional vs POO

## 🎯 Objetivo de la Tarea

Comprender profundamente la diferencia entre dos paradigmas de programación fundamentales:
- **Programación Tradicional (Procedural)**
- **Programación Orientada a Objetos (POO)**

---

## 📋 PARTE 1: Preguntas de Comprensión

### Sección A: Conceptos Generales

**Pregunta 1.1**: ¿Cuál es la diferencia fundamental entre una función y un método?

**Respuesta esperada**: 
- Una **función** es independiente y puede usarse en cualquier contexto
- Un **método** pertenece a una clase y tiene acceso a `self` (los datos del objeto)

---

**Pregunta 1.2**: ¿Qué es una clase en Programación Orientada a Objetos?

**Respuesta esperada**:
Una clase es un **plano o plantilla** que define:
- Qué datos tendrá el objeto (atributos)
- Qué acciones puede hacer (métodos)

Ejemplo: La clase `Mascota` es el molde; cada objeto es una mascota específica.

---

**Pregunta 1.3**: ¿Qué es un objeto?

**Respuesta esperada**:
Un objeto es una **instancia específica de una clase**. Es la copia creada a partir del molde.

Ejemplo:
```python
mascota1 = Mascota("Firulais", "Perro", 3)  # Objeto 1
mascota2 = Mascota("Whiskers", "Gato", 2)   # Objeto 2
```

Cada objeto es independiente con sus propios datos.

---

### Sección B: Programación Tradicional

**Pregunta 2.1**: En programación tradicional, ¿cómo se almacenan los datos?

**Respuesta esperada**:
Los datos se almacenan en **estructuras de datos simples** como:
- Diccionarios: `{"nombre": "Firulais", "especie": "Perro"}`
- Listas: `[mascota1, mascota2, mascota3]`
- Tuplas: `(nombre, especie, edad)`

---

**Pregunta 2.2**: ¿Cómo se pasan los datos entre funciones en programación tradicional?

**Respuesta esperada**:
Los datos se pasan mediante **parámetros**:

```python
def mostrar_mascota(mascota):  # mascota es parámetro
    print(mascota['nombre'])

mostrar_mascota(unidades_mascota)  # Pasamos el diccionario
```

Los datos **viajan** de función en función.

---

**Pregunta 2.3**: Menciona 3 ventajas de la programación tradicional:

**Respuesta esperada**:
1. ✅ **Simplicidad**: Código directo y fácil de entender
2. ✅ **Rapidez**: Menos código boilerplate
3. ✅ **Ideal para scripts**: Perfecta para tareas simples

---

**Pregunta 2.4**: Menciona 3 limitaciones de la programación tradicional:

**Respuesta esperada**:
1. ❌ **Escalabilidad limitada**: Difícil mantener en proyectos grandes
2. ❌ **Código repetitivo**: Múltiples mascotas significa repetir lógica
3. ❌ **Mantenimiento complejo**: Cambios necesarios en múltiples lugares

---

### Sección C: Programación Orientada a Objetos

**Pregunta 3.1**: ¿Qué es un atributo?

**Respuesta esperada**:
Un atributo es una **variable que pertenece a un objeto** y almacena información sobre él.

Ejemplo:
```python
self.nombre = "Firulais"   # Atributo
self.edad = 3              # Atributo
self.especie = "Perro"     # Atributo
```

---

**Pregunta 3.2**: ¿Qué es `self` en un método de una clase?

**Respuesta esperada**:
`self` es una **referencia al objeto mismo**. Permite acceder a los atributos del objeto desde dentro de sus métodos.

Ejemplo:
```python
def mostrar_informacion(self):
    print(self.nombre)     # self.nombre accede al atributo del objeto
```

---

**Pregunta 3.3**: ¿Qué es el constructor (`__init__`)?

**Respuesta esperada**:
El constructor es un **método especial** que:
- Se ejecuta automáticamente al crear un objeto
- Inicializa los atributos del objeto
- Tiene el nombre especial `__init__`

Ejemplo:
```python
def __init__(self, nombre, especie, edad):
    self.nombre = nombre      # Inicializa atributo
    self.especie = especie
    self.edad = edad
```

---

**Pregunta 3.4**: ¿Qué es la abstracción en POO?

**Respuesta esperada**:
La abstracción es **ocultar la complejidad interna**. El usuario solo necesita saber qué hace un método, no cómo lo hace internamente.

Ejemplo:
```python
# El usuario solo llama:
mascota.hacer_sonido()

# Sin necesidad de saber que internamente:
# - Busca en un diccionario de sonidos
# - Obtiene el sonido según la especie
# - Lo formatea
# - Lo imprime
```

---

**Pregunta 3.5**: Menciona 3 ventajas de la Programación Orientada a Objetos:

**Respuesta esperada**:
1. ✅ **Mejor organización**: Datos y comportamiento juntos
2. ✅ **Reutilización efectiva**: Creas múltiples objetos sin repetir lógica
3. ✅ **Escalabilidad**: Fácil agregar nuevas funcionalidades

---

**Pregunta 3.6**: Menciona 2 desventajas de la Programación Orientada a Objetos:

**Respuesta esperada**:
1. ❌ **Curva de aprendizaje**: Más conceptos que entender
2. ❌ **Complejidad inicial**: Para problemas simples puede ser excesivo

---

## 📊 PARTE 2: Comparativa Detallada

### Tabla Comparativa

Completa la siguiente tabla comparativa:

| Aspecto | Programación Tradicional | POO |
|---------|--------------------------|-----|
| **¿Cómo se agrupen los datos?** | En diccionarios/listas | En atributos de objetos |
| **¿Dónde está el comportamiento?** | En funciones separadas | En métodos de la clase |
| **¿Cómo se reutiliza el código?** | Llamando funciones múltiples veces | Creando múltiples objetos |
| **¿Es escalable?** | Limitadamente | Altamente |
| **Unidad principal de organización** | Función | Clase |

### Respuestas Esperadas

| Aspecto | Programación Tradicional | POO |
|---------|--------------------------|-----|
| **¿Cómo se agrupen los datos?** | En diccionarios/listas | En atributos de objetos |
| **¿Dónde está el comportamiento?** | En funciones separadas | En métodos de la clase |
| **¿Cómo se reutiliza el código?** | Llamando funciones múltiples veces | Creando múltiples objetos |
| **¿Es escalable?** | Limitadamente (para problemas simples) | Altamente (para proyectos complejos) |
| **Unidad principal de organización** | Función (unidad de código reutilizable) | Clase (unidad de datos + comportamiento) |

---

## 🔍 PARTE 3: Análisis de Código

### Ejercicio 3.1: Identificar Elementos de POO

Dado el siguiente código, identifica:

```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")

mascota = Mascota("Firulais", "Perro", 3)
mascota.mostrar_informacion()
```

**a) Identifica la clase:**
```
Respuesta: Mascota
```

**b) Identifica los atributos:**
```
Respuesta: nombre, especie, edad
```

**c) Identifica los métodos:**
```
Respuesta: __init__(), mostrar_informacion()
```

**d) Identifica el objeto (instancia):**
```
Respuesta: mascota
```

**e) ¿Cuál es el propósito del método `__init__`?**
```
Respuesta: Inicializar los atributos del objeto cuando se crea
```

---

### Ejercicio 3.2: Convertir Código

Convierte el siguiente código de programación tradicional a POO:

**Código Original (Tradicional)**:
```python
def crear_mascota(nombre, especie, edad):
    return {"nombre": nombre, "especie": especie, "edad": edad}

def mostrar_mascota(mascota):
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad: {mascota['edad']}")

mascota = crear_mascota("Firulais", "Perro", 3)
mostrar_mascota(mascota)
```

**Conversión a POO (Respuesta Esperada)**:
```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")

mascota = Mascota("Firulais", "Perro", 3)
mascota.mostrar_informacion()
```

**Diferencias clave:**
- ❌ Ya no necesitamos `crear_mascota()` → El constructor `__init__` lo hace
- ❌ Ya no pasamos diccionarios → El objeto guarda los datos
- ❌ Ya no pasamos datos a función → El método accede a los atributos con `self`

---

## 🎓 PARTE 4: Casos de Uso

### Ejercicio 4.1: Decidir Qué Enfoque Usar

Para cada situación, decide si usarías **Programación Tradicional (PT)** o **POO**:

| Situación | PT o POO | Justificación |
|-----------|----------|---------------|
| Crear un script que procese un archivo CSV | PT | Es una tarea simple y de corta duración |
| Desarrollar un video juego con múltiples personajes | POO | Cada personaje es un objeto con atributos y métodos |
| Automatizar copias de seguridad diarias | PT | Es una tarea repetitiva y simple |
| Crear un sistema de gestión de tienda con cientos de productos | POO | Escalabilidad y mantenimiento a largo plazo |
| Calcular el promedio de valores en una lista | PT | Operación simple y directa |
| Crear una red social con usuarios, mensajes y comentarios | POO | Entidades complejas y relaciones entre objetos |

---

## 📝 PARTE 5: Explicación Escrita

### Pregunta de Reflexión 1

**Pregunta**: Explica en tus propias palabras por qué es importante entender AMBOS paradigmas de programación.

**Guía de Respuesta**:
Deberías mencionar:
1. Ambos son válidos según el contexto
2. Los problemas simples son más rápido resolverlos con programación tradicional
3. Los proyectos grandes necesitan POO para mantener código limpio
4. Un programador versátil puede elegir la mejor herramienta para cada problema
5. En la industria, necesitas saber ambos

---

### Pregunta de Reflexión 2

**Pregunta**: ¿Cuál es la analogía más útil que encontraste para entender clases y objetos?

**Posibles Respuestas** (escoge una o crea la tuya):
- **Receta de cocina**: La clase es la receta, los objetos son los postres hechos con esa receta
- **Molde de galletas**: La clase es el molde, los objetos son las galletas cortadas
- **Plano arquitectónico**: La clase es el plano, los objetos son las casas construidas
- **Clase escolar**: La clase define qué atributos (nombre, edad) y métodos (estudiar, jugar) tiene un estudiante

---

### Pregunta de Reflexión 3

**Pregunta**: Describe una situación real (no de programación) donde verías una clase y múltiples objetos.

**Ejemplos de Respuestas**:
1. **Autos**: Clase = diseño de auto, Objetos = cada auto construido (Ferrari rojo, Tesla blanco, etc.)
2. **Teléfonos móviles**: Clase = modelo iPhone 15, Objetos = cada iPhone 15 específico que existe
3. **Estudiantes**: Clase = Estudiante, Objetos = Juan, María, Roberto (cada uno con sus propios datos)
4. **Mascotas**: Clase = Mascota, Objetos = cada mascota específica con su nombre, edad, especie

---

## ✅ PARTE 6: Autoevaluación

### Evaluación de tu Comprensión

Marca con ✅ si comprendes cada concepto:

| Concepto | ¿Lo Entiendo? |
|----------|---------------|
| Diferencia entre función y método | ✅ |
| Qué es una clase | ✅ |
| Qué es un objeto | ✅ |
| Qué es un atributo | ✅ |
| Qué es un método | ✅ |
| Para qué sirve `__init__` | ✅ |
| Qué es `self` | ✅ |
| Qué es abstracción | ✅ |
| Cuándo usar programación tradicional | ✅ |
| Cuándo usar POO | ✅ |

**Si no has marcado todos con ✅**, revisa los archivos README.md de las subcarpetas.

---

## 📚 PARTE 7: Ejercicios Prácticos

### Ejercicio 7.1: Extender la Clase Mascota

**Desafío**: Agrega un nuevo método a la clase `Mascota` que imprima "X está comiendo".

**Código a completar**:
```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
    
    # TODO: Agrega el nuevo método aquí
    def alimentar(self):
        print(f"{self.nombre} está comiendo")

# Usar:
mascota = Mascota("Firulais", "Perro", 3)
mascota.alimentar()  # Output: Firulais está comiendo
```

---

### Ejercicio 7.2: Crear Nueva Clase

**Desafío**: Crea una clase `Persona` con:
- Atributos: nombre, edad, profesión
- Métodos: saludar(), trabajar()

**Respuesta Esperada**:
```python
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.profesion}")

# Usar:
persona = Persona("Juan", 30, "Ingeniero")
persona.saludar()      # Output: Hola, soy Juan
persona.trabajar()     # Output: Juan está trabajando como Ingeniero
```

---

### Ejercicio 7.3: Múltiples Objetos

**Desafío**: Crea 3 mascotas diferentes y ejecuta sus métodos.

**Respuesta Esperada**:
```python
mascota1 = Mascota("Firulais", "Perro", 3)
mascota2 = Mascota("Whiskers", "Gato", 2)
mascota3 = Mascota("Tweety", "Pajaro", 1)

mascota1.mostrar_informacion()
mascota1.hacer_sonido()

mascota2.mostrar_informacion()
mascota2.hacer_sonido()

mascota3.mostrar_informacion()
mascota3.hacer_sonido()
```

---

## 📞 Dudas Comunes

### ¿Por qué se llama "Orientada a Objetos"?
Porque la **unidad principal de organización es el objeto**. Todo gira alrededor de los objetos que tienes y qué pueden hacer.

### ¿A qué se refiere "heredar"?
Una clase puede **heredar** atributos y métodos de otra clase:
```python
class Perro(Mascota):          # Perro hereda de Mascota
    def traer_objeto(self):    # Método exclusivo de Perro
        print(f"{self.nombre} trae el objeto")
```

### ¿Cuál es la diferencia entre clase e instancia?
- **Clase**: El molde/plantilla (Mascota)
- **Instancia**: El objeto creado (mascota1, mascota2, mascota3)

---

## 🎯 Resumen Final

### Conceptos Clave a Recordar

1. **Clase** = Molde/Plantilla
2. **Objeto** = Instancia del molde
3. **Atributo** = Dato del objeto
4. **Método** = Función del objeto
5. **Abstracción** = Ocultar complejidad
6. **Encapsulamiento** = Agrupar datos y métodos
7. **`self`** = Referencia al objeto
8. **`__init__`** = Constructor

### Regla de Decisión

```
¿Es un problema PEQUEÑO y SIMPLE?
    → Usa Programación Tradicional
    
¿Es un proyecto GRANDE y COMPLEJO?
    → Usa Programación Orientada a Objetos
```

---

**Fecha**: Junio 2026  
**Semana**: 3  
**Nivel**: Introductorio a Intermedio  
**Tiempo Estimado**: 2-3 horas  

*Completa esta tarea para afianzar tu comprensión de los paradigmas de programación.*

