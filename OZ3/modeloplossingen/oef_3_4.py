import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Vraag de precisie aan de gebruiker (geef een niet te klein getal in).
aantal_iteraties = int(input("Geef de gewenste iteraties in: "))

# initialiseer de nodige variabelen:
pi_geschat = 0
n_in = 0
n_tot = 0

punten_binnen_x = []
punten_binnen_y = []
punten_buiten_x = []
punten_buiten_y = []

for i in range(aantal_iteraties):
    
    # de random functie geeft een willekeurig getal terug tussen [0,1]
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    
    # bereken de straal van de pool-coordinaten
    r = math.sqrt(x ** 2 + y ** 2)
    
    # indien het gegenereerde punt binnen de cirkel valt pas je bepaalde variabelen aan
    if r < 1:
        n_in += 1
        punten_binnen_x.append(x)
        punten_binnen_y.append(y)
    else:
        punten_buiten_x.append(x)
        punten_buiten_y.append(y)
    
    n_tot += 1
    pi_geschat = n_in / n_tot * 4

plt.figure()
plt.plot(punten_binnen_x,punten_binnen_y, '.g')
plt.plot(punten_buiten_x,punten_buiten_y, '.r')


# plot cirkel:
x_cir = []
y_cir = []

# range van floats kan met arange
for i in np.arange(0, 2*math.pi, 0.01):
    x_cir.append(math.cos(i))
    y_cir.append(math.sin(i))

# alternatief:
angle = 0
while angle < 2*math.pi:
    x_cir.append(math.cos(angle))
    y_cir.append(math.sin(angle))
    angle += 0.01


plt.plot(x_cir, y_cir,'-k')

