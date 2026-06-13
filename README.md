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
└── README.md                          # Este archivo

```

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
