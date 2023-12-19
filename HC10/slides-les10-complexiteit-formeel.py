import math

###
#   Machten
#

def machtRecursief(x,n):
    if n == 0:
        return 1
    return x*machtRecursief(x,n-1)

def machtIteratief(x,n):
    r = 1
    for i in range(n):
        r *= x
    return r

def machtRecursiefTwee(x,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return machtRecursiefTwee(x*x,n//2)
    return x*machtRecursiefTwee(x,n-1)



###
#   Strings genereren
#

def alleStrings(lengte, letters = 'ab'):
    if lengte == 0:
        return [""]
    result =[]
    # Genereer eerst alle kleinere strings
    kleinereStrings = alleStrings(lengte-1,letters)
    # en kleef er overal een letter voor
    for s in kleinereStrings:
        for l in letters:
            result.append(l+s)
    return result

def alleStringsIteratief(lengte, letters):
    result = [""]
    for i in range(lengte):
        oud = result
        result = []
        for s in oud:
            for l in letters:
                result.append(l+s)
    return result


###
#   Subsetprobleem
#

def isDeellijstVanLijst(deel,lijst):
    '''
    Controleert of de elementen uit een gegeven
    deellijst allen voorkomen in de gegeven lijst
    Parameters
    ----------
    deel : [.]
    lijst : [.]
    Returns
    -------
    bool
    '''
    for x in deel:
        gevonden = False
        for element in lijst:
            if x == element:
                gevonden = True
        if not gevonden:
            return False
    return True


def isDeellijstVanGesorteerdeLijst(deel,lijst):
    '''
    Controleert of de elementen uit een gegeven
    deellijst allen voorkomen in de gegeven lijst
    Parameters
    ----------
    deel : [.]
    lijst : [.]
        Deze lijst dient gesorteerd te zijn!
    Returns
    -------
    bool
    '''
    for x in deel:
        if zoekBinair(x,lijst) == -1:
            return False
    return True

def isGesorteerdeDeellijstVanGesorteerdeLijst(deel,lijst):
    '''
    Controleert of de elementen uit een gegeven
    deellijst allen voorkomen in de gegeven lijst
    Parameters
    ----------
    deel : [.]
        Deze deellijst dient gesorteerd te zijn!
    lijst : [.]
        Deze lijst dient gesorteerd te zijn!
    Returns
    -------
    bool
    '''
    i = 0
    j = 0
    # overloop beide lijsten tegelijk met indices
    # we zoeken deel[i] in lijst en weten dat
    # beiden gesorteerd zijn
    while i < len(deel) and j < len(lijst):
        if deel[i] == lijst[j]:
            # we hebben het gevonden, verhoog beide indices
            i += 1
            j += 1
        elif deel[i] > lijst[j]:
            # lijst[j] is kleiner, als deel[i] in
            # lijst voorkomt, dan staat het verder naar rechts
            j += 1
        else:
            # we vinden een element in lijst dat groter is
            # dan wat we zoeken, gezien beiden gesorteerd
            # zijn kan wat we zoeken niet meer voorkomen!
            return False
    # als de while stopt dan is i == len(deel) of j == len(lijst)
    # als i == len(deel) dan hebben we alles gevonden uit deel en
    # is het antwoord True, anders False
    return i == len(deel)


def isGesorteerdeDeellijstVanGesorteerdeLijst2(deel,lijst):
    '''
    Controleert of de elementen uit een gegeven
    deellijst allen voorkomen in de gegeven lijst
    Parameters
    ----------
    deel : [.]
        Deze deellijst dient gesorteerd te zijn!
    lijst : [.]
        Deze lijst dient gesorteerd te zijn!
    Returns
    -------
    bool
    '''
    j = 0
    # voor elk element in deel:
    # zoek het element in lijst vanaf index j
    # kan er niet voor staan, wegens beide gesorteerd
    for x in deel:
        # verhoog j tot je x gevonden hebt
        # of tot lijst ten einde is
        while j < len(lijst) and lijst[j] != x:
            j += 1
        # is lijst ten einde, dan is x niet gevonden
        if j == len(lijst):
            return False
        # anders: controleer de volgende x
        # (onthoud waarde van j!)
    # geen enkele return False? dan zijn alle
    # elementen in deel gevonden!
    return True


def zoekBinairVanTot(x,lijst,van = 0, tot = -1):
    '''
    Controleert of het element x voorkomt in een
    gesorteerde lijst lijst, tussen de indices van en tot
    Parameters
    ----------
    x : int
        De te zoeken waarde
    lijst : [.]
        Deze lijst dient gesorteerd te zijn!
    van : int (default = 0)
        De index vanaf waar gezocht moet worden
    tot : int (default = -1)
        De index tot waar gezocht moet worden
        De default waarde is beter de lengte van de lijst, te vervangen in code
    Returns
    -------
    int
        de index van x in de lijst, als x voorkomt, anders -1
    '''
    # Vervang eerst de default tot indien nodig
    if tot == -1:
        tot = len(lijst)
    # Triviaal als er maar 1 element in de lijst zit
    if van == tot-1:
        if lijst[van] == x:
            return van
        else:
            return -1
    # bereken het midden
    midden = (van+tot)//2
    # zoek recursief in een halve lijst
    if lijst[midden] >= x:
        return zoekBinairVanTot(x,lijst, midden,tot)
    else:
        return zoekBinairVanTot(x,lijst,van,midden)
    # Merk op dat je sneller zou kunnen stoppen mocht je het gezochte element
    # toevallig ergens in een midden tegenkomen. Pas het algoritme aan als UOVT.

def zoekBinair(x,lijst):
    '''
        Controleert of het element x voorkomt in een
        gesorteerde lijst lijst (iteratief)
        Parameters
        ----------
        x : int
            De te zoeken waarde
        lijst : [.]
            Deze lijst dient gesorteerd te zijn!
        Returns
        -------
        int
            de index van x in de lijst, als x voorkomt, anders -1
        '''
    # gebruikt een totEnMet waardoor de grenzen anders worden
    van = 0
    totEnMet = len(lijst)-1
    while van < totEnMet: # als van == totEnMet hebben we het getal misschien gevonden
        midden = (van + totEnMet) // 2
        # even aantal elementen: midden = links van het exacte midden
        if x <= lijst[midden]:
            # zoek verder links (tot en met midden)
            totEnMet = midden
        else:
            # zoek verde rechts
            van = midden+1
    if x == lijst[van]:
        return van
    else:
        return -1


###
#   Maximale deelrijsom
#

def maxDeelrijSomNaief(lijst):
    maximaleSom = -math.inf
    # overloop de indices
    for i in range(len(lijst)):
        # voor elke startpositie i:
        # overloop alle eindposities j
        for j in range(i,len(lijst)):
            # bepaal de som van de elementen van i tot en met j
            som = 0
            for index in range(i,j+1):
                som += lijst[i]
            # is de som groter dan de maximale som tot dusver?
            if som > maximaleSom:
                maximaleSom = som
    # geef het antwoord terug
    return maximaleSom

def maxDeelrijSomBeter(lijst):
    maximaleSom = -math.inf
    # overloop de indices
    for i in range(len(lijst)):
        # voor elke startpositie i:
        # overloop alle eindposities j
        # en verwerk de som automatisch op basis
        # van de vorige som!
        som = 0
        for j in range(i,len(lijst)):
            som += lijst[j]
            if som > maximaleSom:
                maximaleSom = som
    # geef het antwoord terug
    return maximaleSom

def maxDeelrijSomBest(lijst):
    maximaleSom = -math.inf
    # overloop de indices
    # onthoud wat de beste rij is die
    # vlak voor i eindigt
    grootsteRijEindigendBijI = 0
    for i in range(len(lijst)):
        # voor elke eindpositie i:
        grootsteRijEindigendBijI = \
            max(0,grootsteRijEindigendBijI+lijst[i])
        if grootsteRijEindigendBijI > maximaleSom:
                maximaleSom = grootsteRijEindigendBijI
    # geef het antwoord terug
    return maximaleSom

