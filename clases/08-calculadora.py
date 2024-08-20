# "input" es un metodo de python que nos permite obtener datos del usuario por medio de la terminal
primer_numero = input("Ingresa primer numero:")
segundo_numero = input("Ingresa un segundo numero:")

primer_numero = int(primer_numero)
segundo_numero = int(segundo_numero)

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multi = primer_numero * segundo_numero
divi = primer_numero / segundo_numero


mensaje = f"""
Para los numeros {primer_numero} y {segundo_numero},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicación es {multi}
y el resultado de la división es {divi}
"""

print(mensaje)
