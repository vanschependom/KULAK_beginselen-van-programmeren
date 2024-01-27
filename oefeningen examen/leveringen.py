leveringen = [
    ["Meskens", 10, 30],
    ["Jorissen", 10, 50],
    ["Pieters", 13, 00],
    ["Janssens", 14, 00]
]

reistijden = [
    [0, 120, 20, 5, 10],
    [120, 0, 15, 20, 3],
    [20, 15, 0, 10, 10],
    [5, 20, 10, 0, 37],
    [10, 3, 10, 37, 0]
]


def maxPakjes(leveringen, reistijden, volgorde=[1, 2, 3, 4]):

    # Initialiseer de tijd
    tijd = 8 * 60
    # Inladen
    tijd += len(leveringen)*2

    # Startpositie
    positie = 0

    # In deze lijst wordt bijgehouden welke levering op tijd waren en op welk uur ze geleverd zijn
    opTijd = list()

    # Loop over de leveringen
    for i, levering in enumerate(leveringen):

        # Pas de tijd aan
        tijd += reistijden[positie][volgorde[i]]
        tijd += 5

        # Als het pakje op tijd was, voeg het toe aan de lijst opTijd
        if tijd <= levering[1] * 60 + levering[2]:
            opTijd.append((levering[0], tijd//60, tijd % 60))

        # Pas de positie aan
        positie = volgorde[i]

    # We keren terug naar het depot
    tijd += reistijden[positie][0]

    # Return welke leveringen op tijd waren en wat de totale tijd in minuten was
    return opTijd, tijd


# Recusieve functie om de permutaties van alle volgordes genereert waarin de stops kunnen overlopen worden
def volgordes(stops):

    # Triviaal geval
    if len(stops) == 1:

        return [stops]

    output = []

    # Verwijder telkens 1 van de stops
    # Genereer kortere volgordes
    # Voeg de stop + de kortere volgorde toe aan de output
    for stop in stops:

        minderStops = list(stops)
        minderStops.remove(stop)

        kleinereVolgordes = volgordes(minderStops)

        for kleinereVolgorde in kleinereVolgordes:

            nieuweVolgorde = [stop]
            nieuweVolgorde.extend(kleinereVolgorde)
            output.append(nieuweVolgorde)

    return output


# Alle stops die moeten gedaan worden
stops = [1, 2, 3, 4]

# Haal alle mogelijek permutaties van de stops op
alleVolgordes = volgordes(stops)


def getBesteVolgorde(mogelijkeVolgordes, leveringen, reistijden):

    maxLeveringen = 0

    # Overloop elke volgorde
    for mogelijkeVolgorde in mogelijkeVolgordes:

        # Haal op welke pakjes op tijd waren voor deze volgorde
        # Haal ook op wat de totale tijd van de levering was
        opTijd, tijd = maxPakjes(leveringen, reistijden, mogelijkeVolgorde)

        # Als het aantal op tijd geleverde pakjes groter is dan het huidig aantal max geleverde pakjes, pas aan
        if len(opTijd) > maxLeveringen:
            maxLeveringen = len(opTijd)
            besteVolgorde = mogelijkeVolgorde
            kortsteTijd = tijd

        # Als het aantal geleverde pakjes gelijk is, kijk of de tijd korter is dan de tot nu toe korstste
        if len(opTijd) == maxLeveringen and tijd <= kortsteTijd:
            besteVolgorde = mogelijkeVolgorde
            kortsteTijd = tijd

    # Return
    return maxLeveringen, kortsteTijd, besteVolgorde


print(getBesteVolgorde(alleVolgordes, leveringen, reistijden))
