"""
Clase Producto: representa un producto del restaurante.
Incluye validaciones mediante @property y @setter.

Ejemplo didáctico:
    p = Producto('Lomo Saltado', 'Plato principal', 25.50)
    print(p.mostrar_informacion())
"""

class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # atributos privados para controlar acceso mediante properties
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = None

        # usar setters para aplicar validaciones
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        """Nombre del producto (no vacío)."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        self._nombre = value.strip()

    @property
    def categoria(self):
        """Categoría del producto (no vacía)."""
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("La categoría del producto no puede estar vacía")
        self._categoria = value.strip()

    @property
    def precio(self):
        """Precio del producto (float > 0)."""
        return self._precio

    @precio.setter
    def precio(self, value):
        try:
            v = float(value)
        except Exception:
            raise ValueError("El precio debe ser un número")
        if v <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        self._precio = v

    @property
    def disponible(self):
        """Indica si el producto está disponible (bool)."""
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        if not isinstance(value, bool):
            raise ValueError("Disponible debe ser True o False")
        self._disponible = value

    def mostrar_informacion(self):
        """Devuelve una representación legible del producto."""
        disponibilidad = "Sí" if self.disponible else "No"
        return f"Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: S/.{self.precio:.2f} | Disponible: {disponibilidad}"

    def __repr__(self):
        return f"Producto(nombre={self.nombre!r}, categoria={self.categoria!r}, precio={self.precio!r}, disponible={self.disponible!r})"