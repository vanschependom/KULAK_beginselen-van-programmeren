
# Collecteer input data:
verbruik_vaatwas = 0.75     # 0.75 kWh per wasbeurt
huidige_productie = float(input("Geef de huidig productie op in kWh voor komend uur : "))
huidig_verbruik = float(input("Geef het huidig verbruik op: "))
batterij_niveau = float(input("Geef huidig batterij niveau op: "))

# Beslissingsboom voor het starten van de vaatwas
if batterij_niveau > .9:
    print("Start de vaatwas: batterij > 90%")
elif huidige_productie > .8 * verbruik_vaatwas:
    print("Start de vaatwas: productie > 80%")
elif batterij_niveau > .65 and huidige_productie > .65 * verbruik_vaatwas:
    print("Start de vaatwas: batterij > 65% en productie > 65%")
else:
    print("Waarschuwing: batterij en/of productie te laag")


