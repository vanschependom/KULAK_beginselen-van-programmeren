
import random

x_coord = 0
y_coord = 0

for stap in range(10):
    rgetal = random.random()
    if rgetal < 0.25:
        # link
        x_coord -= 1
    elif rgetal < .5:
        # rechts
        x_coord += 1
    elif rgetal < .75:
        # boven
        y_coord += 1
    else:
        #onder
        y_coord -= 1
    print(x_coord,y_coord)


# Elegantere code:
richtingen = ['links', 'rechts', 'boven', 'onder']

for stap in range(10):
    richting = random.choice(richtingen)
    if richting == "links":
        x_coord -= 1
    elif richting == "rechts":
        x_coord += 1
    elif richting == "boven":
        y_coord += 1
    elif richting == "onder":
        y_coord -= 1
    print(x_coord,y_coord)


