# Clase Cliente - Sistema de Gestión de Restaurante

class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Atributos:
        nombre (str): El nombre completo del cliente
        numero_telefono (str): Teléfono de contacto del cliente
        numero_documento (str): Número de identificación del cliente
        es_miembro_vip (bool): Indica si el cliente es miembro VIP

    Métodos:
        registrar_cliente(): Retorna un mensaje informando el registro
        aplicar_descuento_vip(): Calcula un descuento si es miembro VIP
        obtener_info(): Retorna la información del cliente
    """

    def __init__(self, nombre, numero_telefono, numero_documento, es_miembro_vip=False):
        """
        Constructor de la clase Cliente.

        Args:
            nombre (str): El nombre completo del cliente
            numero_telefono (str): Teléfono del cliente
            numero_documento (str): Número de documento de identidad
            es_miembro_vip (bool): Si es cliente VIP (por defecto False)
        """
        self.nombre = nombre
        self.numero_telefono = numero_telefono
        self.numero_documento = numero_documento
        self.es_miembro_vip = es_miembro_vip

    def registrar_cliente(self):
        """
        Retorna un mensaje de registro exitoso del cliente.

        Returns:
            str: Mensaje de confirmación del registro
        """
        return f"Cliente {self.nombre} registrado correctamente en el sistema."

    def aplicar_descuento_vip(self, monto_original):
        """
        Calcula el descuento VIP si el cliente tiene ese beneficio.

        Args:
            monto_original (float): El monto total antes del descuento

        Returns:
            float: El monto con descuento aplicado si es VIP, sino retorna el monto original
        """
        if self.es_miembro_vip:
            descuento = monto_original * 0.10  # Descuento del 10% para VIP
            return monto_original - descuento
        return monto_original

    def obtener_info(self):
        """
        Retorna la información del cliente de forma estructurada.

        Returns:
            str: Información formateada del cliente
        """
        estado_vip = "VIP" if self.es_miembro_vip else "Regular"
        return f"{self.nombre} ({estado_vip}) - Doc: {self.numero_documento} - Tel: {self.numero_telefono}"

    def __str__(self):
        """
        Representación en texto del cliente.
        Se ejecuta cuando se imprime el objeto.
        """
        return self.obtener_info()

