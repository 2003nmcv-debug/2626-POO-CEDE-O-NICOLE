# Restaurante App

Aplicacion grafica inicial para el restaurante, inspirada en la organizacion del proyecto docente de la Semana 13. Mantiene la separacion entre modelos, servicios, datos y vistas para que la interfaz no quede concentrada en un solo archivo.

## Estructura

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

## Propósito

- `Producto` representa los productos del restaurante.
- `Usuario` representa los usuarios de acceso simulado.
- `ArchivoServicio` lee la informacion local desde JSON.
- `RestauranteServicio` valida el acceso y entrega usuarios y productos.
- `LoginView` muestra la pantalla de ingreso.
- `MainView` muestra el panel principal con productos, usuarios y una seccion pendiente para futuras funciones.

## Ejecucion

Desde la raiz del repositorio:

```bash
python -m restaurante_app.main
```

O, si se trabaja dentro de la carpeta del proyecto:

```bash
cd restaurante_app
python main.py
```

