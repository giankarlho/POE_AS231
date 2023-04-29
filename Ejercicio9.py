'''
Una tienda hace un descuento de $10 si el total de la compra entre $100 y $200,
Hace un descuento de $20 si el total de la compra es > $200.
Si la compra es menor de $100, no hay descuento. 
El algoritmo debe calcular el precio a pagar, basado en el valor de la compra.

'''

compra = float(input("Ing. el valor de compra"))
valor = 0

if compra >= 100 and compra <= 200:
    valor = compra - 10
elif compra > 200:
    valor = compra - 20
else:
    valor = compra
print("El valor de la compra es: ", valor)