from paquete1.modulo1 import Cliente
from paquete1.modulo2 import *

cliente1 = Cliente("Juan", "Perez", 35, "jperez@gmail.com", ["Celular", "Notebook", "Tablet"])
print(cliente1)
print(cliente1.saludar())
cliente1.comprar("Celular", "Carrefour")

print(cliente1.mostrar_preferencias())

llamado_modulo2()
