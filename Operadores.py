nro1 = int(input("Ingresa el nro1"))
nro2 = int(input("Ingresa el sgte. nro."))
texto = input("Ingresa tu nombre")

# Cálculos acumulados

nro1 +=nro1     # nro1 = nro1 + nro1
print("Acumulado suma: ", nro1)

nro2 -=2		# nro2 = nro2 - 2
print("Acumulado resta: ", nro2)

nro1 *=3		# nro1 = nro1 * 3
print("Acumulado producto *3: ", nro1)


# Calculos con texto
print("La multiplicación en cadena: ", nro1 * texto)

# Cálculos básicos
print("La suma: ", nro1 + nro2)
print("La resta: ", nro1 - nro2)
print("La multiplicación: ", nro1 * nro2)
print("La división: ", nro1 / nro2)
print("La división exacta: ", nro1//nro2)
print("La potencia: ", nro1**nro2)





