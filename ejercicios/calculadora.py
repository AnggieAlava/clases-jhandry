print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese numero:")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operacion: ")