import math

# Vraag de cartesische coordinaten:
x = float(input("Geef x-coordinaat in: "))
y = float(input("Geef y-coordinaat in: "))

# Bereken de pool coordinaten:
r = math.sqrt(x**2 + y**2)
theta = math.atan(y/x)

# Output
print(f"De poolcoordinaten: r = {r} en theta = {theta}")

