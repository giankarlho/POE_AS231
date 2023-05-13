# Visualice la cuenta de los múltiplos de 2 o de 3 que hay entre 1 y 100.
contador = 0
for i in range(1,101):
    if i % 2 == 0 or i % 3 == 0:
        contador+=1 # contador = contador + 1
print("El total de múltiplos de 2 o 3 entre 1 y 100 es: ", contador)
