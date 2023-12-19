"""
Oefening Pakjes (Examen_O_16_1_2020):

Hieronder geven we aan hoe we de verschillende elementen van de vraag modelleren.

    - Pakje: als een dictionary met als keys het verdeelcentrum en de hoogte van het pakje
    - Doos: als een dictionary met als keys het verdeelcentrum, of de doos vol is of niet, de pakjes die reeds in de
    doos zitten (gemodelleerd als een lijst van pakjes), de ondergrens en bovengrens, de hoogte van de inhoud van de
    doos.
    - Magazijn: lijst van dozen
    - Vrijwilliger: lijst van pakjes
    
"""

import random

def check_doos(doos, pakje):
    """
    Bekijkt of pakje in de doos kan, volgens de onder en bovengrenzen van de doos.
    Parameters
    ----------
    doos: dict
    pakje: dict

    Returns
    -------
    bool
        True als pakje in doos past
    """
    
    if doos['verdeelcentrum'] == pakje['verdeelcentrum'] and not doos['vol']:
        
        nieuwe_hoogte = pakje['hoogte'] + doos['huidige_hoogte']
        
        if nieuwe_hoogte < doos['ondergrens']:
            return True
        elif nieuwe_hoogte < doos["hoogte"]:
            if nieuwe_hoogte > doos['bovengrens']:
                return True
            else:
                return False
        else:
            return False
    
    else:
        return False


def voeg_pakje_toe_aan_doos(pakje, doos):
    """
    Voegt een pakje toe aan een bepaalde doos en update alle waarden van de doos
    Parameters
    ----------
    pakje: dict
    doos: dict
    """
    
    doos['pakjes'].append(pakje)
    doos['huidige_hoogte'] += pakje['hoogte']

def start_nieuwe_doos(verdeelcentrum, dooshoogte=50., ondergrens=30., bovengrens=40.):
    """
    Het aanmaken van een nieuwe doos
    Parameters
    ----------
    verdeelcentrum: str
        Naam van verdeelcentrum
    dooshoogte: float
        standaard hoogte van een doos
    ondergrens: float
        ondergrens voor het vullen van de doos
    bovengrens: float
        bovengrens voor het vullen van de doos

    Returns
    -------
    dict
        De lege doos
    """
    
    doos = {"verdeelcentrum": verdeelcentrum, "hoogte": dooshoogte, "ondergrens": ondergrens, "bovengrens": bovengrens,
            "pakjes": [], "huidige_hoogte": 0, "vol": False}
    
    return doos
    

def sorteer_pakjes(magazijn, vrijwilligers):
    """
    
    Parameters
    ----------
    magazijn: list
        lijst van dozen in het magazijn
    vrijwilligers: list
        lijst van vrijwilligers die hun pakjes vast hebben

    Returns
    -------
    list
        Gesorteerd magazijn
    """
    
    for vrijwilliger in vrijwilligers:
        for pakje in vrijwilliger:
            pakje_toegevoegd_aan_doos = False
            for doos in magazijn:
                if check_doos(doos, pakje):
                    voeg_pakje_toe_aan_doos(pakje, doos)
            if not pakje_toegevoegd_aan_doos:
                doos = start_nieuwe_doos(pakje['verdeelcentrum'])
                voeg_pakje_toe_aan_doos(pakje, doos)
                magazijn.append(doos)
            
    return magazijn

# Het modelleren van de main functie werd niet expliciet gevraagd in de opgave.
# Maar dit is handig voor het testen van je code
if __name__ == '__main__':
    magazijn = []
    verdeelcentra = ["PCtje Bissegem", "Den Bras", "De Lange Munte"]
    nmb_vrijwilligers = 9
    
    pakjes = []
    for p in range(3*nmb_vrijwilligers):
        pakjes.append({"verdeelcentrum": random.choice(verdeelcentra), "hoogte": random.random()*20+10})
    
    vrijwilligers = []
    for v in range(nmb_vrijwilligers):
        vrijwilliger = []
        for p in range(3):
            pakje = pakjes.pop()
            vrijwilliger.append(pakje)
        vrijwilligers.append(vrijwilliger)
        
    magazijn = sorteer_pakjes(magazijn, vrijwilligers)
    for doos in magazijn:
        print(f"{doos['verdeelcentrum']}")
        for pakje in doos['pakjes']:
            print(f"\t{pakje['verdeelcentrum']}: {pakje['hoogte']}")