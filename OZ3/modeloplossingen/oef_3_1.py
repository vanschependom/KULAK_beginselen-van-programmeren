
aantal_staven = int(input("Hoeveel staven wil je maken? "))
# uitbreiding:
symbool = input("Geef een symbool mee: ")

idx = 0
lengte_van_staven = []
while idx < aantal_staven:
    lstaaf = int(input(f"Lengte van de {idx+1}e staaf: "))
    lengte_van_staven.append(lstaaf)
    idx += 1

max_lengte_staaf = max(lengte_van_staven)
for lstaaf in lengte_van_staven:
    print(symbool*int(lstaaf/max_lengte_staaf*40))
    

