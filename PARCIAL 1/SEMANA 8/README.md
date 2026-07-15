# Sistema de Restaurante - Programación Orientada a Objetos

## Datos del estudiante
- **Nombre completo:** NICOLE MICAELA CEDEÑO VIZHÑAY
- **Proyecto:** `restaurante_app`
- **Carpeta de trabajo:** `PARCIAL 1/SEMANA 8`
- **Tema:** Aplicación de SRP, OCP y LSP en un restaurante

## Propósito didáctico
Este proyecto está pensado para aprender POO de forma práctica. La idea es observar cómo se organiza un sistema real cuando cada clase cumple una tarea pequeña y clara.

En vez de poner toda la lógica en un solo archivo, el sistema se divide en partes:
- una clase para productos generales,
- una clase especializada para bebidas,
- una clase para clientes,
- un servicio que administra los datos,
- y un `main.py` que se encarga de la interacción con el usuario.

Así se puede ver con facilidad cómo la POO ayuda a que el código sea más ordenado, fácil de leer y más sencillo de mantener.

## Descripción general
Este proyecto implementa un sistema de consola para registrar y listar productos, bebidas y clientes de un restaurante. La solución está organizada en módulos para que cada clase cumpla una responsabilidad concreta y el servicio principal administre únicamente las colecciones y validaciones necesarias.

La clase `Bebida` amplía a `Producto` mediante herencia, lo que permite almacenar productos y bebidas en la misma lista sin modificar la lógica general del servicio. Durante el listado, el sistema usa polimorfismo: cada objeto responde con su propia implementación de `mostrar_informacion()`.

## Estructura del proyecto
```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## ¿Qué hace cada archivo?

### `modelos/producto.py`
Contiene la clase `Producto`.
- Guarda los datos comunes de un producto.
- Valida que el código, el nombre y la categoría no estén vacíos.
- Verifica que el precio sea mayor que cero.
- Ofrece `mostrar_informacion()` para presentar el producto.

### `modelos/bebida.py`
Contiene la clase `Bebida`.
- Hereda de `Producto`.
- Reutiliza los datos comunes del producto.
- Agrega información propia como `tamano` y `tipo_envase`.
- Sobrescribe `mostrar_informacion()` para mostrar más detalles.

### `modelos/cliente.py`
Contiene la clase `Cliente`.
- Representa a un cliente registrado.
- Guarda identificación, nombre y correo.
- Valida que el correo tenga un formato básico correcto.
- También ofrece `mostrar_informacion()`.

### `servicios/restaurante.py`
Contiene la clase `Restaurante`.
- Administra una lista de productos y una lista de clientes.
- Registra objetos sin duplicar códigos ni identificaciones.
- Devuelve copias de las listas para proteger la información interna.

### `main.py`
Es el archivo de ejecución.
- Muestra el menú.
- Pide datos con `input()`.
- Crea los objetos.
- Llama a los métodos del servicio.

## Paso a paso del funcionamiento
1. El usuario abre el programa desde `main.py`.
2. Aparece el menú en consola.
3. El usuario elige una opción.
4. El sistema solicita los datos necesarios.
5. Se crea un objeto `Producto`, `Bebida` o `Cliente`.
6. El objeto se envía al servicio `Restaurante`.
7. El servicio lo guarda si no existe otro igual.
8. Al listar, cada objeto muestra su información con su propio método.

## Relación entre `Producto` y `Bebida`
`Bebida` hereda de `Producto` porque una bebida sí es un tipo de producto. Esa relación permite:
- Reutilizar atributos y validaciones comunes.
- Almacenar ambos objetos en una sola colección.
- Usar el mismo método de listado sin preguntar si el objeto es `Producto` o `Bebida`.

Esto evidencia el principio de **sustitución de Liskov**: cualquier `Bebida` puede usarse donde se espere un `Producto`.

## Principios SOLID aplicados

### S — Responsabilidad única
- `Producto` representa productos.
- `Bebida` especializa productos.
- `Cliente` representa clientes.
- `Restaurante` administra colecciones y validaciones.
- `main.py` coordina la interacción por consola.

### O — Abierto / Cerrado
El sistema está abierto para agregar nuevas clases de producto sin reescribir el servicio principal. `Bebida` se incorpora como una extensión de `Producto`.

### L — Sustitución de Liskov
Una bebida puede almacenarse y listarse como producto sin alterar el comportamiento esperado del sistema.

## Instrucciones de ejecución
1. Abrir una terminal en la raíz del repositorio.
2. Ir a la carpeta del proyecto:
   ```bash
   cd "PARCIAL 1/SEMANA 8/restaurante_app"
   ```
3. Ejecutar el programa:
   ```bash
   python main.py
   ```

## Ejemplo de menú
```text
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Salir
```

## Ejemplo didáctico de uso
### Registrar un producto
- Código: `P001`
- Nombre: `Hamburguesa`
- Categoría: `Comida`
- Precio: `15.50`

### Registrar una bebida
- Código: `B001`
- Nombre: `Limonada`
- Categoría: `Bebida fría`
- Precio: `7.00`
- Tamaño: `500 ml`
- Envase: `Vaso`

### Registrar un cliente
- Identificación: `DNI12345`
- Nombre: `Ana Pérez`
- Correo: `ana.perez@example.com`

## Qué aprender con este proyecto
- Cómo crear clases en Python.
- Cómo usar herencia correctamente.
- Cómo aplicar polimorfismo en un listado.
- Cómo separar responsabilidades entre archivos.
- Cómo validar datos antes de guardarlos.
- Cómo construir un programa modular y mantenible.

## Reflexión breve
Diseñar un proyecto con responsabilidades separadas hace que el código sea más fácil de entender, probar y mejorar. Cuando cada clase tiene un propósito claro, agregar nuevas funciones no obliga a reescribir todo el sistema. Esa organización es una base importante para construir programas mantenibles y escalables.
