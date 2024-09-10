cars = ['bmw', 'audi', 'toyota', 'subaru']

# Este metodo cambia el orden de la lista de forma ascendente y permanente
""" cars.sort()
print(cars) """

# Este metodo cambia el orden de la lista de forma descendente y permanente
""" cars.sort(reverse=True)
print(cars)
 """
# Este metodo cambia el orden de la lista pero no afecta el orden original

print(f"Este es la lista original: \n{cars}")
print(f"\nEsta es la lista con el metodo sorted(): \n{sorted(cars)}")
cars.reverse()
print(f"\nEsta es la lista con el metodo reverse(): \n{cars}")
