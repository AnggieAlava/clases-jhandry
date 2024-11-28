""" Programa que convierte temperaturas de grados Celsius a Fahrenheit y viceversa. """
temperatura = float(input("Ingresa por favor un valor de temperatura en grados Celsius: " + "\n"))
fahrenheit = (temperatura * (9 / 5)) + 32
kelvin = temperatura + 273.15
print(f"La temperatura ingresada Celsius {temperatura:.2f} equivale a: \nFahrenheit: {fahrenheit:.2f} y\nKelvin: {kelvin:.2f}")
