
import random


def zoek_pad_naar_waldo(structuur, pad=None):
    if pad is None:
        pad = []

    if isinstance(structuur, Kamer):
        if structuur.waldo_in_kamer():
            return pad

    else:
        for substructuur in structuur.get_substructuur():
            subpad = list(pad)
            subpad.append(substructuur.get_naam())
            subpad = zoek_pad_naar_waldo(substructuur, subpad)
            if subpad is not None:
                return subpad


class WaarIsWaldo:
    def __init__(self):
        self._wereld = None

    def get_wereld(self):
        return self._wereld

    def genereer_wereld(self):
        wereld = Wereld()
        wereld.genereer()
        self._wereld = wereld
        self.plaats_waldo_in_wereld()

    def plaats_waldo_in_wereld(self):

        structuur = self._wereld
        while not isinstance(structuur, Kamer):
            structuur = random.choice(structuur.get_substructuur())

        structuur.plaats_waldo_in_kamer()

    def zoek_waldo(self):
        pad = zoek_pad_naar_waldo(self._wereld)
        return pad


class Structuur:
    def __init__(self, naam):
        self._naam = naam

    def get_naam(self):
        return self._naam

    def __str__(self):
        return self._naam

    def __repr__(self):
        return self._naam


class Wereld(Structuur):
    def __init__(self):
        super().__init__("Wereld")
        self._continenten = []

    def get_substructuur(self):
        return self._continenten

    def genereer(self):
        nmb_continenten = random.randint(1, 4)
        continenten = ["Afrika", "Noord-Amerika", "Europa"]
        random.shuffle(continenten)

        for continentnaam in continenten[:nmb_continenten]:
            continent = Continent(continentnaam)
            continent.genereer()
            self._continenten.append(continent)


class Continent(Structuur):
    def __init__(self, naam):
        super().__init__(naam)
        self._landen = []

    def get_substructuur(self):
        return self._landen

    def genereer(self):
        nmb_landen = random.randint(1, 3)
        landen = {"Afrika": ["Kenia", "Zuid-Afrika", "Kameroen"],
                  "Noord-Amerika": ["Canada", "USA", "Mexico"],
                  "Europa": ["Frankrijk", "Nederland", "Italie"]}

        mogelijke_landen = landen[self._naam]
        random.shuffle(mogelijke_landen)

        for landnaam in landen[self._naam][:nmb_landen]:
            land = Land(landnaam)
            land.genereer()
            self._landen.append(land)


class Land(Structuur):
    def __init__(self, naam):
        super().__init__(naam)
        self._steden = []

    def get_substructuur(self):
        return self._steden

    def genereer(self):
        nmb_steden = random.randint(1, 3)
        steden = {"Kenia": ["Nairobi", "Nakuru", "Mombassa"],
                  "Zuid-Afrika": ["Pretoria", "Bloemfontein", "Durban"],
                  "Kameroen": ["Yaonde", "Douala", "Bafoussam"],
                  "Canada": ["Quebec", "Montreal", "Ottawa"],
                  "USA": ["New-York", "San Francisco", "Phoenix"],
                  "Mexico": ["Oaxaca", "Mexico-Stad", "Merida"],
                  "Frankrijk": ["Angers", "Lyon", "Tours"],
                  "Nederland": ["Dordrecht", "Den Haag", "Eindhoven"],
                  "Italie": ["Napoli", "Genua", "Bologna"]}

        mogelijke_steden = steden[self._naam]
        random.shuffle(mogelijke_steden)

        for stadsnaam in mogelijke_steden[:nmb_steden]:
            stad = Stad(stadsnaam)
            stad.genereer()
            self._steden.append(stad)


class Stad(Structuur):
    def __init__(self, naam):
        super().__init__(naam)
        self._gebouwen = []

    def get_substructuur(self):
        return self._gebouwen

    def genereer(self):
        nmb_gebouwen = random.randint(1, 3)
        gebouwen = ["gemeentehuis", "sporthal", "cinema"]
        random.shuffle(gebouwen)

        for gebouwentype in gebouwen[:nmb_gebouwen]:
            gebouw = Gebouw(gebouwentype)
            gebouw.genereer()
            self._gebouwen.append(gebouw)


class Gebouw(Structuur):
    def __init__(self, naam):
        super().__init__(naam)
        self._kamers = []

    def get_substructuur(self):
        return self._kamers

    def genereer(self):
        nmb_kamers = random.randint(1, 7)

        for kamer_idx in range(nmb_kamers):
            kamer = Kamer(kamer_idx)
            self._kamers.append(kamer)


class Kamer(Structuur):
    def __init__(self, idx):
        self._idx = idx
        super().__init__(f"kamer: {idx}")
        self._waldo = False

    def plaats_waldo_in_kamer(self):
        self._waldo = True

    def waldo_in_kamer(self):
        return self._waldo


if __name__ == '__main__':
    spel = WaarIsWaldo()
    spel.genereer_wereld()
    print(spel.zoek_waldo())
