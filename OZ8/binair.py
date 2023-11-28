from test_suite import *


def linearZoeken(lijst, getal):
    """
    Linear zoeken
    Parameters
    ----------
    lijst: list
    getal: int

    Returns
    -------
    bool
        True if getal is in lijst
    """
    for getalInLijst in lijst:
        if getalInLijst == getal:
            return True
    return False


def binairZoekenNaief(lijst, getal):
    """
    Binair zoeken met behulp van slice operator
    Parameters
    ----------
    lijst: list
    getal: int

    Returns
    -------
    bool
        True if getal is in lijst
    """
    # Als lijst leeg is, dan zit getal niet in de lijst.
    if len(lijst) == 0:
        return False
    # Als lijst één element bevat, dan zit het getal in de lijst,
    # als dat ene element gelijk is aan het getal.
    if len(lijst) == 1:
        return getal == lijst[0]

    # Bij een lijst met even lengte (i.e. zonder exact midden)
    # zijn er twee middelste elementen, deze variabele wijst naar de rechtse.
    midden = len(lijst) // 2

    # Als het middelste getal gelijk is aan ons getal,
    # dan zit het getal in de lijst.
    if getal == lijst[midden]:
        return True

    # Als het getal (strikt) kleiner is dan het middelste getal,
    # dan zoeken we in de linkerhelft.
    if getal < lijst[midden]:
        return binairZoekenNaief(lijst[:midden], getal)

    # Als de code hier komt, weten we dat ons getal (strikt) groter is dan het midden.
    # We hoeven dus daar niet meer op te controleren en we zoeken rechts.
    # Het middelste element laten we achterwege.
    return binairZoekenNaief(lijst[midden + 1:], getal)


def binairZoekenEfficient(lijst, getal, van=0, totenmet=-1):

    if totenmet == -1:
        return binairZoekenEfficient(lijst, getal, van, len(lijst)-1)

    if totenmet-van == 0:
        return lijst[van] == getal

    midden = (totenmet - van) // 2 + van

    if lijst[midden] == getal:
        return True
    elif lijst[midden] > getal:
        return binairZoekenEfficient(lijst, getal, van, midden)
    else:
        return binairZoekenEfficient(lijst, getal, midden+1, totenmet)


def binairZoekenNietRecursief(lijst, getal):
    van = 0
    totenmet = len(lijst)-1

    while van != totenmet:

        midden = (van + totenmet) // 2

        if lijst[midden] == getal:
            return True

        if lijst[midden] > getal:

            totenmet = midden

        else:

            van = midden + 1

    return False


def setup(n):
    return [0]*n, 1


def main():
    # Voeg hieraan binairZoekenEfficient toe wanneer je het geïmplementeerd hebt.
    algoritmen = [linearZoeken, binairZoekenNaief,
                  binairZoekenEfficient, binairZoekenNietRecursief]
    test(algoritmen, setup)


main()
