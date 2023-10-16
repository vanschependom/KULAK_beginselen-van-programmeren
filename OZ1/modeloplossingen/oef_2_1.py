
# Vraag start en duurtijd voor de twee afspraken aan de gebruiker

afspr1_start = float(input("Geef de starttijd van de eerste afspraak in: "))
afspr1_duur = float(input("Geef de duurtijd van de eerste afspraak in: "))
afspr2_start = float(input("Geef de starttijd van de tweede afspraak in: "))
afspr2_duur = float(input("Geef de duurtijd van de tweede afspraak in: "))


# Indien de tweede afspaak vroeger start dan de eerste
# wisselen we de twee afspraken van variabele
# Zo is afspraak 1 gegarandeerd de eerste

if afspr1_start > afspr2_start:
    # sla de starttijd van de 2e afspraak op in een tijdelijke variabele
    # zodat de variabele kan overschreven worden
    tmp = afspr2_start
    afspr2_start = afspr1_start
    afspr1_start = tmp
    
    tmp = afspr2_duur
    afspr2_duur = afspr1_duur
    afspr1_duur = tmp

if afspr1_start + afspr1_duur > afspr2_start:
    print("De twee afspraken overlappen!")
else:
    print("De afspraken werden correct ingepland")

