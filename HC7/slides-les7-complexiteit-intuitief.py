import timeit
import itertools
import random

##
#   Eerst enkele hulpfuncties voor het visualiseren van de data.
#

def collect(statement,setup,metingen = 100, aRange = range(10,1000,100)):
    '''
    Collect voert een statement uit na een setup en meet de tijd in een aantal metingen
    Het statement is een functie waarvan de tijdscomplexiteit empirisch bepaald
    dient te worden.
    Parameters
    ----------
    statement : str
        het uit te voeren en te timen bevel.
    setup : str
        een functie die als parameter de grootte van de instantie neemt.
    metingen : int (default = 100)
        het aantal keer dat het statement bij een experiment wordt uitgevoerd.
    aRange : collection (default = range(10,1000,100)
        de verzameling van waarden voor de grootte van de instantie.
    Returns
    -------
    result : [float]
        De tijd in seconden om het statement uit te voeren, voor elke waarde in aRange.
    '''
    result = []
    for count in aRange:
        result.append(timeit.timeit(statement,setup + '(' + str(count) + ')',
                                    number = metingen, globals = globals()))
    return result

def show(title, axis, axisName, data, names,yAxis = 'Seconden'):
    '''
    Show genereeert een plot van een aantal tabellen met gegeven waarden
    Parameters
    ----------
    title : str
        Titel van de plot.
    axis : [str]
        waarden op de x-as.
    axisName : str
        naam van de x-as.
    data : [[float]]
        lijst van lijsten waarden.
    names : [str]
        lijst van namen voor de lijsten waarden.
    yAxis : str (default = 'Seconden')
        naam van de y-as.
    Returns
    -------
    None
    '''
    import matplotlib.pyplot as plt
    plt.close()
    plt.xlabel(axisName)
    plt.ylabel(yAxis)
    plt.title(title)
    for p in range(len(data)):
        plt.plot(axis, data[p], label = names[p])
    plt.legend(loc = 'upper left')
    plt.show()





#####
#   Hieronder komen de functies waarmee we zullen experimenteren.
#   (Je kan de documentatie in- en uitklappen.)
#

## Loketrijen:

def alleStringsIteratief(lengte, letters):
    '''
    Genereert alle strings (iteratief) van gegeven lengte,
    bestaande uit de gegeven letters.
    Parameters
    ----------
    lengte : int
    letters : str or [chr]
    Returns
    -------
    [str]
    '''
    result = [""]
    for i in range(lengte):
        oud = result
        result = []
        for s in oud:
            for l in letters:
                result.append(l+s)
    return result



def loketRijenNaief(lengte, a='A', b='B'):
    '''
    Genereert alle geldige loketrijen van gegeven lengte
    door alle mogelijke rijen te genereren en enkel die
    te behouden die aan de voorwaarde voldoen.
    Parameters
    ----------
    lengte : int
    a : chr
        Het character dat mensen voorstelt die met 5€ betalen.
    b : chr
        Het character dat mensen voorstelt die met 10€ betalen.
    Returns
    -------
    [str]
    '''
    # bepaal eerst alle mogelijke strings (hergebruik bestaande functie)
    mogelijkheden = alleStringsIteratief(lengte,[a,b])
    # overloop ze en houd enkel de goede strings over
    result = []
    for optie in mogelijkheden:
        # overloop de posities in de string
        # veronderstel dat alles goed is aan het begin
        goed = True
        # houd bij hoeveel a's en b's je telt
        aantalA = 0
        aantalB = 0
        for i in range(len(optie)):
            if optie[i] == a:
                aantalA += 1
            else:
                aantalB += 1
            # indien er teveel B's zijn is de string niet goed
            if aantalB > aantalA:
                goed = False
                # je kan de lus al stoppen hier om niet nodeloos verder te zoeken
                break
        if goed:
            result.append(optie)
    return result

def loketRijenNaiefSlimmer(lengte, a='A', b='B'):
    '''
    Genereert alle geldige loketrijen van gegeven lengte
    door alle mogelijke rijen te genereren en enkel die
    te behouden die aan de voorwaarde voldoen.
    Parameters
    ----------
    lengte : int
    a : chr
        Het character dat mensen voorstelt die met 5€ betalen.
    b : chr
        Het character dat mensen voorstelt die met 10€ betalen.
    Returns
    -------
    [str]
    '''
    # bepaal alle mogelijke strings via slimme en snelle python functie
    # deze functie maakt een iterator: genereert niet eerst alles in
    # 1 grote lijst, maar wel on-the-fly,
    # pas wanneer je het gebruikt in de for-loop !
    # overloop ze en houd enkel de goede strings over
    result = []
    for optie in itertools.product(a + b,repeat = lengte):
        # overloop de posities in de string
        # veronderstel dat alles goed is aan het begin
        goed = True
        # houd bij hoeveel a's en b's je telt
        aantalA = 0
        aantalB = 0
        for i in range(len(optie)):
            if optie[i] == a:
                aantalA += 1
            else:
                aantalB += 1
            # indien er teveel B's zijn is de string niet goed
            if aantalB > aantalA:
                goed = False
                # je kan de lus al stoppen hier om niet nodeloos verder te zoeken
                break
        if goed:
            result.append(optie)
    return result


def loketRijenRecursiefCount(lengte, a='A', b='B'):
    '''
    Genereert recurrsief alle geldige loketrijen van gegeven lengte
    door enkel de juiste strings aan te maken.
    Parameters
    ----------
    lengte : int
    a : chr
        Het character dat mensen voorstelt die met 5€ betalen.
    b : chr
        Het character dat mensen voorstelt die met 10€ betalen.
    Returns
    -------
    [str]
    '''
    # triviaal?
    if lengte == 0:
        return ['']
    # anders: genereer rijen van 1 korter
    # en voeg daarna a's en/of b's toe
    kortereRijen = loketRijenRecursiefCount(lengte-1)
    result = []
    for rij in kortereRijen:
        # 'A' mag altijd toegevoegd worden
        result.append(rij+a)
        # 'B' mag enkel toegevoegd worden indien
        # er reeds meer 'A's dan 'B's voorkomen
        if rij.count(a) > rij.count(b):
            result.append(rij+b)
    return result



def loketRijenRecursiefPrefix(lengte):
    '''
    Genereert alle mogelijke loketrijen (strings) met letters A en B
    en van de gegeven lengte zodat
    voor elke positie in de string geldt dat het aantal A's tot die positie
    groter of gelijk is aan het aantal B's tot die positie.
    Parameters
    ----------
    lengte: int
    Returns
    -------
    [str]
        de lijst met toegelaten loketrijen (strings)
    '''
    return loketRijenMetPrefix("",0,lengte)


def loketRijenMetPrefix(prefix,verschilAB,lengte):
    '''
    Genereert alle mogelijke loketrijen (strings) met letters A en B
    die starten met de gegeven prefix, en <lengte> langer zijn dan de prefix,
    zodat voor elke positie geldt dat het aantal A's tot die positie
    groter of gelijk is aan het aantal B's tot die positie.
    Parameters
    ----------
    prefix : str
    verschilAB : int
        het verschil tussen het aantal A's en B's in de prefix
    lengte : int
    Returns
    -------
    [str]
        de lijst met toegelaten loketrijen (strings)
    '''
    if lengte == 0:
        return [prefix]
    if verschilAB > 0:
        # dan kan er na de prefix zowel een A als een B komen
        return loketRijenMetPrefix(prefix+'A',verschilAB+1,lengte-1) + \
               loketRijenMetPrefix(prefix+'B',verschilAB-1,lengte-1)
    else:
        # dan mag er enkel een A komen na de prefix
        return loketRijenMetPrefix(prefix+'A',verschilAB+1,lengte-1)



def loketRijenIteratiefCount(lengte, a='A', b='B'):
    '''
    Iteratieve variant dat enkel de toegelaten strings berekent
    door telkens te tellen of er nog a's of b's mogen toegevoegd
    worden.
    Parameters
    ----------
    lengte : int
    a : chr
        Het character dat mensen voorstelt die met 5€ betalen.
    b : chr
        Het character dat mensen voorstelt die met 10€ betalen.
    Returns
    -------
    [str]
    '''
    result = [""]
    for i in range(lengte):
        oud = result
        result = []
        for rij in oud:
            # 'A' mag altijd toegevoegd worden
            result.append(rij+a)
            # 'B' mag enkel toegevoegd worden indien
            # er reeds meer 'A's dan 'B's voorkomen
            if rij.count(a) > rij.count(b):
                result.append(rij+b)
    return result


def loketRijenIteratiefNoCount(lengte, a='A', b='B'):
    '''
    Iteratieve variant dat enkel de toegelaten strings berekent
    zonder telkens te tellen of er nog a's of b's mogen toegevoegd
    worden. (apart bijgehouden in een lijst)
    Parameters
    ----------
    lengte : int
    a : chr
        Het character dat mensen voorstelt die met 5€ betalen.
    b : chr
        Het character dat mensen voorstelt die met 10€ betalen.
    Returns
    -------
    [str]
    '''
    result = [""]
    verschillen = [0]
    for i in range(lengte):
        oud = result
        oudeVerschillen = verschillen
        result = []
        verschillen = []
        for i in range(len(oud)):
            # 'A' mag altijd toegevoegd worden
            result.append(oud[i]+a)
            verschillen.append(oudeVerschillen[i]+1)
            # 'B' mag enkel toegevoegd worden indien
            # er reeds meer 'A's dan 'B's voorkomen
            if oudeVerschillen[i] > 0:
                result.append(oud[i]+b)
                verschillen.append(oudeVerschillen[i]-1)
    return result




### Maxima

def maximumNaief(lijst):
    grootste = lijst[0]
    for x in lijst:
        # initieel goed
        isGrootste = True
        for ander in lijst:
            if x < ander:
                isGrootste = False
        # is x het grootste?
        if isGrootste:
            grootste = x
    return grootste

def maximumViaIteratie(lijst):
    result = lijst[0]
    for l in lijst:
        if l > result:
            result = l
    return result


def maximumViaIndex(lijst):
    resultindex = 0
    for i in range(len(lijst)):
        if lijst[i] > lijst[resultindex]:
            resultindex = i
    return lijst[resultindex]


def maximumViaPython(lijst):
    return max(lijst)


### Sorteren:


def selectionSort(lijst):
    '''
    Sorteert de lijst (ter plaatse) via selection sort.
    Het algoritme kiest telkens het kleinste overgebleven element
    en plaatst het 'vooraan'.
    Parameters
    ----------
    lijst : [.]
    Returns
    -------
    [.]
    '''
    for p in range(len(lijst)):
        kleinste = p
        for s in range(p+1,len(lijst)):
            if lijst[s] < lijst[kleinste]:
                kleinste = s
        h = lijst[p]
        lijst[p] = lijst[kleinste]
        lijst[kleinste] = h
    return lijst


def quickSort(lijst):
    '''
    Overkoepelende functie die quicksort toepast.
    De bijkomende parameters worden toegevoegd voor
    oproeping van de recursieve functie.
    Parameters
    ----------
    lijst : list
        de gedeeltelijk te sorteren lijst.
    Returns
    -------
    lijst : list
        de gesorteerde lijst.
    '''
    return sorteerQuickVanTot(lijst,0,len(lijst))


def sorteerQuickVanTot(lijst, van, tot):
    '''
    Gebruik quicksort om de deelrij beginnende bij van en
    eindigende juist voor tot te sorteren
    Parameters
    ----------
    lijst : [.] : de gedeeltelijk te sorteren lijst
    van : int : eerste index van het te sorteren deel
    tot : int : één meer dan de laatste index van het te sorteren deel
    Returns
    -------
    [.]
        de gesorteerde lijst
    '''
    if van >= tot - 1:
        return lijst
    p = partition(lijst, van, tot)
    sorteerQuickVanTot(lijst, van, p)
    sorteerQuickVanTot(lijst, p+1, tot)
    return lijst


def partition(lijst, van, tot):
    '''
    Zoek voor het eerste element uit de deelrij [van:tot]
    de juiste positie en zorg ervoor dat de elementen
    kleiner voor dit element komen en de elementen groter na dit element.
    Geef na afloop de index terug van dit element dat op zijn plaats staat.
    pivot: het element dat op de juiste plaats zal worden gezet
    j: alles voor deze index is kleiner dan de pivot
    Bij de start:
        pivot is van
        j start bij van+1
    Tijdens het overlopen: (alles na de pivot)
        kom je iets tegen dat kleiner is dan de pivot?
            wissel om met wat op j staat, en schuif j 1 op naar rechts
        kom je iets tegen dat groter is dan de pivot?
            laat het staan, verander j niet
    Na het overlopen:
        alles voor j is kleiner dan de pivot
        alles vanaf j is groter dan de pivot
        wissel nu de pivot en hetgeen op plaats j-1 staat om
        nu is alles [0..j-2] kleiner dan de pivot en
        alles [j..] groter dan de pivot
        geef de plaats van de pivot terug (j-1)
    '''
    j = van + 1
    pivot = van
    for i in range(pivot + 1,tot):
        if lijst[i] < lijst[pivot]:
            h = lijst[j]
            lijst[j] = lijst[i]
            lijst[i] = h
            j += 1
    h = lijst[pivot]
    lijst[pivot] = lijst[j-1]
    lijst[j-1] = h
    return j-1

def pythonSort(lijst):
    '''
    Gebruik de ingebouwde sorteerfunctie om te sorteren.
    Werkt niet ter plaatse!
    Parameters
    ----------
    lijst : [.] : de gedeeltelijk te sorteren lijst
    Returns
    -------
    [.]
        een gesorteerde lijst met dezelfde inhoud als lijst
    '''
    return sorted(lijst)



def mergeSort(lijst):
    # Indien triviaal: geef triviale oplossing
    if len(lijst) == 1:
        return lijst
    else:
        # splits in twee helften
        midden = len(lijst)//2          # Dit is de index van het rechterdeel
        linkerhelft = lijst[:midden]    # Dit kan dus nooit leeg zijn
        rechterhelft = lijst[midden:]   # Dit ook niet

        # sorteer beide delen recursief
        linksGesorteerd = mergeSort(linkerhelft)
        rechtsGesorteerd = mergeSort(rechterhelft)

        # voeg beide gesorteerde delen samen: overloop en voeg element
        # per element toe
        gesorteerd = []
        links = 0
        rechts = 0
        # vergelijk twee elementen, tot 1 van de delen uitgeput is
        while links < len(linksGesorteerd) and rechts < len(rechtsGesorteerd):
            if linksGesorteerd[links] < rechtsGesorteerd[rechts]:
                gesorteerd.append(linksGesorteerd[links])
                links += 1
            else:
                gesorteerd.append(rechtsGesorteerd[rechts])
                rechts += 1

        # kopieer de rest van de andere deelrij
        while links < len(linksGesorteerd):
            gesorteerd.append(linksGesorteerd[links])
            links += 1
        while rechts < len(rechtsGesorteerd):
            gesorteerd.append(rechtsGesorteerd[rechts])
            rechts += 1

        # geef het resultaat terug
        return gesorteerd




##### Fibonacci

def fibonacciRecursief(n):
    if n == 1 or n == 2:
        return 1
    return fibonacciRecursief(n-2)+fibonacciRecursief(n-1)

def fibonacciIteratief(n):
    fib = 1
    fibMin1 = 1
    for i in range(3,n+1):
        som = fib+fibMin1
        fibMin1 = fib
        fib = som
    return fib







####
#   De functies die experimenten opzetten en uitvoeren
#


def setupLoket(lengte):
    '''
    Hulpfunctie om de data te verzamelen voor de loketrijen
    Geeft een nieuwe waarde aan de globale variabele l.
    Parameters
    ----------
    lengte : int
    '''
    global l
    l = lengte


def experimentLoketrijen(maximaleGrootte, stap=1, metingen = 10):
    '''
    Voert een experiment uit met de verschillende functies
    voor het loketrijen probleem.
    Parameters
    ----------
    maximaleGrootte : int
        de maximale grootte van de problemen
    stap : int
        de stap waarmee de probleemgrootte toeneemt
    metingen : int
        het aantal metingen per probleemgrootte
    '''

    # range van probleemgroottes
    r = range(0,maximaleGrootte+1,stap)
    # voer het experiment uit voor elke functie
    # en verzamel de data
    data = []
#    data.append(collect('loketRijenNaief(l)','setupLoket',metingen, r))
#    data.append(collect('loketRijenNaiefSlimmer(l)','setupLoket',metingen, r))
    data.append(collect('loketRijenRecursiefCount(l)','setupLoket',metingen, r))
    data.append(collect('loketRijenRecursiefPrefix(l)','setupLoket',metingen, r))
#    data.append(collect('loketRijenIteratiefCount(l)','setupLoket',metingen, r))
#    data.append(collect('loketRijenIteratiefNoCount(l)','setupLoket',metingen, r))

    show('Loketrijen',r,'Lengte',data,
#         ['Naief', 'NaiefSlimmer','RecursiefCount', 'RecursiefPrefix', 'IteratiefCount'])
#         ['RecursiefCount', 'RecursiefPrefix', 'IteratiefCount', 'IteratiefNoCount'])
#         ['RecursiefPrefix', 'IteratiefNoCount'])
         ['RecursiefCount', 'RecursiefPrefix'])


def setupMaximum(lengte):
    '''
    Hulpfunctie om de data te verzamelen voor de maxima
    Geeft een nieuwe waarde aan de globale variabele rij.
    Parameters
    ----------
    lengte : int
    '''
    global deLijst
    random.seed()
    deLijst = [random.randint(1,1000000) for x in range(lengte)]

def setupWorstCase(lengte):
    global deLijst
    deLijst = [x for x in range(lengte)]


def experimentMaximum(maximaleLengte, stap = 1, metingen = 10):
    '''
    Voert een experiment uit met de verschillende functies
    voor het zoeken van het maximum in een lijst.
    Parameters
    ----------
    maximaleLengte : int
        de maximale lengte van de te beschouwen lijsten
    stap : int
        de stap waarmee de probleemgrootte toeneemt
    metingen : int
        het aantal metingen per probleemgrootte
    '''

    # range van probleemgroottes
    r = range(1,maximaleLengte+1,stap)
    # voer het experiment uit voor elke functie
    # en verzamel de data
    data = []
#    data.append(collect('maximumNaief(deLijst)','setupMaximum', metingen, r))
    data.append(collect('maximumViaIteratie(deLijst)','setupMaximum', metingen, r))
    data.append(collect('maximumViaIndex(deLijst)','setupMaximum', metingen, r))
    data.append(collect('maximumViaPython(deLijst)','setupMaximum', metingen, r))

    show('Maxima',r,'Lengte',data,
#             ['Naief',"Iteratie"])
         ['Iteratie', 'Indexatie','Python'])



def experimentSorteren(maximaleLengte, stap = 1, metingen = 10):
    '''
    Voert een experiment uit met de verschillende functies
    voor het zoeken van het maximum in een lijst.
    Parameters
    ----------
    maximaleLengte : int
        de maximale lengte van de te beschouwen lijsten
    stap : int
        de stap waarmee de probleemgrootte toeneemt
    metingen : int
        het aantal metingen per probleemgrootte
    '''
    import sys
    sys.setrecursionlimit(12000)

    # range van probleemgroottes
    r = range(1,maximaleLengte+1,stap)
    # voer het experiment uit voor elke functie
    # en verzamel de data (kunnen dezelfde setup gebruiken als maxima)
    data = []
#    data.append(collect('selectionSort(deLijst)','setupMaximum', metingen, r))
    data.append(collect('quickSort(deLijst)','setupMaximum', metingen, r))
    data.append(collect('mergeSort(deLijst)','setupMaximum', metingen, r))
    data.append(collect('pythonSort(deLijst)','setupMaximum', metingen, r))

    show('Sorteren',r,'Lengte',data,
#         ['selectionSort', 'quickSort','mergeSort' ,'pythonSort'])
         ['quickSort','mergeSort' ,'pythonSort'])
#         ['mergeSort' ,'pythonSort'])
#         ['pythonSort'])

def setupFibonacci(grootte):
    '''
    Hulpfunctie om de data te verzamelen voor de loketrijen
    Geeft een nieuwe waarde aan de globale variabele l.
    Parameters
    ----------
    lengte : int
    '''
    global n
    n = grootte

def experimentFibonacci(maximaleN, stap = 1, metingen = 1):
    # range van probleemgroottes
    r = range(1,maximaleN+1,stap)
    # voer het experiment uit voor elke functie
    # en verzamel de data
    data = []
    data.append(collect('fibonacciIteratief(n)','setupFibonacci', metingen, r))
    data.append(collect('fibonacciRecursief(n)','setupFibonacci', metingen, r))

    show('Fibonacci',r,'N',data,
         ['iteratief', 'recursief'])
#         ['iteratief'])

#experimentLoketrijen(20,1,1)
#experimentLoketrijen(26,2,1)
#experimentMaximum(5000, 10, 20)
#experimentSorteren(10500, 50, 1)
experimentFibonacci(40, 1, 1)