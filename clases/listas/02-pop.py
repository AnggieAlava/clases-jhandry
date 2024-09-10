# Este metodo elimina el ultimo elemento de una lista
# pero te permite trabajar con ese elemento eliminado

nombres = ['anggie', 'carol', 'lucrecia']
print(nombres)

elemento_eliminado = nombres.pop()

print(elemento_eliminado)

# Tambien se puede usar el metodo pop para eliminar un item de cualquier posicion 
# especificando el index

objetos = ['lapiz', 'pluma', 'borrador']
print(objetos)
popped_item = objetos.pop(0)
print(popped_item)