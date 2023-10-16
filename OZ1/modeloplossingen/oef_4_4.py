# Lees een getal in
getal = float(input("Geef een float in: "))

# We gaan niet alle mogelijke gevallen uitschrijven, het zijn er teveel
# Wel gaan we de boodschap slim opbouwen, en op het einde slechts 1 print statement schrijven
boodschap = "Dit getal is "

if (getal == 0):
    # nul? Dan zijn we snel klaar:
    boodschap += "nul."
else:
    # niet nul? Dan moeten we meer testen

    # Er komt sowieso al 'een' bij de boodschap
    boodschap = boodschap + "een "

    # 'klein' of 'groot' toevoegen?
    if (abs(getal) < 1):
        boodschap += "klein "
    elif (abs(getal) > 1000000):
        boodschap += "groot "
    # (geen else tak meer hier)

    # 'postief' of 'negatief'?
    if (getal > 0):
        boodschap += "positief "
    else:
        boodschap += "negatief "

    # Eindigen doen we sowieso met 'getal.'
    boodschap += "getal."

# En afdrukken maar...
print(boodschap)