# Generar el cuadrado de los 9 primeros números naturales
for i in range(1,10):
    print(i**2, "\t", end="")

print(" ")

# Calcula el cuadrado de los primeros números hasta 
# un número de dos cifras aleatorio natural.
# mínima cifra es 10 y la máxima 99
import random
numero = random.randint(10,99) # mínimo 10 y máximo 99
print("El número aleatorio es: ", numero)
for i in range(1,numero+1):
    print(i**2, "\t", end="")
