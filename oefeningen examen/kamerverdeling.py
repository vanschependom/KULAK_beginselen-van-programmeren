import random
import math

studenten = ["Dre", "Jasper", "Vincent", "Arthur",
             'Rune', "Tine", "Fleur", "Marie", "Bahdan"]

studenten2 = ["Dre", "Jasper", "Vincent", "Marie"]

vragenlijst = {
    "Vincent": {
        "Dre": 10,
        "Tine": 8
    },
    "Jasper": {
        "Bahdan": 4,
        "Marie": 10
    },
    "Rune": {
        "Vincent": 9,
        "Fleur": 10,
    },
    "Arthur": {
        "Jasper": 10,
        "Dre": 4,
        "Vincent": 2,
        "Fleur": 10
    }
}


def permutaties(studenten):

    if len(studenten) == 1:

        return [studenten]

    output = []

    for student in studenten:

        kopie = list(studenten)
        kopie.remove(student)

        korterePermutaties = permutaties(kopie)

        for permutatie in korterePermutaties:

            toAppend = [student]
            toAppend.extend(permutatie)
            output.append(toAppend)

    return output


def berekenKamerScore(kamer, vragenlijst):

    score = 0
    minScore = 1000000

    for persoon in kamer:

        # De persoon heeft de vragelijst ingevuld
        if persoon in vragenlijst.keys():

            anderePersonen = set(kamer)
            anderePersonen.remove(persoon)

            for anderePersoon in anderePersonen:

                # Als er een score werd ingevuld, verhoog de score hiermee
                if anderePersoon in vragenlijst[persoon].keys():

                    score += vragenlijst[persoon][anderePersoon]

                    if vragenlijst[persoon][anderePersoon] < minScore:

                        minScore = vragenlijst[persoon][anderePersoon]

                # Anders, verhoog de score met 5
                else:

                    score += 5

        # De persoon heeft de vragenlijst niet ingevuld
        else:

            score += 10
            minScore = 0

    return score, minScore


def maakVerdeling(volgorde):

    verdeling = []

    i = 0

    kamer = []

    for student in volgorde:

        if len(kamer) < 3:

            kamer.append(student)

        else:

            verdeling.append(kamer)
            kamer = [student]

    verdeling.append(kamer)

    return verdeling


def berekenVerdelingScore(kamerverdeling, vragenlijst):

    verdelingScore = 0
    minScoreSom = 0

    for kamer in kamerverdeling:

        kamerScore, minScore = berekenKamerScore(kamer, vragenlijst)
        verdelingScore += kamerScore
        minScoreSom += minScore

    return verdelingScore, minScoreSom


def main():

    # Maak alle mogelijke volgordes van studenten
    allePermutaties = permutaties(studenten)

    besteScore = 0
    besteVerdeling = []
    minScoreBeste = 0

    # Loop over elke volgorde
    for volgorde in allePermutaties:

        # Maak een kamerverdeling voor deze volgorde
        kamerVerdeling = maakVerdeling(volgorde)

        # Bereken de score voor deze volgorde
        # Bereken ook de som van de minimumscores van elke kamer
        score, minScore = berekenVerdelingScore(kamerVerdeling, vragenlijst)

        # Als de score beter is
        # Of als de score gelijk is maar de minscore is groter
        if score > besteScore or (score == besteScore and minScore > minScoreBeste):

            # Vervang de beste score, beste verdeling en de nieuwe minsom
            besteScore = score
            besteVerdeling = kamerVerdeling
            minScoreBeste = minScore

        # Als zowel de score als de minscore gelijk, kies een random kamer
        elif score == besteScore and minScore == minScoreBeste:

            besteVerdeling = random.choice([kamerVerdeling, besteVerdeling])

            if besteVerdeling == kamerVerdeling:

                besteScore = score
                minScoreBeste = minScore

    print(besteVerdeling, besteScore)


main()
