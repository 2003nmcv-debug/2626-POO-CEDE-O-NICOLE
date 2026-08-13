# Semana 9 - restaurante_app

## Estudiante
- Nombre completo: **Nicole Micaela Cedeño Vizhñay**

## Descripcion breve
Este proyecto implementa un sistema de consola para administrar productos y usuarios de un restaurante.
Se mantiene la arquitectura modular con modelos, servicios y punto de arranque en `main.py`.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

## Responsabilidad de componentes
- `restaurante_app/modelos/producto.py`: define la entidad `Producto`.
- `restaurante_app/modelos/usuario.py`: define la entidad `Usuario`.
- `restaurante_app/servicios/restaurante.py`: gestiona colecciones y operaciones del sistema.
- `restaurante_app/main.py`: controla el menu interactivo y la entrada por consola.

## Uso de estructuras de datos
- `list`: en `Restaurante` se usan listas para almacenar dinamicamente productos y usuarios.
- `tuple`: en `main.py` la tupla `OPCIONES_MENU` guarda opciones estables del menu.
- `dict`: en `main.py` el diccionario `acciones` relaciona opcion -> funcion.
- `set`: en `Restaurante.obtener_categorias_unicas()` se obtienen categorias sin duplicados.

## Funcionalidades implementadas
- Registrar producto (con validacion de codigo unico)
- Buscar producto por codigo
- Actualizar producto
- Eliminar producto
- Listar productos
- Registrar usuario (con validacion de identificacion unica)
- Listar usuarios
- Mostrar categorias unicas de productos

## Ejecucion
Desde la carpeta `SEMANA 9`:

```bash
python -m restaurante_app.main
```

## Reflexion
Elegir bien la estructura de datos mejora la claridad, la eficiencia y el mantenimiento del sistema.
En este ejercicio, cada estructura fue usada para resolver una necesidad real del flujo del programa,
evita codigo redundante y facilita futuras ampliaciones.

