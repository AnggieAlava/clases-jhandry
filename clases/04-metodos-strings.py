# Asigna una cadena de texto a la variable 'animal'
animal = '  puerquito GRITON  '

# Convierte toda la cadena a mayúsculas y la imprime
print(animal.upper())  # Output: '  PUERQUITO GRITON  '

# Convierte toda la cadena a minúsculas y la imprime
print(animal.lower())  # Output: '  puerquito griton  '

# Elimina espacios en blanco al inicio y al final, y convierte la primera letra a mayúscula
print(animal.strip().capitalize())  # Output: 'Puerquito griton'

# Convierte la primera letra de cada palabra a mayúscula y el resto a minúsculas
print(animal.title())  # Output: '  Puerquito Griton  '

# Elimina espacios en blanco al inicio y al final de la cadena
print(animal.strip())  # Output: 'puerquito GRITON'

# Elimina espacios en blanco al inicio de la cadena
print(animal.lstrip())  # Output: 'puerquito GRITON  '

# Elimina espacios en blanco al final de la cadena
print(animal.rstrip())  # Output: '  puerquito GRITON'

# Busca la subcadena 'to' dentro de la cadena y devuelve la posición (INDICE)
print(animal.find("to"))  # Output: 11

# -1 significa no lo encontre
print(animal.find("sol"))  # Output: -1

# Reemplaza los caracteres que le pases en el primer string por los que indicas en el segundo
print(animal.replace('qui', 'mi'))  # Output: Puermito GRITON

# Te devuelve un boolean indicando si es true o false dependiendo los argumentos que pases
print("pu" in animal)

# verifica si no se encuentra
print("pu" not in animal)
