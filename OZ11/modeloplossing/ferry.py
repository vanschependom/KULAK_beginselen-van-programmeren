import random
import copy

def genereerWagens(n,minLengte = 2, maxLengte = 7):
    """
    genereer wagens maakt een lijst aan met de lengte van de wagens. De lengte van elke wagen is tussen 2 en 7m
    :param n: de aantal wagens die gegenereerd moeten worden
    :param minLengte: minimum lengte van de autos
    :param maxLengte: maximum lengte van de autos
    :return: lijst die de lengte van de wagens bevat.
    """
    lijst = []
    for i in range(n):
        lijst.append(random.random()*(maxLengte-minLengte)+minLengte)
    
    return lijst

def mogelijkeRijen(ferry, wagen):
    """
    functie mogelijkeRijen geeft de rijen terug die nog genoeg capciteit hebben voor de wagen aan toe te voegen.
    :param ferry: dict
    :param wagen: float
    :return: lijst met mogelijke rijen waar we de wagen aan kunnen toevoegen
    """
    output = []
    for idx,cap in enumerate(ferry['capaciteit']):
        if cap >= wagen:
            output.append(idx)
    return output
    
def genereerAlleMogelijkeOplossingen(ferry, wagens):
    """
    Recursieve functie die alle mogelijke combinaties van het orden van de wagens op een ferry genereert
    :param ferry: dict, ferry heeft een capaciteit per rij en een vracht
    :param wagens: list, lijst met de lengtes van wagens
    :return: lijst met mogelijke combinaties van het opvullen van de ferry
    """
    if len(wagens)==0 or len(mogelijkeRijen(ferry,wagens[0])) == 0:
        return [ferry]

    output = []
    keuzeRijen = mogelijkeRijen(ferry, wagens[0])
    wagensRest = wagens[1:]
    
    for rij in keuzeRijen:
        
        newFerry = copy.deepcopy(ferry)
        newFerry['capaciteit'][rij] = newFerry['capaciteit'][rij]-wagens[0]
        newFerry['vracht'][rij].append(wagens[0])
        
        oplossingen = genereerAlleMogelijkeOplossingen(newFerry,wagensRest)
        output.extend(oplossingen)
    
    return output

def selecteerOptimaleVolgorde(oplossingen):
    """
    functie zoekt tussen alle oplossingen, de oplossing met het maximaal aantal wagens.
    :param oplossingen: list, lijst met oplossingen van het ordenen van een ferry
    :return: optimaleOplossing
    """
    optimaleOplossing = 0
    maxWagens = 0
    for oplossing in oplossingen:
        aantalRijen = len(oplossing['vracht'])
        huidigAantal = 0
        for rij in range(aantalRijen):
            huidigAantal += len(oplossing['vracht'][rij])
        if huidigAantal > maxWagens:
            maxWagens = huidigAantal
            optimaleOplossing = oplossing
    return optimaleOplossing

def genereerWagenVolgorde(optimaleOplossing, wagens):
    aantalRijen = len(optimaleOplossing['vracht'])
    idxColom = [0 for i in range(aantalRijen)]
    wagenVolgorde = [[] for i in range(aantalRijen)]
    volgorde = 0
    for wagenIdx in range(len(wagens)):
        for i in range(aantalRijen):
            if len(optimaleOplossing['vracht'][i])>idxColom[i] and wagens[wagenIdx] == optimaleOplossing['vracht'][i][idxColom[i]]:
                wagenVolgorde[i].append(volgorde)
                idxColom[i] += 1
                volgorde += 1
                break
    return wagenVolgorde
        

def main():
    ferry = dict({'capaciteit':[5,7,10],'vracht':[[],[],[]]})
    wagens = genereerWagens(15,2,4)
    print('Wagens:', wagens)
    oplossingen = genereerAlleMogelijkeOplossingen(ferry, wagens)
    print(f"Aantal mogelijke oplossingen: {len(oplossingen)}")
    optimaleOplossing = selecteerOptimaleVolgorde(oplossingen)
    print(optimaleOplossing)
    wagenVolgorde = genereerWagenVolgorde(optimaleOplossing, wagens)
    lengteRijen = [len(rij) for rij in optimaleOplossing['vracht']]


print('Ferry:')
print('-' * (max(lengteRijen) * 4 + 1))
for rij in wagenVolgorde:
    rijStr = '# '
    for wagen in rij:
        rijStr += '{0} - '.format(wagen)
    rijStr = rijStr[:-3]
    rijStr += ' ' * ((max(lengteRijen) * 4) - len(rijStr)) + '#'
    print(rijStr)
print('-' * (max(lengteRijen) * 4 + 1))


main()