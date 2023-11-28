from test_suite import *


def elementInList(lijst):
    elem = -1
    if elem in lijst:
        return True
    else:
        return False


def elementInSetWithTransform(lijst):
    elem = -1
    verzameling = set(lijst)
    if elem in verzameling:
        return True
    else:
        return False


def elementInSet(verzameling):
    elem = -1
    if elem in verzameling:
        return True
    else:
        return False


def mergeLijstForLus(lijst1, lijst2):
    for elem2 in lijst2:
        if elem2 not in lijst1:
            lijst1.append(elem2)
    return lijst1


def mergeLijstSet(lijst1, lijst2):
    set1 = set(lijst1)
    set2 = set(lijst2)
    lijst1 = list(set1.union(set2))
    return lijst1


# Setup
def genereerLijst(nmbElem):
    lijst = list(range(nmbElem))
    return lijst,


def genereerSet(nmbElem):
    verzameling = set(list(range(nmbElem)))
    return verzameling,


def genereerTweeLijsten(nmbElem):
    lijst1 = list(range(nmbElem))
    lijst2 = list(range(nmbElem))
    return lijst1, lijst2


def main():
    import sys
    sys.setrecursionlimit(30000)

    # Element in ...: setup=genereerLijst, N=22
    algoritmen = [elementInList, elementInSet, elementInSetWithTransform]
    setup = [genereerLijst, genereerSet, genereerLijst]
    # test(algoritmen, setup, aRange=numpy.logspace(1, 22, num=22, base=2))

    # Merge lijsten zonder duplicates: setup=genereerTweeLijsten N=14
    algoritmen = [mergeLijstSet, mergeLijstForLus]
    test(algoritmen, genereerTweeLijsten,
         aRange=numpy.logspace(1, 18, num=18, base=2))


main()
