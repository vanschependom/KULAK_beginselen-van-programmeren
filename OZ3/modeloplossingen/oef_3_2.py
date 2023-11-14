
scoreAantallen = {"A":8, "B":13,"D":3, "F":2, "C":6}

for key in scoreAantallen:
    print(key)
    
for value in scoreAantallen.values():
    print(value)
    
for item in scoreAantallen.items():
    # geeft een tuple terug van (key, value)
    key = item[0]
    value = item[1]
    
    print(key, value)

# geeft een lijst van gestorteerde keys terug.
scoreAantallenSorted = sorted(scoreAantallen)

for key in scoreAantallenSorted:
    print(f"{key}: " + "*" * scoreAantallen[key])
    
    