class Cliente():

    def __init__(self, nombre, apellido, edad, email, preferencias=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__email = email
        self.__preferencias = preferencias or []

    def __str__(self):
        return f'Se ha creado el cliente {self.__nombre} {self.__apellido}.'

    def comprar(self, articulo, tienda):
        self.__articulo = articulo
        self.__tienda = tienda
        print(f'{self.__tienda} le agradece por la compra de {self.__articulo}.')
        print(f'Se le ha enviado un correo con su factura a {self.__email}')

    def saludar(self):
        return f'Hola {self.__nombre} {self.__apellido} le damos la bienvenida!'

    def mostrar_preferencias(self):
        return f'Hola {self.__nombre} {self.__apellido}, sus preferencias son: {", ".join(self.__preferencias)}'
