# Semana 11 - restaurante_app

## Estudiante
- Nombre completo: **Nicole Micaela Cedeño Vizhñay**

## Descripcion breve
Aplicacion de consola para administrar productos, usuarios y ventas de un restaurante usando colecciones de objetos y persistencia JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Responsabilidad de cada componente
- `modelos/producto.py`: representa cada producto y su stock; valida datos y se convierte a JSON.
- `modelos/usuario.py`: representa a la persona registrada y su informacion basica.
- `modelos/venta.py`: representa la relacion entre usuario, producto y cantidad vendida.
- `servicios/restaurante.py`: administra colecciones, busquedas, ventas y reglas de negocio.
- `servicios/archivo_servicio.py`: carga y guarda productos, usuarios y ventas en archivos JSON.
- `main.py`: coordina el menu y solicita datos por consola sin modificar las colecciones directamente.

## Funcionamiento del stock y las ventas
Cada producto conserva un atributo `stock`. Al vender:
1. Se busca el usuario.
2. Se busca el producto.
3. Se valida que la cantidad sea mayor que cero.
4. Se verifica que exista stock suficiente.
5. Se crea una instancia `Venta`.
6. Se agrega la venta a la coleccion.
7. Se descuenta el stock del producto.
8. Se guardan `ventas.json` y `productos.json`.

## Persistencia JSON
- `productos.json`: conserva los productos y su stock.
- `usuarios.json`: conserva los usuarios registrados.
- `ventas.json`: conserva las relaciones registradas entre usuarios y productos.

Al iniciar la aplicacion, los tres archivos se leen con `json.load()` y cada registro valido se reconstruye como objeto. Si un archivo no existe, contiene JSON invalido o no se puede leer, el sistema inicia con la coleccion vacia correspondiente.

## Excepciones controladas
- `FileNotFoundError`
- `json.JSONDecodeError`
- `PermissionError`
- `KeyError`
- `ValueError`

## Ejecucion
Desde la carpeta `SEMANA 11`:

```bash
python -m restaurante_app.main
```

## Pruebas realizadas
- Registro de productos con stock.
- Registro de usuarios.
- Venta valida con descuento de stock.
- Consulta de ventas por usuario.
- Reinicio del programa para verificar recuperacion desde JSON.
- Intento de venta con stock insuficiente para confirmar rechazo.
