"""
    @Pc
    Ejemplo de manejo de paquetes
"""
#.
# Valor 2 elevado a la potencia 2 es igual a 4

# llamada de valores de la clase informacion del paquete1
from paquete1.informacion import valores
from paquete1.informacion2 import hacer_potencia

# para dar valores al metodo hacer_potencia en la clase informacion2
# se imprime los valotres
for l in valores:
	r = hacer_potencia(l, 2)
	print("Valor %d elevado a la potencia %d"
		" es igual a %.1f" % (l, 2, r))
