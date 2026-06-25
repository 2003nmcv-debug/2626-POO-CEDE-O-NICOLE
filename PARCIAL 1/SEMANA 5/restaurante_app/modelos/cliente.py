"""
Módulo que define la clase Cliente.
Representa una persona registrada en el sistema del restaurante.
"""


class Cliente:
    """
    Clase que representa un cliente del restaurante.
    
    Atributos:
        id_cliente (int): Identificador único del cliente
        nombre (str): Nombre completo del cliente
        email (str): Correo electrónico del cliente
        telefono (str): Número de teléfono del cliente
        miembro_premium (bool): Indica si el cliente es miembro premium
    """
    
    def __init__(
        self, 
        id_cliente: int, 
        nombre: str, 
        email: str, 
        telefono: str, 
        miembro_premium: bool = False
    ) -> None:
        """
        Inicializa un nuevo cliente con los datos proporcionados.
        
        Args:
            id_cliente: Identificador único del cliente
            nombre: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono (formato flexible)
            miembro_premium: Indica si tiene membresía premium (por defecto False)
        """
        self.id_cliente: int = id_cliente
        self.nombre: str = nombre
        self.email: str = email
        self.telefono: str = telefono
        self.miembro_premium: bool = miembro_premium
    
    def __str__(self) -> str:
        """Retorna una representación legible del cliente."""
        tipo_miembro: str = "Premium" if self.miembro_premium else "Regular"
        return (
            f"[ID: {self.id_cliente}] {self.nombre}\n"
            f"  Email: {self.email}\n"
            f"  Teléfono: {self.telefono}\n"
            f"  Tipo de membresía: {tipo_miembro}"
        )
    
    def cambiar_estado_premium(self, es_premium: bool) -> None:
        """
        Cambia el estado de membresía premium del cliente.
        
        Args:
            es_premium: Nuevo estado de membresía premium (True/False)
        """
        self.miembro_premium = es_premium
    
    def obtener_informacion_corta(self) -> str:
        """Retorna una representación breve del cliente."""
        tipo: str = "(Premium)" if self.miembro_premium else "(Regular)"
        return f"{self.nombre} {tipo}"
