

def genereerZinnen(woordenDict, zinSkelet):
    '''
        Genereert zinnen volgens een gegeven skelet met woorden uit een gegeven dictionary
    Parameters
    ----------
    woordenDict: dict
        Dictionary waarbij de keys de woorden zijn met de values de functie
    zinSkelet: list
        Geeft de structuur van de te genereren zinnen
    Returns
    -------
    list:
        Lijst van alle gegenereerde zinnen die voldoen aan de structuur
    '''
    # Triviaal geval: een leeg skelet, oftewel een lege lijst.
    if len(zinSkelet) == 0:
        return ["."]  # Laatste karakter van de zin: het leesteken
    else:
        # Verklein probleem: genereer alle zinnen voor een kleiner zinSkelet
        kleinerZinSkelet = zinSkelet[1:]
        alleZinnenVoorKleinerSkelet = genereerZinnen(woordenDict, kleinerZinSkelet)

        # Samenvoegen: alle mogelijkheden voor het volledig skelet maken
        resultaat = []
        woordsoort = zinSkelet[0]  # gevraagde woordsoort voor de huidige locatie
        for key in woordenDict.keys():
            if woordenDict[key] == woordsoort:
                for zin in alleZinnenVoorKleinerSkelet:
                    resultaat.append(key + " " + zin)  # Zin uitbreiden met nieuwe woord
                                                       # en toevoegen aan resultaat

        return resultaat


def genereerZinnenZonderDubbels(woordenDict, zinSkelet):
    '''
        Genereert zinnen volgens een gegeven skelet met woorden uit een gegeven dictionary
    Parameters
    ----------
    woordenDict: dict
        Dictionary waarbij de keys de woorden zijn met de values de functie
    zinSkelet: list
        Geeft de structuur van de te genereren zinnen
    Returns
    -------
    list:
        Lijst van alle gegenereerde zinnen die voldoen aan de structuur
    '''
    # Triviaal geval: een leeg skelet, oftewel een lege lijst.
    if zinSkelet == []:
        return ["."]  # Laatste karakter van de zin: het leesteken
    else:
        # Verklein probleem: genereer alle zinnen voor een kleiner zinSkelet
        kleinerZinSkelet = zinSkelet[1:]
        alleZinnenVoorKleinerSkelet = genereerZinnenZonderDubbels(woordenDict, kleinerZinSkelet)

        # Samenvoegen: alle mogelijkheden voor het volledig skelet maken
        resultaat = []
        woordsoort = zinSkelet[0]  # gevraagde woordsoort voor de huidige locatie
        for key in woordenDict.keys():
            if woordenDict[key] == woordsoort:
                for zin in alleZinnenVoorKleinerSkelet:
                    if key not in zin: # als de key al niet in de zin zit:
                        resultaat.append(key + " " + zin)  # Zin uitbreiden met nieuwe woord
                        # en toevoegen aan resultaat

        return resultaat

def genereerZinnenALTERNATIEF(woordenDict, zinSkelet, metDubbels = True):
    '''
        Genereert zinnen volgens een gegeven skelet met woorden uit een gegeven dictionary
    Parameters
    ----------
    woordenDict: dict
        Dictionary waarbij de keys de woorden zijn met de values de functie
    zinSkelet: list
        Geeft de structuur van de te genereren zinnen
    metDubbels: bool:
        True indien dubbels worden toegelaten
    Returns
    -------
    list:
        Lijst van alle gegenereerde zinnen die voldoen aan de structuur
    '''
    # Triviaal geval: een leeg skelet, oftewel een lege lijst.
    if zinSkelet == []:
        return ["."]  # Laatste karakter van de zin: het leesteken
    else:
        resultaat = []
        # Bepaal de eerste woordsoort (en meteen ook hoe de rest van het skelet eruit ziet)
        eersteWoordsoort = zinSkelet[0]
        kleinerZinSkelet = zinSkelet[1:]
        # Overloop de woorden in de dictionary
        for woord in woordenDict:
            # Is het woord van het juiste type?
            if eersteWoordsoort == woordenDict[woord]:
                # Roep recursief de functie op met de rest van het skelet
                # Maar eventueel met een kleinere woordenDict!
                kleinereWoordenDict = dict(woordenDict)
                # Indien er geen dubbels mogen voorkomen wordt het woord uit de dict gehaald
                if not metDubbels:
                    kleinereWoordenDict.pop(woord)
                # Bepaal recursief de zinnen met een kleiner skelet (en evt. kleinere woordenDict)
                alleZinnenVoorKleinerSkelet = genereerZinnenALTERNATIEF(kleinereWoordenDict, kleinerZinSkelet, metDubbels)
                # Voor elke zin in het deelresultaat
                for zin in alleZinnenVoorKleinerSkelet:
                    # Plak ze aan het woord en voeg toe aan het resultaat
                    resultaat.append(woord+" "+zin)

        return resultaat

def main():
    woordenDict = {"de tafel": "substantief", "de appel": "substantief", "staat": "werkwoord", "ligt": "werkwoord",
                   "op": "voorzetsel", "naast": "voorzetsel"}
    zinSkelet = ["substantief", "werkwoord", "voorzetsel", "substantief"]
    zinnen = genereerZinnen(woordenDict, zinSkelet)
    print(zinnen)
    print()

    #Uitbreiding: zonder herhaling van woorden
    zinnenUitbreiding=genereerZinnenZonderDubbels(woordenDict,zinSkelet)
    print(zinnenUitbreiding)
    print()

    #Uitbreiding: zonder herhaling van woorden ahv extra argument voor functie
    zinnenUitbreiding=genereerZinnenALTERNATIEF(woordenDict,zinSkelet,False)
    print(zinnenUitbreiding)
    print()

main()