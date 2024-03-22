#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
def arbolTernario(numero):
	return [numero, [], [], []]

def insertaEnArbolTernario(arbol,numero):
	if arbol==[]:
		arbol+=arbolTernario(numero)
	elif numero < arbol[0]:
		insertaEnArbolTernario(arbol[1],numero)
	elif numero == arbol[0]:
		insertaEnArbolTernario(arbol[2],numero)
	else:
		insertaEnArbolTernario(arbol[3],numero)

t = input().split()
try:
	for num in range(len(t)):
		t[num]=int(t[num])
	arbolito=arbolTernario(t[0])
	for num in t[1:-1]:
		insertaEnArbolTernario(arbolito,num)
	print(arbolito)
except ValueError:
	print()

