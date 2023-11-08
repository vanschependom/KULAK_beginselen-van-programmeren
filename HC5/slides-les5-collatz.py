
# Opmerking: je kan in PyCharm makkelijk de lijncomments verwijderen via
# het menu Code/Comment with line comment...

def collatz(n):
    '''
    Genereer statistieken over de rij van Collatz
    voor een gegeven startwaarde

    Parameters
    ----------
    n : int
        de startwaarde

    Returns
    -------
    (int,int,int)
        een tupel met daarin:
            0: de startwaarde
            1: het aantal stappen in de reeks
            2: de maximale waarde in de reeks
    '''
    # eerste getal in de reeks, de startwaarde:
    x = n
    statistiek = initieleStatistiek(n)
    while x != 1:
        x = doeCollatzStap(x)
        statistiek = verwerkStatistiek(statistiek, x)
    return statistiek


def collatzBeter(n):
    # eerste getal in de reeks, de startwaarde:
    x = n
    # initiele statistiek:
    statistiek = (n,0,n)
    while x != 1:
        x = doeCollatzStap(x)
        # verwerk de nieuwe waarde in de statistiek:
        statistiek = (statistiek[0],statistiek[1]+1,max(x,statistiek[2]))
    return statistiek



def collatzNaief(n):
    rij = [n]
    if rij[0] == 1:
        klaar = True
    else:
        klaar = False
    while not klaar:
        rij.append(doeCollatzStap(rij[-1]))
        if rij[-1] == 1:
            klaar = True
    return (n,len(rij)-1,max(rij))


def initieleStatistiek(n):
    '''
    Genereert een initiele statistiek
    Parameters
    ----------
    n : int
        de startwaarde
    Returns
    -------
    (int,int,int)
        (n,0,n)
    '''
    return (n,0,n)

def doeCollatzStap(x):
    '''
    Voert een Collatz stap uit en geeft het
    volgende getal terug op basis van het gegeven getal
    Parameters
    ----------
    x : int
        de huidige waarde
    Returns
    -------
    int
        de volgende waarde
    '''
    if x % 2 == 0:
        return x//2
    else:
        return 3*x+1

def verwerkStatistiek(statistiek,x):
    '''
    Verwerkt een statistiek op basis van een nieuwe
    waarde in de rij en geeft de vernieuwde statistiek terug
    Parameters
    ----------
    statistiek : (int,int,int)
        de basisstatistiek (startwaarde, stappen, maximum)
    x : int
        de nieuwe waarde in de reeks
    Returns
    -------
    (int,int,int)
        (startwaarde, stappen + 1, max(maximum,x)
    '''
    maximum = statistiek[2]
    if x > maximum:
        maximum = x
    return (statistiek[0],statistiek[1]+1,maximum)

def testStap():
    print(doeCollatzStap(3))
    print(doeCollatzStap(10))
    print(doeCollatzStap(5))
    print(doeCollatzStap(16))

#testStap()


def testRun():
    print(collatzNaief(3))
    print()
    print("%5d : stappen %5d, maximum %7d"%collatzNaief(3))
    print()
    for i in range(1,101):
        print("%5d : stappen %5d, maximum %7d"%collatzNaief(i))

#testRun()


def main():
    grootsteMaximum = (0,0,-1)
    langsteReeks = (0,-1,0)
    for i in range(1,1000001):
        stat = collatz(i) # bereken de statistieken voor i
        # update beste waarden indien nodig:
        if stat[1] > langsteReeks[1]:
            langsteReeks = stat
        if stat[2] > grootsteMaximum[2]:
            grootsteMaximum = stat

    print("Langste reeks voor    n=%-7d : %5d stappen, maximale waarde: %14d"%langsteReeks)
    print("Grootste maximum voor n=%-7d : %5d stappen, maximale waarde: %14d"%grootsteMaximum)

main()

