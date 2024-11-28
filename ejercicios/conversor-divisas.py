cantidad_local = float(input("Por favor ingresa la cantidad a cambiar en tu moneda local: "))
usd = cantidad_local * 0.050
eur = cantidad_local * 0.047
gbp = cantidad_local * 0.039
jpy = cantidad_local * 7.71

result = f"USD: {usd} \nEUR: {eur} \nGBP: {gbp}  \nJPY: {jpy}"
print(result)
