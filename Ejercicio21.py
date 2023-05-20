'''
Calcula la suma de los N primeros números pares
 a partir del nro. ingresado.  
Example 1:
	input		: 5
	proceso		: 6+8+10+12+14
	output		: 50
Example 2:
	input		: 4
	proceso		: 4 + 6 + 8 + 10
			output		: 28
'''
nro = int(input("Ingresa un número -> "))
cantidad, contador, suma = nro , 1, 0
if nro%2 != 0:  # Me aseguro que sea un número par
    nro = nro + 1
while contador <= cantidad:
    print(nro, "\t", end="")
    suma += nro
    nro += 2   # nro = nro + 2
    contador += 1   # contador = contador + 1   
print("La suma es: ", suma)   
