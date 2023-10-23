
getal = int(input("Geef een getal in: "))

is_priem = True

for i in range(2, getal/2): # eventueel kan je slechts lopen tot int(getal/2)
    # Controlleer voor alle getallen of ze een deler zijn
    if getal % i == 0:
        is_priem = False
        # Aangezien een deler is gevonden hoeven we niet verder meer te controleren
        break

if is_priem:
    print(f"Getal {getal} is EEN priem getal")
else:
    print(f"Getal {getal} is GEEN priem getal")


