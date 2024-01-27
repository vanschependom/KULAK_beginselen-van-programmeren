class Plant():

    def __init__(self, naam, zone):

        self._naam = naam
        self.setZone(zone)

    def setZone(self, zone):

        if zone.getNaam() in ["zonnig", "schaduw", "halfschaduw"]:

            self._zone = zone
            zone.voegPlantToe(self)

        else:

            raise ValueError("Geen geldige zone.")

    def __str__(self):

        return self._naam


class Groente(Plant):

    def __init__(self, naam, zone):

        super().__init__(naam, zone)
        self._type = "Groente"

    def __str__(self):

        return f"{self._naam} ({self._type})"


class MeerjargePlant(Plant):

    def __init__(self, naam, zone):

        super().__init__(naam, zone)
        self._type = "Meerjarige Plant"

    def __str__(self):

        return f"{self._naam} ({self._type})"


class Kruid(MeerjargePlant):

    def __init__(self, naam, zone):

        super().__init__(naam, zone)
        self._type = "Kruid"

    def __str__(self):

        return f"{self._naam} ({self._type})"


class Zone():

    def __init__(self, naam):

        self._naam = naam
        self._planten = list()

    def voegPlantToe(self, plant):

        self._planten.append(plant)

    def getNaam(self):

        return self._naam

    def getPlanten(self):

        return self._planten

    def __str__(self):

        return self._naam


class Moestuin():

    def __init__(self):

        self._zones = list()
        self._planten = list()

    def voegPlantToe(self, plant):

        self._planten.append(plant)

    def voegZoneToe(self, zone):

        self._zones.append(zone)

    def printPlantenPerZone(self):

        for zone in self._zones:

            print(f"Zone '{zone}':")

            for plant in zone.getPlanten():

                print(f"\t- {plant}")


def main():

    moestuin = Moestuin()

    zonnig = Zone("zonnig")
    halfschaduw = Zone("halfschaduw")
    schaduw = Zone("schaduw")

    moestuin.voegZoneToe(zonnig)
    moestuin.voegZoneToe(halfschaduw)
    moestuin.voegZoneToe(schaduw)

    plant = Plant("Olijfboom", zonnig)
    kruid = Kruid("Basilicum", halfschaduw)

    moestuin.voegPlantToe(plant)

    moestuin.printPlantenPerZone()


main()
