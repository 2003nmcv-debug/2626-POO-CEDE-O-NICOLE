# Programación Tradicional - Sistema de Registro de Mascotas

Este archivo documenta la **solución de programación tradicional** (procedural) para el registro y visualización de mascotas.

## 📌 Descripción

Implementa un sistema de mascotas **sin usar clases ni objetos**, utilizando únicamente:
- ✅ **Funciones**
- ✅ **Diccionarios**
- ✅ **Input/Output**

## 📁 Archivo del Proyecto

```
programación_tradicional/
├── tradicional.py    # Solución con funciones
└── README.md         # Este archivo
```

## 🎯 Objetivo

Crear un programa que:
1. Solicite información de una mascota por teclado
2. Almacene los datos en diccionarios
3. Muestre la información de forma organizada

## 🏗️ Estructura del Código

El programa tiene **3 funciones principales**:

### 1. `registrar_mascota()`

Solicita datos del usuario y almacena en un diccionario.

```python
def registrar_mascota():
    """
    Solicita datos y retorna diccionario con información
    """
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = input("Edad: ")
    color = input("Color: ")
    peso = input("Peso: ")
    
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "color": color,
        "peso": peso
    }
    return mascota
```

**Responsabilidades**:
- Solicitar datos con `input()`
- Almacenar en diccionario
- Retornar diccionario

### 2. `mostrar_mascota(mascota)`

Muestra los datos del diccionario de forma organizada.

```python
def mostrar_mascota(mascota):
    """
    Recibe diccionario y muestra información
    """
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad: {mascota['edad']}")
```

**Responsabilidades**:
- Recibir diccionario como parámetro
- Acceder a datos con claves
- Mostrar de forma formateada

### 3. `main()`

Controla el flujo del programa.

```python
def main():
    """
    Controla el flujo principal
    """
    mascota = registrar_mascota()
    mostrar_mascota(mascota)
```

**Responsabilidades**:
- Llamar `registrar_mascota()`
- Llamar `mostrar_mascota()`
- Controlar flujo

## 📊 Flujo del Programa

```
Inicio
  ↓
┌─ registrar_mascota() ─────────┐
│ Solicita datos por teclado    │
│ Crea diccionario              │
│ Retorna diccionario           │
└───────────────────────────────┘
  ↓
┌─ mostrar_mascota() ───────────┐
│ Recibe diccionario            │
│ Muestra datos organizados     │
└───────────────────────────────┘
  ↓
Fin
```

## 🗂️ Estructura de Datos: Diccionario

Un diccionario almacena datos como pares **clave-valor**:

```python
mascota = {
    "nombre": "Firulais",      # clave: "nombre"
    "especie": "Perro",        # valor: "Firulais"
    "edad": "3",
    "color": "Marrón",
    "peso": "25"
}
```

### Acceso a Datos

```python
# Acceder por clave
mascota["nombre"]      # "Firulais"
mascota["especie"]     # "Perro"
mascota["edad"]        # "3"
```

## 🚀 Cómo Ejecutar

### Requisitos
- Python 3.x

### Pasos

1. Abre terminal
2. Navega a la carpeta:
   ```bash
   cd programación_tradicional
   ```
3. Ejecuta:
   ```bash
   python tradicional.py
   ```

### Ejemplo de Ejecución

```
==================================================
Hola bienvenidos a su tienda mascota.
Ayúdame con los datos de su mascota
==================================================

Ingrese el nombre de su mascota: Firulais
Ingrese la especie de su mascota: Perro
Ingrese la edad de su mascota: 3
Ingrese el color de su mascota: Marrón
Ingrese el peso de su mascota (en kg): 25

==================================================
INFORMACIÓN DE LA MASCOTA REGISTRADA
==================================================
Nombre:  Firulais
Especie: Perro
Edad:    3 años
Color:   Marrón
Peso:    25 kg
==================================================

¡Gracias por registrar tu mascota!
```

## 💡 Conceptos Clave

### 1. Funciones

Agrupa código reutilizable:

```python
def registrar_mascota():    # Sin parámetros
    pass

def mostrar_mascota(mascota):  # Con parámetro
    pass
```

### 2. Parámetros y Retorno

```python
def registrar_mascota():
    # ... código ...
    return mascota          # Retorna diccionario

def mostrar_mascota(mascota):  # Recibe parámetro
    # ... código ...
    # No retorna nada
```

### 3. Diccionarios

Estructura de datos clave-valor:

```python
mascota = {
    "nombre": "Firulais",
    "especie": "Perro"
}
```

### 4. Input/Output

```python
nombre = input("Ingrese nombre: ")     # Input
print(f"Nombre: {nombre}")             # Output
```

## ✅ Ventajas de Este Enfoque

1. **Simplicidad**: Código directo y comprensible
2. **Rapidez**: Menos boilerplate
3. **Ideal para scripts**: Perfecto para tareas simples
4. **Bajo acoplamiento**: Funciones independientes
5. **Fácil de debuggear**: Flujo secuencial claro

## ❌ Limitaciones

1. **Escalabilidad limitada**: Difícil en proyectos grandes
2. **Código repetitivo**: Múltiples mascotas = repetición
3. **Mantenimiento complejo**: Cambios afectan múltiples lugares
4. **Pobre organización**: Demasiadas funciones sueltas
5. **Sin reutilización**: Necesitas pasar datos constantemente

## 🔧 Posibles Extensiones

### Registrar Múltiples Mascotas

```python
def registrar_multiples_mascotas():
    mascotas = []
    registrar_mas = True
    
    while registrar_mas:
        mascota = registrar_mascota()
        mascotas.append(mascota)
        registrar_mas = input("¿Otra? (s/n): ").lower() == 's'
    
    return mascotas
```

### Guardar en Archivo

```python
import json

def guardar_mascota(mascota):
    with open("mascota.json", 'w') as f:
        json.dump(mascota, f)
```

### Validar Entrada

```python
def registrar_mascota_validado():
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
    
    while True:
        edad_str = input("Edad: ")
        if edad_str.isdigit():
            break
    
    # ...resto del código...
```

## 📝 Ejemplo Completo

```python
# Función 1
def registrar_mascota():
    mascota = {
        "nombre": input("Nombre: "),
        "especie": input("Especie: "),
        "edad": input("Edad: ")
    }
    return mascota

# Función 2
def mostrar_mascota(mascota):
    print("\n" + "=" * 50)
    print(f"Nombre: {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad: {mascota['edad']}")
    print("=" * 50)

# Función 3
def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)

# Ejecutar
if __name__ == "__main__":
    main()
```

## 🎓 Comparación: Función vs Método

### Con Programación Tradicional

```python
def mostrar_mascota(mascota):
    # Recibe datos como parámetro
    print(mascota['nombre'])

# Usar:
mostrar_mascota(unidades_mascota)
```

### Con POO

```python
class Mascota:
    def mostrar_informacion(self):
        # Ya tiene acceso a datos
        print(self.nombre)

# Usar:
mascota = Mascota("Firulais", "Perro", 3)
mascota.mostrar_informacion()
```

## 📚 Cuándo Usar Este Enfoque

### ✅ Usa Cuando:
- Proyecto pequeño y simple
- Necesitas prototipado rápido
- Equipo nuevo en programación
- Código de corta duración
- Script o automatización

### ❌ NO uses Cuando:
- Proyecto grande y complejo
- Necesitas reutilizar similar múltiples veces
- Trabajo en equipo a larga duración
- Muchos cambios y extensiones futuras

## 🔗 Ver También

- **Programación Orientada a Objetos**: `programación_poo/`
- **Visión General de Semana 3**: Archivo README.md principal

## 📄 Resumen

Este enfoque **procedural** es válido para problemas simples. Para proyectos complejos, la **Programación Orientada a Objetos** ofrece mejor organización y escalabilidad.

**Lo importante**: Entender AMBOS enfoques y saber cuándo usar cada uno.

---

*Documentación de Programación Tradicional - Semana 3*

