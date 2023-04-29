"""
Una tienda hace un descuento de $10 si el total de 
compra es mayor a $500. Deberás calcular el precio
a pagar, basado en el valor de la compra.
"""


compra = float(input("Ing. el valor de compra"))
valor = 0

if compra > 500:
    valor = compra - 10
else:
    valor = compra
print ("El valor a pagar será: ", valor)
