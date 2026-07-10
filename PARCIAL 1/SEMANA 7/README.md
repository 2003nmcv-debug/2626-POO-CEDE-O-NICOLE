# Semana 7 - Sistema Restaurante (POO)

Resumen
-------
Proyecto didáctico que adapta los conceptos de la Semana 7 (biblioteca) al dominio de un restaurante. El objetivo es practicar Programación Orientada a Objetos en Python aplicando: constructores, decoradores @property/@setter, @dataclass, validaciones y arquitectura por capas (modelos/servicios/entrada).

Estructura del proyecto
-----------------------
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py     # Clase Producto (constructor, properties, validaciones)
│   └── cliente.py      # Clase Cliente (@dataclass, validaciones básicas)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py  # Clase Restaurante (registro, listado, búsqueda, carga de ejemplos)
└── main.py             # Interfaz por consola (menú interactivo)

Características principales
--------------------------
- Producto: implementado con __init__, atributos privados y control mediante @property y @setter. Valida nombre, categoría y precio (>0). Incluye mostrar_informacion().
- Cliente: implementado con @dataclass. Contiene id_cliente, nombre y correo; valida formato básico de correo en __post_init__.
- Restaurante: servicio que administra listas de productos y clientes. Métodos: registrar, listar y buscar. Incluye cargar_ejemplos() para precargar datos didácticos.
- main.py: menú interactivo que permite registrar, listar y buscar productos y clientes. Pregunta al inicio si se desean cargar datos de ejemplo.

Cómo ejecutar
-------------
1. Abrir una terminal en la carpeta del proyecto (ejemplo Windows):
   cd C:\Users\USER\PycharmProjects\2626-POO-CEDE-O-NICOLE\restaurante_app
2. Ejecutar el programa:
   python main.py
3. Responder 's' si se desea cargar los datos de ejemplo.

Notas didácticas
----------------
- No se copia el código de la biblioteca; se toman los patrones (capas, uso de dataclass y properties). 
- El flujo de datos ejemplifica: input() -> constructor -> objeto -> servicio.registrar -> listar/buscar.
- Revisar los docstrings en modelos/ para ejemplos de uso rápido.

Sugerencias de mejora (opcional)
--------------------------------
- Persistir datos en archivos o base de datos.
- Añadir manejo avanzado de excepciones y logs.
- Implementar eliminación y edición de registros.

Autor: Nicole Micaela Cedeño Vizhñay
ID/Código: N/A
Curso/Paralelo: Paralelo C
Correo institucional: nm.cedenov@uea.edu.ec
Semana: 7
