import random
# Opmerking: je kan in PyCharm makkelijk de lijncomments verwijderen via
# het menu Code/Comment with line comment...


def nim(spelers, minStapels, maxStapels, minLucifers, maxLucifers):
    '''
    Speel het spel nim, gegeven de parameters.
    Parameters
    ----------
    spelers : [str]
        de namen van de spelers
        Als een naam "computer" is, dan speelt de computer de optimale
        strategie. (zie "Nim, A Game with a Complete Mathematical Theory,
        C. L. Bouton, Annals of Mathematics, Second Series, Vol 3,
        No. 1/4 (1901 - 1902) pp. 35-39 DOI: 10.2307/1967631")
    minStapels, maxStapels : int
        ondergrens en bovengrens voor het aantal stapels
        Het werkelijke aantal wordt random gekozen
    minLucifers, maxLucifers :  int
        ondergrens en bovengrens voor het aantal lucifers op een stapel.
        Het werkelijke aantal wordt random gekozen per stapel.
    Returns
    -------
    None
    '''
    toestand = beginToestand(minStapels, maxStapels, minLucifers, maxLucifers)
    beurt = 0   # de eerste speler in de lijst is aan de beurt
    while not isAfgelopen(toestand):
        drukToestandAf(toestand)
        if spelers[beurt] == "computer":
            zet = slimmeZet(toestand)
        else:
            zet = leesGeldigeZetIn(spelers[beurt], toestand)
        print(spelers[beurt] + " doet zet: %3d %3d" % zet)
        toestand = doeZet(zet,toestand)
        beurt = (beurt + 1) % len(spelers)
    drukToestandAf(toestand)
    print("De winnaar is " + str(spelers[(beurt - 1) % len(spelers)]))









def beginToestand(minStapels, maxStapels, minLucifers, maxLucifers):
    '''
    Genereer een random begintoestand
    Parameters
    ----------
    minStapels,maxStapels : int
        het minimum/maximum aantal stapels
    minLucifers,maxLucifers : int
        het minimum/maximum aantal lucifers per stapel
    Returns
    -------
    [int]
        een lijst van de stapels (waarde = aantal lucifers)
    '''
    random.seed()
    aantalStapels = random.randrange(minStapels,maxStapels+1)
    stapels = []
    for i in range(aantalStapels):
        stapels.append(random.randrange(minLucifers,maxLucifers+1))
    return stapels


def drukToestandAf(toestand):
    '''
    Drukt een toestand af op de standaard uitvoer.
    Bijvoorbeeld 3 stapels met telkens 3, 2 en 1 lucifer worden
    voorgesteld als
         0[    3]    1[    2]    2[    1]
    Parameters
    ----------
    toestand : [int]
    Returns
    -------
    None
    '''
    lijn = ""
    for stapel in range(len(toestand)):
        lijn += "%5d[%3d]" %(stapel, toestand[stapel])
    print(lijn)


def leesGeldigeZetIn(speler, toestand):
    '''
    Leest een geldige zet in voor een bepaalde speler in een
    bepaalde toestand.
    Parameters
    ----------
    speler : str
    toestand : [int]
    Returns
    -------
    (int,int)
        (stapelNr,aantalLucifers)
    '''
    prompt = speler + ", geef je zet in: (formaat: int int) "
    zet = transformeerInput(input(prompt))
    while not isGeldig(zet,toestand):
        zet = transformeerInput(input(prompt))
    return zet


def transformeerInput(lijn):
    '''
    Interpreteer een lijn input als een zet
    Parameters
    ----------
    lijn : str
    Returns
    -------
    (int,int)
        (stapelNr,aantalLucifers)
    '''
    parts = lijn.split()
    return (int(parts[0]),int(parts[1]))



def isAfgelopen(toestand):
    '''
    Controleer of het spel afgelopen is
    Parameters
    ----------
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    bool
        True indien alle stapels nul lucifers bevatten, False anders
    '''
    for s in toestand:
        if s != 0:
            return False
    return True


def isGeldig(zet, toestand):
    '''
    Controleer of een zet geldig is
    Parameters
    ----------
    zet : (int,int)
        (stapelNr,aantalLucifers)
    toestand : [int]
        de stapels
    Returns
    -------
    bool
        True indien de stapel een geldige stapel is en indien er
            zich op die stapel genoeg lucifers bevinden
        False indien de stapel niet geldig is of indien er zich
            op de stapel niet voldoende lucifers bevinden
    '''
    return 0 <= zet[0] < len(toestand) and toestand[zet[0]] >= zet[1] >= 1



def doeZet(zet,toestand):
    '''
    Voer een zet uit in stand
    Parameters
    ----------
    zet : (int,int)
        (stapelNr,aantal)
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    [int]
        update van de toestand
    '''
    if isGeldig(zet,toestand):
        t = list(toestand)  # maak een kopie van de lijst
        t[zet[0]] -= zet[1] # en pas aan op de juiste plaats.
        return t
    else:
        return None



def naieveZet(toestand):
    '''
    Doe een naieve zet, neem van 1 van de meest gevulde stapels 1 lucifer
    Parameters
    ----------
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    (int,int)
        (stapelNr, aantalLucifers = 1)
    '''
    maxI = 0
    maxAantal = toestand[maxI]
    for i in range(1,len(toestand)):
        if toestand[i] > maxAantal:
            maxAantal = toestand[i]
            maxI = i
    return (maxI,1)




def nimSum(toestand):
    '''
    Bereken de nimsum van de toestand
    dit is de exclusieve or (XOR) van alle groottes van stapels (in binaire notatie)
    Parameters
    ----------
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    int
        de nimsum van alle groottes van stapels
    '''
    res = 0
    for s in toestand:
        res ^= s
    return res




def zoekStapel(nS, toestand):
    '''
    Zoek een stapel waarin voor de grootte de meest
    significante bit van nS ook gezet is
    Parameters
    ----------
    nS : int
        nimsum waarvan de meest significante bit moet gezet zijn.
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    int
        het nummer van een stapel waarvoor in de grootte de meest
        significante bit van nS gezet is.
    '''
    theBit = 1 << (nS.bit_length() - 1)
    for i in range(len(toestand)):
        if toestand[i] & theBit:
            return i



def winnendeZet(toestand):
    '''
    Geef indien mogelijk een winnende zet.
    Een winnende zet maakt de nimsum van de toestand nul.
    Een winnende zet is mogelijk, enkel en alleen, als
    de nimsum van de huidige toestand verschillend is van nul
    Parameters
    ----------
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    (int,int)
        (stapelNr, aantal) indien de winnende zet bestaat, anders None
    '''
    nS = nimSum(toestand)
    if nS == 0:
        return None
    stapelNr = zoekStapel(nS, toestand)
    aantal = toestand[stapelNr] - nimSum([nS,toestand[stapelNr]])
    return (stapelNr, aantal)




def slimmeZet(toestand):
    '''
    Vind een winndende zet indien mogelijk
    anders, geef een naieve zet
    Parameters
    ----------
    toestand : [int]
        een lijst met de groottes van de stapels
    Returns
    -------
    (int,int)
        (stapelNr, aantal)
    '''
    winner = winnendeZet(toestand)
    if winner:
        return winner
    else:
        return naieveZet(toestand)


def test():
    for i in range(10):
        drukToestandAf(beginToestand(1,5,1,10))

#test()




def main():
    nim(("computer","Harry"), 2,4,1,7)

#main()





###
### Extraatje: laat de computer tegen zichzelf spelen en kijk wie er wint
###
def laatdespelersspelen(spelers,minStapels,maxStapels,minLucifers,maxLucifers):
    toestand = beginToestand(minStapels, maxStapels, minLucifers, maxLucifers)
    beurt = 0   # de eerste speler in de lijst is aan de beurt
    while not isAfgelopen(toestand):
        #drukToestandAf(toestand)
        zet = slimmeZet(toestand) # altijd een computergegenereerde slimme zet!
        #print(spelers[beurt] + " doet zet: %3d %3d"%zet)
        toestand = doeZet(zet,toestand)
        beurt = (beurt + 1) % 2
    #drukToestandAf(toestand)
    #print("De winnaar is " + str(spelers[(beurt + 1) % 2]))
    return spelers[(beurt - 1) % 2]

def simuleerSpellen(aantalSpellen):
    spelers = ["startspeler","andere Speler"]
    wins = {}
    for speler in spelers:
        wins[speler] = 0
    for i in range(aantalSpellen):
        winnaar = laatdespelersspelen(spelers,2,4,1,7)
        wins[winnaar] += 1
    for speler in spelers:
        print("Winstpercentage van de "+speler+": %.2f "%(wins[speler]/aantalSpellen))


simuleerSpellen(1000)

