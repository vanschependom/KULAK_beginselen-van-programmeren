
# Opmerking: je kan in PyCharm makkelijk de lijncomments verwijderen via
# het menu Code/Comment with line comment...


def fibonacciRecursief(n):
    if n == 1 or n == 2:
        return 1
    return fibonacciRecursief(n-1)+fibonacciRecursief(n-2)


def fibonacciIteratief(n):
    fib = 1
    fibMin1 = 1
    for i in range(3, n+1):
        som = fib+fibMin1
        fibMin1 = fib
        fib = som
    return fib


def fibonacciNaief(n):
    f = [1, 1]  # f[i] = i+1e Fibonacci getal
    for i in range(2, n):
        f.append(f[-1]+f[-2])
    # er zitten nu n getallen in de lijst (index laatste = n-1)
    return f[-1]


def machtRecursief(x, n):
    if n == 0:
        return 1
    return x*machtRecursief(x, n-1)


def machtIteratief(x, n):
    r = 1
    for i in range(n):
        r *= x
    return r


def machtRecursiefTwee(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return machtRecursiefTwee(x*x, n//2)
    return x*machtRecursiefTwee(x, n-1)


def isPalindroomRecursief(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and isPalindroomRecursief(s[1:-1])


def isPalindroomIteratief(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True


def palindromenNaief(lengte, letters):
    strings = alleStrings(lengte, letters)
    result = []
    for s in strings:
        if isPalindroomRecursief(s):
            result.append(s)
    return result


def palindromen(lengte, letters):
    if lengte == 0:
        return [""]
    if lengte == 1:
        return list(letters)
    result = []
    # Zoek de palindromen van lengte-2
    kleinerePalindromen = palindromen(lengte-2, letters)
    # en kleef elke letter er eens voor en na
    for p in kleinerePalindromen:
        for l in letters:
            result.append(l+p+l)
    return result


def palindromenAlt(lengte, letters):
    if lengte == 0:
        return [""]
    result = []
    s = alleStrings(lengte//2, letters)
    if lengte % 2 == 0:
        # dan moeten we enkel de helften aan elkaar plakken
        for helft in s:
            result.append(helft + keerOm(helft))
    else:
        # dan moeten we er ook nog eens alle mogelijk letters tussen plakken
        for helft in s:
            for l in letters:
                result.append(helft + l + keerOm(helft))
    return result


def alleStrings(lengte, letters):
    if lengte == 0:
        return [""]
    result = []
    # Genereer eerst alle kleinere strings
    kleinereStrings = alleStrings(lengte-1, letters)
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


def keerOm(s):
    r = ""
    for i in range(len(s)):
        r += s[-(i+1)]
    return r


def palindromenMidden(middenDeel, lengteRest, letters):
    '''
    Genereert palindromen met gegeven middendeel
    Parameters
    ----------
    middenDeel: str
        pre: middenDeel is een palindroom
    lengteRest : int
        pre: lengteRest is even!
    letters : str
    Returns
    -------
    [str]
        een lijst palindromen waarbij het middendeel gebruikt wordt
        en er nog 'lengteRest' tekens aan toegevoegd werden
    '''
    if lengteRest == 0:
        return [middenDeel]
    result = []
    for l in letters:
        # voeg iets toe aan het middendeel en vraag de palindromen van lengte-2 op
        result += palindromenMidden(l+middenDeel+l, lengteRest-2, letters)
    return result


def palindromenAlt2(lengte, letters):
    if lengte % 2 == 0:
        return palindromenMidden("", lengte, letters)
    else:
        result = []
        for l in letters:
            result += palindromenMidden(l, lengte-1, letters)
        return result


def allePalindromenZonderDubbels(letters):
    # in elk geval de lege string
    result = ['']
    for l in letters:   # indien geen letters, for niet uitgevoerd!
        # in elk geval ook de string met enkel deze letter
        result += [l]
        # verwijder de letter (uit een kopie!)
        minderLetters = list(letters)
        minderLetters.remove(l)
        # zoek de kleinere palindromen
        kleinerePalindromen = allePalindromenZonderDubbels(minderLetters)
        # en kleef er de letter ook eens voor en achter
        for p in kleinerePalindromen:
            result.append(l+p+l)
    return result


def alleStringsZonderDubbels(letters):
    # in elk geval de lege string
    result = ['']
    # zonder elke letter eens af
    for l in letters:  # indien geen letters meer, for niet uitgevoerd!
        # verwijder de letter (uit een kopie!)
        minderLetters = list(letters)
        minderLetters.remove(l)
        # zoek de kleinere strings
        kleinereStrings = alleStringsZonderDubbels(minderLetters)
        # en kleef er de letter ook eens voor
        for s in kleinereStrings:
            result.append(l+s)
    return result


def loketRijenAlt(lengte):
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
    return loketRijenMetPrefix("", 0, lengte)


def loketRijenMetPrefix(prefix, verschilAB, lengte):
    '''
    Genereert alle mogelijke loketrijen (strings) met letters A en B
    die starten met de gegeven prefix, en <lengte> langer zijn dan de prefix,
    zodat voor elke positie geldt dat het aantal A's tot die positie
    groter of gelijk is aan het aantal B's tot die positie.
    Parameters
    ----------
    prefix : str
        moet een string zijn met enkel A's en B's
    verschilAB : int
        moet het verschil tussen het aantal A's en B's in de prefix
    lengte : int
        De resterende lengte die toegevoegd moet worden
    Returns
    -------
    [str]
        de lijst met toegelaten loketrijen (strings)
    '''
    if lengte == 0:
        return [prefix]
    if verschilAB > 0:
        # dan kan er na de prefix zowel een A als een B komen
        return loketRijenMetPrefix(prefix+'A', verschilAB+1, lengte-1) + \
            loketRijenMetPrefix(prefix+'B', verschilAB-1, lengte-1)
    else:
        # dan mag er enkel een A komen na de prefix
        return loketRijenMetPrefix(prefix+'A', verschilAB+1, lengte-1)


def loketRijen(lengte):
    if lengte == 0:
        return ['']
    kortereRijen = loketRijen(lengte-1)
    result = []
    for rij in kortereRijen:
        # 'A' mag altijd toegevoegd worden
        result.append(rij+'A')
        # 'B' mag enkel toegevoegd worden indien
        # er reeds meer 'A's dan 'B's voorkomen
        if rij.count('A') > rij.count('B'):
            result.append(rij+'B')
    return result


def main():
    print(fibonacciIteratief(35))
    print(fibonacciRecursief(35))
    # print(keerOm("tommy"))
    # print(palindromen(1,"abc"))
    # print(palindromenAlt(4,"abc"))
    # print(alleStrings(2,"abc"))
    #
    # print(allePalindromenZonderDubbels("abcd"))
    # print(alleStringsZonderDubbels("abc"))

    # for rij in loketRijen(5):
    #     print(rij)
    #
    #
    # print(palindromenNaief(4,"abc"))


main()
