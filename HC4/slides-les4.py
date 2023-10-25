import math
# Opmerking: je kan in PyCharm makkelijk de lijncomments verwijderen via
# het menu Code/Comment with line comment...

# lijst = [1,2,-8,-3,6,0,-10,5,7]
#
# print(lijst)
# print(sum(lijst))
#
# for i in range(len(lijst)):
#     if lijst[i] < 0:
#         lijst[i] = abs(lijst[i])
#
# print(lijst)
# print(sum(lijst))
# print(max(lijst))


def helloWorld():
    print("Hello World!")

#helloWorld()


def drukDelers(n):
    print(1,end = '')
    for d in range(2,n+1):
        if n % d == 0:
            print(",",d, end = '')
    print()

#drukDelers(1729)


def toonTekst(t):
    print("="*42)
    getoond = 0
    lijnpositie = 0
    while getoond < len(t):
        if lijnpositie >= 42 and t[getoond] == ' ':
            print()
            lijnpositie = 0
        print(t[getoond],end='')
        getoond += 1
        lijnpositie += 1
    print()
    print("="*42)

#toonTekst(input("Geef een tekst in: "))

def maakEenGroet():
    return "Hello World!"

s = maakEenGroet()
#print(s)

def schikTekst(t):
    res = "="*42 + '\n'
    geschikt = 0
    lijnpositie = 0
    while geschikt < len(t):
        if lijnpositie >= 42 and t[geschikt] == ' ':
            res += "\n"
            lijnpositie = 0
        res += t[geschikt]
        geschikt += 1
        lijnpositie += 1
    return res + '\n'+ "="*42

#print(schikTekst(input("Geef een tekst in: ")))



def codeer(tekst,k):
    '''
        Gebruik de sleutel k om de tekst te coderen.
        Elk teken wordt vervangen door het teken waarvan
        de ordinaat k hoger is (modulo 128).

        Parameters
        ----------
        tekst : str
            de te coderen tekst
        k : int
            de sleutelwaarde

        Returns
        -------
        str
            de gecodeerde string
        '''
    result = ""
    for teken in tekst:
        result += chr((ord(teken) + k) % 128)
    return result

#print(codeer("Aha! Zwart is de kleur.",5))

def decodeer(tekst,k):
    '''
    Gebruik de sleutel k om de tekst te decoderen.
    Elk teken wordt vervangen door het teken waarvan
    de ordinaat k lager is (modulo 128).

    Parameters
    ----------
    tekst : str
        de te decoderen tekst
    k : int
        de sleutel

    Returns
    -------
    str
        de gedecodeerde tekst
    '''
    result = ""
    for teken in tekst:
        result += chr((ord(teken) - k) % 128)
    return result

#print(decodeer("Fmf&%_|fwy%nx%ij%pqjzw3",3))
#print(decodeer("Fmf&%_|fwy%nx%ij%pqjzw3",5))

def decodeerBIS(tekst,k):
    '''
    Gebruik de sleutel k om de tekst te decoderen.
    Elk teken wordt vervangen door het teken waarvan
    de ordinaat k lager is (modulo 128).

    Parameters
    ----------
    tekst : str
        de te decoderen tekst
    k : int
        de sleutel

    Returns
    -------
    str
        de gedecodeerde tekst
    '''
    return codeer(tekst,-k)


def delers(n):
    result = [1]
    for d in range(2,n+1):
        if n % d == 0:
            result.append(d)
    return result

#print(delers(1729))

def ispriem(p):
    '''
    Controleert of p een priemgetal is.
    Parameters
    ----------
    p : int
        het te controleren getal

    Returns
    -------
    bool
        True indien p een priemgetal is, anders False
    '''
    return delers(p) == [1,p]


# print("2 is priem?",ispriem(2))
# print("1 is priem?",ispriem(1))
# print("1729 is priem?",ispriem(1729))
# print("997 is priem?",ispriem(997))


def ggdSuperNaief(a,b):
    '''
    Supernaieve functie om de grootste gemene deler
    van twee getallen te zoeken
    Parameters
    ----------
    a : int
    b : int
    Returns
    -------
    int
        de grootste gemene deler van a en b
    '''
    dA = delers(a)
    dB = delers(b)
    grootste = 1
    for ene in dA:
        for andere in dB:
            if ene == andere:
                if ene > grootste:
                    grootste = ene
    return grootste

#print(delers(210))
#print(delers(546))
#print(ggdSuperNaief(210,546))

def ggdSets(a,b):
    '''
    Naieve functie om de grootste gemene deler
    van twee getallen te zoeken
    Parameters
    ----------
    a : int
    b : int
    Returns
    -------
    int
        de grootste gemene deler van a en b
    '''
    dA = set(delers(a))
    dB = set(delers(b))
    return max(dA.intersection(dB))

#print(ggdSets(210,546))

def ggd(a,b):
    '''
    iteratieve functie om de grootste gemene deler
    van twee getallen te zoeken
    Parameters
    ----------
    a : int
    b : int
    Returns
    -------
    int
        de grootste gemene deler van a en b
    '''
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    return a

#print(ggd(210,546))

def ggdStappend(a,b):
    '''
    snellere functie om de grootste gemene deler
    van twee getallen te zoeken
    Parameters
    ----------
    a : int
    b : int
    Returns
    -------
    int
        de grootste gemene deler van a en b
    '''
    if a > b:
        h = a
        a = b
        b = h
    while b % a != 0:
        r = b % a
        b = a
        a = r
    return a

#print(ggdStappend(210,546))


def delersTussen(n,van = 1,tot = -1):
    if tot == -1:
        tot = n+1
    result = []
    for d in range(van,tot):
        if n % d == 0:
            result.append(d)
    return result

#print(delersTussen(1729,100,1729))
#print(delersTussen(1729,15))
#print(delersTussen(1729))


def verwijderVeelvouden(lijst):
    '''
    Verwijdert de veelvouden van het eerste element uit de lijst
    Parameters
    ----------
    lijst : list of int
    Returns
    -------
    None
    '''
    r = lijst[0]
    for i in lijst:
        if i % r == 0:
            lijst.remove(i)

# l = list(range(2,20))
# verwijderVeelvouden(l)
# print(l)

def maiin():
    l = []
    for i in range(0,8432):
        l.append(math.sin(i/100*math.pi))
    print("Het maximum is %5.2f, het komt %d keer voor." % maxNum(l))

def maxNum(l):
    maximum = l[0]
    voorkomen = 0
    for v in l:
        if v == maximum:
            voorkomen += 1
        elif v > maximum:
            maximum = v
            voorkomen = 1
    return (maximum,voorkomen)

#main()

def main():
    uren = int(input("Geef het uur (tussen 0 en 23): "))
    while uren < 0 or uren > 23:
        print("Geen geldige waarde (%d)" % uren)
        uren = int(input("Geef het uur (tussen 0 en 23): "))
    minuten = int(input("Geef de minuten  (tussen 0 en 59): "))
    while minuten < 0 or minuten > 59:
        print("Geen geldige waarde (%d)" % minuten)
        minuten = int(input("Geef de minuten (tussen 0 en 59): "))
    seconden = int(input("Geef de seconden (tussen 0 en 59): "))
    while seconden < 0 or seconden > 59:
        print("Geen geldig waarde (%d)" % seconden)
        seconden = int(input("Geef de seconden (tussen 0 en 59): "))
    print("%02d:%02d:%02d" % (uren,minuten,seconden))

#main()

def mainImproved():
    uren = geefGetalOnder("het uur",23)
    minuten = geefGetalOnder("de minuten",59)
    seconden = geefGetalOnder("de seconden",59)
    print("%02d:%02d:%02d" % (uren,minuten,seconden))

def geefGetalOnder(naam,grens):
    prompt = "Geef " + naam + "(tussen 0 en " + str(grens) + "): "
    res = int(input(prompt))
    while res < 0 or res > grens:
        print("Geen geldige waarde (%d)" % res)
        res = int(input(prompt))
    return res

#mainImproved()

def mainScope():
    som = 0
    for i in range(11):
        kwadraat = i*i
        som += kwadraat
    print(i,som)

#mainScope()

def mainScope2():
    sideLength = 10
    result = cubeVolume(sideLength)
    print(result)

def cubeVolume(l):
    return l ** 3

#mainScope2()

def faculteit(n):
    r = 1
    for i in range(n+1):
        r *= i
    return r

def macht(x,n):
    r = 1
    for i in range(n):
        r *= x
    return r




