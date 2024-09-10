print("Bienvenidos a tu primera calculadora")
print("Para iniciar por favor haz correr el codigo")

while True:
    try:
        n1 = float(input('Ingrese el primer número: '))
        operacion = input('Ingrese la operación (suma, resta, multi, div): ')
        n2 = float(input('Ingrese el segundo número: '))

        if operacion == 'suma':
            resultado = n1 + n2
        elif operacion == 'resta':
            resultado = n1 - n2
        elif operacion == 'multi':
            resultado = n1 * n2
        elif operacion == 'div':
            if n2 != 0:
                resultado = n1 / n2
            else:
                print('Error: no se puede dividir por cero')
                continue

        print(f'Resultado: {resultado}')
    except ValueError:
        print('Error: entrada no válida')

    respuesta = input('¿Desea continuar? (si/no): ')
    if respuesta.lower() != 'si':
        break