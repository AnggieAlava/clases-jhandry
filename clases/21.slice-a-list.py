setup = ['plumas' , 'monitores', 'camara', 'lampara']
for item in setup[1:]:
    print(item.title())


# Copiar una lista es simplement usar el metodo slice sin indicar el inicio ni el final

new_setup = setup[:]
print(new_setup)
