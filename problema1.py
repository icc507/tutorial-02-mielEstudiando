#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
lista1 = input().split()
lista2 = input().split()
for i in range(len(lista1)):
    try:
        lista1[i]=int(lista1[i])
    except ValueError:
        exit
for i in range(len(lista2)):
    try:
        lista2[i]=int(lista2[i])
    except ValueError:
        exit
t = tuple(lista1)
m = tuple(lista2)
print(m+t+m)