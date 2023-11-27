from buurtfeesten import *

def main():

    b = Buurtfeest("Kulaktie")
    b.voegComitelidToe(Comitelid("Jan Janssens", "Heirweg 1, 1000 Brussel"))
    a1 = Activiteit("Nieuwjaarsreceptie", "Concertgebouw Brugge")
    b.voegActiviteitToe(a1)
    a2 = Activiteit("Wandeling", "Oostende")
    b.voegActiviteitToe(a2)
    a3 = Activiteit("Lezing", "Schouwburg Kortrijk")
    b.voegActiviteitToe(a3)
    k = Klacht("lawaaihinder")
    a1.voegKlachtToe(k)
    k.voegReactieToe("De door de politie opgemeten waarde overschrijdt de drempel niet.")

    print(b.getAantalActiviteiten())


    feestLijst = []
    # <code om een testomgeving op te zetten>
    # maak een aantal feesten aan, ken er leden en activiteiten aan toe
    # maak een aantal verschillende klachten voor activiteiten
    # etc.
    feestLijst.append(b)

    ## OPDRACHT 1: feesten met minstens 3 activiteiten
    groteFeesten = []
    for feest in feestLijst:
        if feest.getAantalActiviteiten() >= 3:
            groteFeesten.append(feest)
    print("Feesten met minstens 3 activiteiten: [aantal: %d]"%len(groteFeesten))
    for f in groteFeesten:
        print("-",f.getNaam())

    ## OPDRACHT 2: comitéleden die bij minstens 2 feesten betrokken zijn
    aantalFeestenPerLid = dict()
    for feest in feestLijst:
        for lid in feest.getComiteleden():
            if lid not in aantalFeestenPerLid:
                aantalFeestenPerLid[lid] = 1
            else:
                aantalFeestenPerLid[lid] += 1
    betrokkenLeden = []
    for lid in aantalFeestenPerLid:
        if aantalFeestenPerLid[lid] >= 2:
            betrokkenLeden.append(lid)
    print("Leden betrokken in minstens 2 feesten: [aantal: %d]"%len(betrokkenLeden))
    for lid in betrokkenLeden:
        print("-",lid.getNaam())


    ## OPDRACHT 3: reacties voor feesten met lawaaihinder
    print("Reacties op feesten met lawaaihinder:")
    for feest in feestLijst:
        for act in feest.getActiviteiten():
            for klacht in act.getKlachten():
                if klacht.getOmschrijving() == "lawaaihinder":
                    print(feest.getNaam(), act.getNaam() + ":")
                    for reactie in klacht.getReacties():
                        print("\t->", reactie)


    print()
    print(b)
    print()
    print(b.getComiteleden())
    print()
    print(a1)
    print()
    print(k)

main()

