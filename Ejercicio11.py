"""
Realizar un algoritmo que, 
dado un número entero, visualice en pantalla si es par o impar.
En el caso de ser 0, debe visualizar “el número no es par ni impar.
"""
nro = int(input("Ing. un número entero"))

if nro == 0:
    print("El número no es par ni impar")
elif nro % 2 == 0:
    print("El nro. es par")
else:
    print("El nro. es impar")