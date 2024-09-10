squares = []

for n in range(1,11):
    squares.append(n ** 2)

print(squares)

# Version con comprension de listas

squares_two = [number ** 2 for number in range(1,10)]
print(f"Esta es la lista en compresion de listas: \n{squares_two}")
