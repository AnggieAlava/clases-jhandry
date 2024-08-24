import random

# definir tres variables que contendran los caracteres que queremos en nuestra contrasena 
uno = ['!', '@'] # si es tipo 1 escogemos simbolos
dos = ['0', '1', '2'] # si es tipo 2 escogemos numero
tres = ['a', 'e', 'i', 'o', 'u']  # <= Iterare sobre este conjunto para extraer cada caracter 

# Iterar = Recorrer y obtener informacion de un conjunto de datos 

def generar_contrasena(longitud): # Declarar una funcion => Usa la palabra reservada "def"
    contrasena = "" # declaro una variable vacia aqui guardaremos la combinacion de los caracteres (total 6)

    for dato in range(longitud): # itero la longitud sera definida por el usuario

        tipo = random.randint(1,3) #1 es simbolos, 2 va a ser numeros, y 3 va a ser letras

        if tipo == 1:
            contrasena  += random.choice(uno)
        elif tipo == 2:
            contrasena += random.choice(dos)
        elif tipo == 3:
            contrasena += random.choice(tres)

    return contrasena


longitud = int(input("Cuantos caracteres quieres que tenga la contrasena? "))

print("Tu contrasena es la siguiente:", generar_contrasena(longitud))



