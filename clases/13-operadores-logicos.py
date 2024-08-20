""" Los operadores logicos son:
And => &  =>  Aqui evaluaremos dos condiciones por ejemplo, si es mayor de edad y es mujer (Ambas condiciones deben cumplirse para ejecutar el codigo despues de esta condicion)

Or => |  => Evalua dos condiciones, siendo necesario que al menos una de las dos sea verdadero para que esta porcion de codigo se ejeecute, sin embargo si de las dos opciones de la condicion de OR son evaluadas como falso entonces devolvera un FALSE

Not !

"""

gasolina = True
encendido = False
edad = 18

if (gasolina or encendido) and edad >= 18:
    print("Puedes avanzar pues si tienes gasolina y el carro esta encendido")
