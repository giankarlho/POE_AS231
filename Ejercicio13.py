"""
Leer un número entero de dos dígitos distintos de uno y determinar si un dígito es múltiplo del otro.
Example 1:
	input: 68
	output: “Los números no son múltiplos”
Example 2:
	input: 39
	output: “El segundo dígito es múltiplo del primero”
Example 3:
	input: 82
	output: “El primer dígito es múltiplo del segundo”
Constraints:
	10 <= N < 100 
"""

numero = int(input("Ingresa un number"))
unidad , decena = 0 , 0
if numero >=10 and numero <=99:
    unidad = numero % 10
    decena = numero // 10
    if unidad % decena == 0:
        print("El 1er. digito es múltiplo del 2do.")
    elif decena % unidad == 0:
        print("El 2do. digito es múltiplo del 1ero.")
    else:
        print("Los dígitos no son múltiplos")
else:
    print("Invalid number")