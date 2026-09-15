# Semana 14 - aplicación gráfica del restaurante

## Descripción

Se implementó una interfaz gráfica en Tkinter para gestionar el acceso a la aplicación del restaurante y visualizar la información básica del sistema. La estructura del proyecto separa modelos, servicios y vistas para mantener un código más ordenado y reutilizable.

## Características

- Login con validación de usuario y contraseña.
- Vista principal con resumen de cantidad de productos, usuarios y stock total.
- Listado de productos y usuarios en tablas de la interfaz.
- Botón de cierre de sesión y cambio de pantalla entre vistas.
- Carga inicial de datos desde archivos JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Responsabilidad de cada componente

- `modelos/producto.py`: representa un producto con validaciones básicas de nombre, categoría, precio y stock.
- `modelos/usuario.py`: representa a un usuario con nombre de acceso y contraseña.
- `servicios/archivo_servicio.py`: lee los archivos JSON y reconstruye objetos a partir de los registros.
- `servicios/restaurante_servicio.py`: centraliza la lógica de validación y consulta de usuarios y productos.
- `ui/login_view.py`: permite iniciar sesión con credenciales.
- `ui/main_view.py`: muestra un panel principal con tablas y resumen de datos.
- `main.py`: inicializa la aplicación y controla la navegación entre pantallas.

## Ejecución

Desde la carpeta `PARCIAL 2/SEMANA 14`:

```bash
python -m restaurante_app.main
```

También se puede ejecutar desde la propia carpeta del proyecto:

```bash
cd restaurante_app
python main.py
```

## Resultado esperado

Al iniciar la aplicación, el usuario debe ingresar credenciales válidas para acceder al panel principal, donde puede consultar productos y usuarios cargados desde los archivos JSON del proyecto.
