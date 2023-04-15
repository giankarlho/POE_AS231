'''
Dadas dos variables numéricas A y B, que el usuario debe teclear,
se pide realizar un algoritmo que intercambie los valores de ambas
variables y muestre cuánto valen al final las dos variables.
'''

variableA = int(input("Ingresa el primer valor"))
variableB = int(input("Ingresa el segundo valor"))

auxiliar = variableA
variableA = variableB
variableB = auxiliar

print("El valor de A es: ", variableA)
print("El valor de B es: ", variableB)





