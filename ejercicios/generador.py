import random

# definir tres variables que contendran los caracteres que queremos en nuestra contrasena 
simbolos = ['!', '@'] # si es tipo 1 escogemos simbolos
numeros = ['0', '1', '2'] # si es tipo 2 escogemos numero
letras = ['a', 'e', 'i', 'o', 'u']  # <= Iterare sobre este conjunto para extraer cada caracter 

# Iterar = Recorrer y obtener informacion de un conjunto de datos 


def generar_contrasena(): # Declarar una funcion => Usa la palabra reservada "def"
    contrasena = "" # aqui guardaremos la combinacion de los caracteres (total 6)


    for dato in range(6): # seran 6 caracteres en cada contrasena 

        tipo = random.randint(1,3) #1 es simbolos, 2 va a ser numeros, y 3 va a ser letras

        if tipo == 1:
            contrasena  += random.choice(simbolos)
        elif tipo == 2:
            contrasena += random.choice(numeros)
        elif tipo == 3:
            contrasena += random.choice(letras)

    return contrasena


print(generar_contrasena())



