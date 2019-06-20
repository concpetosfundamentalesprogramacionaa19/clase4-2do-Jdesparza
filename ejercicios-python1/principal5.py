"""
    @PC
    Manejo de estructuras
"""

# Mi nombre es: René y mi apellido es: Elizalde
# declaracion de diccionarios con valores cadena
diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Luis", "apellidos": "Alvarez"}
# declaracion de lista que contiene los diccionarios
lista = [diccionario, diccionario2]
# se imprime un mensaje
print("Imprimir diccionario")
# para recorrer lista e imprimir cada uno de los diccionarios
for l in lista:
	# mi diccionario va a ser igual al contador l
	midiccionario = l
	print("Mi nombre es : %s y mi apellido es: %s" %
		(diccionario["nombre"],
			diccionario["apellidos"]))


