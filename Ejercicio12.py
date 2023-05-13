""" Ejercicio 12
Se quiere determinar el tipo de persona según su edad:
Si < 5 años es un bebé
Si > 5 y < 12 es un niño.
Si > 12 y < 25 es un adolescente.
Si > 25 y < 60 es adulto
Sino es adulto mayor
"""
edad = int(input("Ingresa tu edad"))
if edad < 5:
    print("Eres un bebito")
elif edad >=5 and edad <12:
    print("Eres un niño")
elif edad >=12 and edad <25:
    print("Eres un adolescente")
elif edad >= 25 and edad <60:
    print("Eres un adulto")
else:
    print("Eres un maestro roshi")