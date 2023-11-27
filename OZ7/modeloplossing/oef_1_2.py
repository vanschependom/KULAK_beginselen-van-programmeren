
def genereerZinnenRec(woordenLijst):
    '''
        Recursieve functie om alle zinnen bestaande uit exact de woorden uit woordenLijst te genereren
    Parameters
    ----------
    woordenLijst: list
        een lijst van strings
    Returns
    -------
    list:
        een lijst van strings, waarbij elke string een zin is bestaande uit alle woorden in 'woordenLijst'.
        De lijst bevat alle mogelijke zinnen die gemaakt kunnen worden op basis van de woorden uit woordenLijst
    '''
    # Triviaal geval: de woordenlijst bestaat uit 1 element.
    # Resultaat: een zin bestaande uit 1 woord.
    if len(woordenLijst) == 1:
        return [woordenLijst[0]]
    else:
        # Strategie:
        #   Alle woorden in de woordenlijst 1 voor 1 als eerste woord van de zin nemen
        #       (=> opsplitsing in len(woordenLijst) deelproblemen)
        #   Voor elk woord alle zinnen zonder dit woord recursief berekenen
        #       (=> probleem kleiner gemaakt)
        #   Het weggehouden woord toevoegen als eerste woord aan elk van de recursief gegenereerde zinnen
        resultaatLijst = list()  # Lijst waarin alle zinnen bijgehouden zullen worden

        for woord in woordenLijst:
            restWoorden = list(woordenLijst)  # Kopie maken van de lijst
            restWoorden.remove(woord)  # Het woord uit de kopie verwijderen
            # Let op: als je geen kopie maakt, wordt het woord permanent uit de woordenlijst zelf verwijderd!

            zinnenRestWoorden = genereerZinnenRec(restWoorden)  # Recursieve oproep: alle zinnen zonder dit woord

            # Deelresultaat gebruiken: woord vooraan plaatsen in alle gegenereerde zinnen en aan de resultatenlijst toevoegen
            for zin in zinnenRestWoorden:
                nieuweZin = woord + " " + zin  # Spatie dient om woorden van elkaar te scheiden
                resultaatLijst.append(nieuweZin)

        return resultaatLijst


def main():
    print("Resultaat als er maar 1 woord is:")
    print(genereerZinnenRec(["ik"]))
    print()

    print("Resultaat zoals in de opgave:")
    woorden = ["ik", "programmeer", "graag"]
    print(genereerZinnenRec(woorden))
    print()

    print("Resultaat als er nog meer woorden zijn:")
    meerWoorden = ["ik", "programmeer", "graag", "in", "Python"]
    print(genereerZinnenRec(meerWoorden))
    print()


    # Merk op dat de code voor genereerZinnenRec niet erg efficiënt is.
    # Uncomment volgende code om je computer heel lang te doen rekenen
    # Maak eventueel zelf een schatting over hoe lang het zal duren door stap per stap
    # 1 woord meer toe te voegen en te zien hoe de benodigde tijd groeit
    # 15 elementen =
    # superVeelWoorden = ["Deze" , "zin", "bevat", "te", "veel", "woorden", "om" , "snel", "door", "een", "normale", "computer", "verwerkt", "te", "worden"]
    # alleZinnen = genereerZinnenRec(superVeelWoorden)

    # Hint: ctrl-c stopt het uitvoeren van code


main()