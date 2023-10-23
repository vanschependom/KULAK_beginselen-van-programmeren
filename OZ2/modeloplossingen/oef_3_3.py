import math

grenswaarde = float(input('Geef een grenswaarde in: '))
x = float(input('Geef een waarde in voor x: '))
ex = 1
n = 1

while True:
    volgende_term = x**n/math.factorial(n)
    ex += volgende_term
    
    if volgende_term < grenswaarde:
        break
        
    n += 1

print(f"e^x = {ex}, voor {n} termen")
print(f"with math module: {math.e**x}")