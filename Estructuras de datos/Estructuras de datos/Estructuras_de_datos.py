# Bienvenida.

print("Hola bienvenidos")

#Ingreso de datos1.
a = int(input("Ingrese un numero numero"))
b = int(input("Ingrese un numero numero"))
c = int(input("Ingrese un numero numero"))
d = int(input("Ingrese un numero numero"))
e = int(input("Ingrese un numero numero"))


#ingreso de lista1
lista1 = [a,b,c,d,e]

#Mensaje
print()

print("El primer listado seria: ", lista1)

print("El listado ordenado seria: ",sorted(lista1, reverse=True))

#Ingreso de datos2.
f = int(input("Ingrese un numero numero"))
g = int(input("Ingrese un numero numero"))
h = int(input("Ingrese un numero numero"))
i = int(input("Ingrese un numero numero"))
j = int(input("Ingrese un numero numero"))

#ingreso de lista2
lista2 = [f,g,h,i,j]

#mensaje
print()
print("El segundo listado seria: ", lista2)
print("El listado ordenado seria: ",sorted(lista2, reverse=True))

#Marge de listas
general = (lista1 + lista2)

#Impresion final
print(("El conjunto ordenado general seria"), sorted(general, reverse=True))
