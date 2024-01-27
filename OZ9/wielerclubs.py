class Club():

    def __init__(self, naam):

        self._naam = naam
        self._ledenlijst = list()

    def voegLidToe(self, lid):

        self._ledenlijst.append(lid)
        lid.setClub(self)

    def printLeden(self):

        print(f"Leden van club '{self._naam}'")

        for lid in self._ledenlijst:

            print(f"\t- {lid}")


class AmateurClub(Club):

    def __init__(self, naam):

        super().__init__(naam)
        self._activiteiten = list()
        self._uitstappen = list()
        self._type = "amateurclub"

    def voegActiviteitToe(self, activiteit):

        self._activiteiten.append(activiteit)

    def voegUitstap(self, uitstap):

        self._activiteiten.append(uitstap)

    def getTypeClub(self):

        return self._type


class Activiteit():

    def __init__(self, naam):

        self._naam = naam


class Uitstap():

    def __init__(self, naam):

        self._naam = naam


class ProfClub(Club):

    def __init__(self, naam):

        super().__init__(naam)
        self._deelnames = dict()
        self._type = 'profclub'

    def getTypeClub(self):

        return self._type

    def voegLidToeAanWedstrijd(self, lid, wedstrijd):

        if wedstrijd.getNaam() in self._deelnames.keys():

            self._deelnames[wedstrijd.getNaam()].append(lid)

        else:

            self._deelnames[wedstrijd.getNaam()] = [lid]

    def printUitslagen(self):

        print(f"Uitslagen voor de club '{self._naam}'")

        for wedstrijdNaam, leden in self._deelnames.items():

            print(f"\t - Leden voor de wedstrijd '{wedstrijdNaam}':")

            for lid in leden:

                uitslagen = lid.getUitslagen()
                print(f"\t\t - {lid} (plaats {uitslagen[wedstrijdNaam]})")


class Lid():

    def __init__(self, naam, admin, club=None):

        self._naam = naam
        self._registatieNummer = None
        self._uitslagen = dict()
        self.setClub(club)
        if club != None:
            club.voegLidToe(self)
        admin.registreerNieuwLid(self)

    def setRegistratienummer(self, nummer):

        self._registatieNummer = nummer

    def setClub(self, club):

        self._club = club

    def getClub(self):

        return self._club

    def voegUitslagToe(self, wedstrijd, plaats):

        self._uitslagen[wedstrijd.getNaam()] = plaats

    def getUitslagen(self):

        return self._uitslagen

    def printUitslagen(self):

        print(f"Uitslagen voor {self._naam}")

        for wedstrijd, plaats in self._uitslagen.items():

            print(f"\t - Wedstrijd '{wedstrijd}': #{plaats}")

    def __str__(self):

        return f"{self._naam} (nr. {self._registatieNummer})"


class Wedstrijd():

    def __init__(self, naam):

        self._naam = naam
        self._uitslagen = dict()

    def voegUitslagToe(self, persoon, plaats):

        self._uitslagen[str(plaats)] = persoon
        persoon.voegUitslagToe(self, plaats)
        persoon.getClub().voegLidToeAanWedstrijd(persoon, self)

    def getNaam(self):

        return self._naam

    def __str__(self):

        return self._naam


class Administratie():

    def __init__(self):

        self._wedstrijden = list()
        self._clubs = list()
        self._uitgedeeldeNummers = [0]

    def voegClubToe(self, club):

        self._clubs.append(club)

    def voegWedstrijdToe(self, wedstrijd):

        self._wedstrijden.append(wedstrijd)

    def registreerNieuwLid(self, lid):

        nieuwNummer = self._uitgedeeldeNummers[-1]+1

        lid.setRegistratienummer(nieuwNummer)
        self._uitgedeeldeNummers.append(nieuwNummer)


def main():

    admin = Administratie()

    deClerck = ProfClub("Ramen en Deuren De Clerck")
    jumbo = ProfClub("Visma - Lease-a-Bike")

    admin.voegClubToe(deClerck)

    vincent = Lid("Vincent", admin)
    stefan = Lid("Stefan", admin, deClerck)
    robin = Lid("Robin", admin, deClerck)
    wout = Lid("Wout", admin, jumbo)
    christophe = Lid("Christophe", admin, jumbo)

    deClerck.voegLidToe(vincent)

    gpDeClerck = Wedstrijd("Grote Prijs De Clerck")
    gpDeClerck.voegUitslagToe(vincent, 1)
    gpDeClerck.voegUitslagToe(christophe, 3)
    gpDeClerck.voegUitslagToe(wout, 2)
    gpDeClerck.voegUitslagToe(stefan, 4)

    gpDeClerck = Wedstrijd("TTC Temse-Velle")
    gpDeClerck.voegUitslagToe(wout, 1)
    gpDeClerck.voegUitslagToe(robin, 3)
    gpDeClerck.voegUitslagToe(stefan, 2)

    deClerck.printLeden()
    jumbo.printLeden()

    vincent.printUitslagen()
    robin.printUitslagen()

    deClerck.printUitslagen()
    jumbo.printUitslagen()


main()
