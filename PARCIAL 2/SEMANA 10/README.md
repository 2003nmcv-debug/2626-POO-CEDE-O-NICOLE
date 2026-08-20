# Semana 10 - restaurante_app

## Estudiante
- Nombre completo: **Nicole Micaela Cedeño Vizhñay**

## Descripcion breve
Sistema de consola para administrar productos y usuarios de un restaurante.
En esta semana se incorporo persistencia JSON para los productos, manteniendo el trabajo con objetos `Producto` durante toda la ejecucion.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
└── main.py
README.md
```

## Responsabilidad de cada componente
- `modelos/producto.py`: valida y representa cada producto; ademas puede convertirse a diccionario y reconstruirse desde JSON.
- `modelos/usuario.py`: conserva la entidad Usuario en memoria.
- `servicios/restaurante.py`: administra las colecciones y las operaciones de negocio.
- `servicios/archivo_servicio.py`: centraliza la lectura y escritura de `datos/productos.json`.
- `main.py`: carga los productos al iniciar, coordina el menu y solicita el guardado despues de registrar, actualizar o eliminar productos.

## Funcionamiento de la persistencia
1. Al iniciar la aplicacion, `ArchivoServicio` intenta leer `datos/productos.json`.
2. Si el archivo no existe, el sistema arranca con una lista vacia.
3. Si el contenido no es JSON valido, tambien se inicia sin detener el programa.
4. Cada registro valido del archivo se convierte nuevamente en `Producto`.
5. Cuando un producto se registra, actualiza o elimina correctamente, el archivo se reescribe con `json.dump()`.

## Excepciones controladas
- `FileNotFoundError`: permite el primer inicio sin archivo.
- `json.JSONDecodeError`: controla contenido JSON invalido.
- `PermissionError`: cubre problemas de lectura o escritura.
- `KeyError`: se usa al reconstruir productos incompletos desde JSON.
- `ValueError`: mantiene las validaciones de `Producto` y controla datos invalidos.

## Ejecucion
Desde la carpeta `SEMANA 10`:

```bash
python -m restaurante_app.main
```

## Comprobacion de persistencia
- Se registro un producto.
- Se verifico que quedara guardado en `datos/productos.json`.
- Se cerro el programa y se volvio a ejecutar.
- Se confirmo que el producto seguia disponible en el listado.
- Luego se actualizo y elimino un producto, y el reinicio posterior conservo esos cambios.

