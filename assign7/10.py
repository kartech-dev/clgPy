
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) +32, celsius_temps))
print(fahrenheit_temps)
above_freezing = list(filter(lambda f: f > 32, fahrenheit_temps))
print(above_freezing)
