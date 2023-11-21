import string


def cleanWord(w):
    '''
        De functie verwijdert leestekens uit een string en zet alle hoofdletters in kleine letters.

    Parameters
    ----------
    w : string
         De op te kuisen string.

    Returns
    -------
    string
        De string zonder leestekens en hoofdletters
    '''
    return w.lower().strip(string.punctuation)


def getWoorden(zin):
    '''
        Deze functie verandert een zin in een verzameling woorden.

    Parameters
    ----------
    zin : string
        Een zin bestaande uit verschillende woorden.

    Returns
    -------
    list
        Een lijst met alle woorden uit de zin.

    '''
    woorden = set()
    for w in zin.split():
        woorden.add(cleanWord(w))
    return woorden


def leesBestand(bestandsnaam):
    '''
        Deze functie leest een bestand in en geeft een lijst met regels terug.

    Parameters
    ----------
    bestandsnaam : string
        De naam van het in te lezen bestand.

    Returns
    -------
    list
        Een lijst met de regels uit het bestand

    '''
    bestand = open(bestandsnaam,'r')
    zinnen = bestand.read().split('\n')
    bestand.close()
    return zinnen



# Hoofdprogramma
def main():
    # Maak een lijst van regels uit je bestand
    zinnen = leesBestand('oef6_tekst.txt')

    # Maak een lege woordenschat (dictionary)
    woordenschat = {}


    for zin in zinnen:
        # Vind de woorden uit de zin (in propere vorm)
        woorden = getWoorden(zin)

        # Houd bij welke woorden je toevoegt:
        nieuweWoorden = set()


        for woord in woorden:
            # Pas de woordenschat aan
            if woord in woordenschat:
                # Het woord zit er al in: dus verhoog waarde met 1
                woordenschat[woord] += 1
            else:
                # Het woord zit er nog niet in: voeg toe met waarde 1
                woordenschat[woord] = 1
                nieuweWoorden.add(woord)

        # Print info over de verwerkte zin:
        print("Verwerkte zin: '" + zin + "'")
        # Print de grootte van de nieuwe woordenschat
        print("Grootte van de nieuwe woordenschat: " + str(len(woordenschat)))
        # Print de nieuwe woorden
        print("Nieuwe woorden toegevoegd: " + str(nieuweWoorden))


    print("KLAAR")
    # Print nu de woorden af die in meer dan 50% van de zinnen voorkomen:
    print("Woorden die in meer dan 50% van de zinnen voorkomen:")


    for woord, frequentie in woordenschat.items():
        # komt het woord in meer dan 50% van de regels voor?
        if frequentie / len(zinnen) > 0.5:
            # druk het dan af:
            print(woord, end=" ")


# start de main
main()