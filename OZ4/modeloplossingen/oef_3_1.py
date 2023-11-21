def maakPiramide(hoogte, symbool = '#'):
    '''
    Deze functie maakt een piramide met een gegeven hoogte en optioneel gegeven symbool.

    Parameters
    ----------
    hoogte : int
        De hoogte van de te maken piramide.
    symbool : char
        Het optioneel geven character waaruit de piramide wordt opgebouwd.

    Returns
    -------
    string :
        De string die de piramide voorstelt
    '''
    # Maak een lege string aan voor de piramide
    piramide = ""
    # Voor elk lijnnummer (1 tem hoogte):
    for lijnnummer in range(1,hoogte+1):
        # Start met een lege lijn
        lijn = ""

        # Voeg spaties toe:
        aantalSpaties = hoogte-lijnnummer
        lijn += (' ' * aantalSpaties)

        # Voeg symbolen
        aantalSymbolen = lijnnummer*2-1
        lijn += symbool * aantalSymbolen

        # voeg toe aan de piramide
        piramide += (lijn + "\n")

    return piramide


# Main
def main():
    # Roep de functie maakPiramide op:
    print(maakPiramide(5))


# start de main
main()