
is_null = False
index = 0
som = 0
str_output = ''

while not is_null:
    getal = int(input("Geef een getal in: "))
    if getal == 0:
        is_null = True
    else:
        # afhankelijk van de index wordt het getal opgetelt of afgetrokken
        som += (-1) ** index * getal
        # logica voor het aanmaken van de output string
        if index % 2 == 0:
            if index == 0:
                str_output += f"{getal}"
            else:
                str_output += f" + {getal}"
        else:
            str_output += f" - {getal}"
    index += 1

print(f"{str_output} = {som}")
