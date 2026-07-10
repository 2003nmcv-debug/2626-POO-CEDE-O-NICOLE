"""
Modelo Cliente (dataclass) - almacena datos básicos del cliente.
Ejemplo didáctico:
    c = Cliente(id_cliente='C001', nombre='Ana Pérez', correo='ana.perez@example.com')
    print(c)
"""
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str

    def __post_init__(self):
        # normalizar valores
        self.id_cliente = str(self.id_cliente).strip()
        self.nombre = str(self.nombre).strip()
        self.correo = str(self.correo).strip()
        # validación mínima de correo para fines didácticos
        if '@' not in self.correo or '.' not in self.correo:
            raise ValueError('Correo inválido para el cliente')

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente!r}, nombre={self.nombre!r}, correo={self.correo!r})"