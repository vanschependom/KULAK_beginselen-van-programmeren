from test_suite import *
from random import uniform


def selectionSort(lijst):
    for index in range(len(lijst)):

        # print(lijst)

        # MinimumIndex is de index van het kleinste element tot nu toe gevonden.
        minimumIndex = index

        # Vanaf index (exclusief) tot het einde van de lijst,
        # zoek de index van het kleinste element.
        for index2 in range(index + 1, len(lijst)):
            if lijst[minimumIndex] > lijst[index2]:
                minimumIndex = index2

        # print(lijst[index], lijst[minimumIndex])

        # Wissel het kleinst gevonden element met index.
        temp = lijst[index]
        lijst[index] = lijst[minimumIndex]
        lijst[minimumIndex] = temp


def quickSort(lijst, van=0, totenmet=None):
    if totenmet == None:
        totenmet = len(lijst)-1

    # Triviaal geval, de lege lijst of lijst met één element is gesorteerd.
    if van >= totenmet:
        return

    spil = partitie(lijst, van, totenmet)

    quickSort(lijst, van, spil-1)
    quickSort(lijst, spil+1, totenmet)


def partitie(lijst, van, totenmet):
    # Kies laatste element van de lijst als pivot element
    pivot = lijst[totenmet]
    indexLow = van
    indexHigh = totenmet - 1

    while True:
        while indexLow <= indexHigh and lijst[indexHigh] >= pivot:
            indexHigh -= 1

        while indexLow <= indexHigh and lijst[indexLow] <= pivot:
            indexLow += 1

        if indexLow <= indexHigh:
            lijst[indexLow], lijst[indexHigh] = lijst[indexHigh], lijst[indexLow]
        else:
            break

    lijst[indexLow], lijst[totenmet] = lijst[totenmet], lijst[indexLow]

    return indexLow


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


def setupGemiddeldeGeval(n):
    teSorteren = []
    for iteratie in range(n):
        teSorteren.append(uniform(0, 1))
    return [teSorteren]


def setupSlechtsteGeval(n):
    lijst = range(n, 0, -1)
    return [list(lijst)]


def main():
    # Gebruik onderstaande twee lijnen als je de 'recursion depth exceeded' error krijgt.
    import sys
    sys.setrecursionlimit(30000)
    algoritmen = [selectionSort, quickSort, mergeSort, sorted]
    print(setupGemiddeldeGeval(10))
    print(setupSlechtsteGeval(10))
    test(algoritmen, setupSlechtsteGeval,
         aRange=numpy.logspace(1, 11, num=11, base=2))


main()
