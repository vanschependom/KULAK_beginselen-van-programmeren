
class Klacht:
    '''
    Klasse die klachten voorstelt. Een klacht bestaat uit
    een omschrijving en een lijst reacties (strings).
    '''
    def __init__(self, omschrijving):
        '''
        Maakt een nieuwe Klacht aan met gegeven omschrijving
        en een lege lijst reacties.
        Parameters
        ----------
        omschrijving : str
        '''
        self._omschrijving = omschrijving
        self._reacties = []

    def getOmschrijving(self):
        '''
        Geeft de omschrijving terug
        Returns
        -------
        str
        '''
        return self._omschrijving

    def getReacties(self):
        '''
        Geeft (een kopie van) de lijst reacties terug
        Returns
        -------
        [str]
        '''
        return list(self._reacties)

    def voegReactieToe(self,reactie):
        '''
        Voegt een reactie toe aan de lijst reacties.
        Parameters
        ----------
        reactie : str
        '''
        self._reacties.append(reactie)

    def __repr__(self):
        '''
        Geeft een leesbare string terug van dit Klacht object.
        Returns
        -------
        str
        '''
        s =  "Klacht: " + self.getOmschrijving()
        for r in self._reacties:
            s += "\n\t Reactie: " + r
        return s


class Comitelid:
    '''
    Klasse die comitéleden voorstelt.
    Een comitélid heeft een naam en een adres.
    '''
    def __init__(self, naam, adres):
        '''
        Maakt een nieuw Comitelid aan met gegeven naam en adres.
        Parameters
        ----------
        naam : str
        adres : str
        '''
        if not isinstance(naam,str):
            raise TypeError("naam is geen string!")
        if naam == "":
            raise ValueError("naam is geen geldige string!")
        if not isinstance(adres,str):
            raise TypeError("adres is geen string!")
        if adres == "":
            raise ValueError("adres is geen geldige string!")
        self._naam = naam
        self._adres = adres

    def getNaam(self):
        '''
        Geeft de naam van het Comitelid terug.
        Returns
        -------
        str
        '''
        return self._naam

    def getAdres(self):
        '''
        Geeft het adres van het Comitelid terug.
        Returns
        -------
        str
        '''
        return self._adres

    def setAdres(self,adres):
        '''
        Past het adres van het Comitelid aan.
        Parameters
        ----------
        adres :  str
        '''
        self._adres = adres

    def __repr__(self):
        '''
        Geeft een leesbare string terug van dit Comitelid object.
        Returns
        -------
        str
        '''
        s = "Comitélid: " + self.getNaam() + " (" + self.getAdres() + ")"
        return s

    def __lt__(self, other):
        '''
        LESS THAN
        Vergelijkt twee Comitéleden
        self is kleiner dan other indien de naam van self
        alfabetisch voor de naam van other komt.
        Indien beide dezelfde naam hebben wordt het adres
        gebruikt om te vergelijken.
        Parameters
        ----------
        other : Comitelid
        Returns
        -------
        bool
        '''
        if self.getNaam() == other.getNaam():
            return self.getAdres() < other.getAdres()
        else:
            return self.getNaam() < other.getNaam()

    def __gt__(self, other):
        '''
        GREATER THAN
        Vergelijkt twee Comitéleden
        self is groter dan other indien other kleiner is dan self
        Parameters
        ----------
        other : Comitelid
        Returns
        -------
        bool
        '''
        return other < self

    def __le__(self, other):
        '''
        LESS THAN OR EQUAL
        Vergelijkt twee Comitéleden
        Geeft True indien self kleiner dan of gelijk is aan other.
        Parameters
        ----------
        other : Comitelid
        Returns
        -------
        bool
        '''
        return not (other < self)

    def __ge__(self, other):
        '''
        GREATER THAN OR EQUAL
        Vergelijkt twee Comitéleden
        Geeft True indien self groter dan of gelijk is aan other.
        Parameters
        ----------
        other : Comitelid
        Returns
        -------
        bool
        '''
        return not (self < other)

    def __eq__(self, other):
        '''
        EQUALS
        Vergelijkt twee Comitéleden
        self is gelijk aan other indien de naam en het adres
        van self en other gelijk zijn.
        Parameters
        ----------
        other : Comitelid
        Returns
        -------
        bool
        '''
        return not (self < other) and not (other < self)

    def __ne__(self, other):
        '''
        NOT EQUAL
        Vergelijkt twee Comitéleden
        Geeft True indien self niet gelijk is aan other.
        Parameters
        ----------
        other : Comitelid
        Returns
        -------
        bool
        '''
        return not(self == other)




class Activiteit:
    '''
    Klasse die activiteiten voorstelt.
    Een activiteit heeft een naam, locatie
    en een lijst met eventuele klachten.
    '''
    def __init__(self, naam, locatie):
        '''
        Maakt een nieuwe activiteit met gegeven naam en locatie.
        Parameters
        ----------
        naam : str
        locatie : str
        '''
        self._naam = naam
        self._locatie = locatie
        self._klachten = []

    def getNaam(self):
        '''
        Geeft de naam terug.
        Returns
        -------
        str
        '''
        return self._naam

    def getLocatie(self):
        '''
        Geeft de locatie terug.
        Returns
        -------
        str
        '''
        return self._locatie

    def getKlachten(self):
        '''
        Geeft een (kopie van) de lijst klachten terug.
        Returns
        -------
        [Klacht]
        '''
        return list(self._klachten)

    def voegKlachtToe(self, klacht):
        '''
        Voegt een klacht toe aan deze activiteit.
        Parameters
        ----------
        klacht : Klacht
        '''
        self._klachten.append(klacht)

    def __repr__(self):
        '''
        Geeft een leesbare string terug van dit Activiteit object.
        Returns
        -------
        str
        '''
        s = "Activiteit: " + self.getNaam() + " (" + self.getLocatie() + ")"
        for klacht in self._klachten:
            s += "\n\t Klacht: " + klacht.getOmschrijving()
        return s


class Buurtfeest:
    '''
    Klasse die buurtfeesten voorstelt.
    Een buurtfeest heeft een naam,
    een aantal comitéleden en een lijst activiteiten.
    '''

    def __init__(self, naam):
        '''
        Maakt een nieuw buurtfeest aan.
        (zonder comitéleden of activiteiten)
        '''
        self._naam = naam
        self._comiteleden = []
        self._activiteiten = []

    def getNaam(self):
        '''
        Geeft de naam van het buurtfeest terug.
        Returns
        -------
        str
        '''
        return self._naam

    def getComiteleden(self):
        '''
        Geeft een kopie van de lijst comitéleden terug.
        Returns
        -------
        [Comitelid]
        '''
        return list(self._comiteleden)

    def getActiviteiten(self):
        '''
        Geeft een kopie van de lijst activiteiten terug.
        Returns
        -------
        [Activiteit]
        '''
        return list(self._activiteiten)

    def getAantalActiviteiten(self):
        '''
        Geeft het aantal activiteiten terug
        Returns
        -------
        int
        '''
        return len(self._activiteiten)

    def voegComitelidToe(self, lid):
        '''
        Voegt een comitélid toe
        Parameters
        ----------
        lid : Comitelid
        '''
        self._comiteleden.append(lid)

    def voegActiviteitToe(self, activiteit):
        '''
        Voegt een activiteit toe.
        Parameters
        ----------
        activiteit : Activiteit
        '''
        self._activiteiten.append(activiteit)


    def __repr__(self):
        '''
        Geeft een leesbare string terug van dit Buurtfeest object.
        Returns
        -------
        str
        '''
        s = "Buurtfeest: " + self.getNaam()
        for act in self._activiteiten:
            s += "\n\t Activiteit: "+act.getNaam()
        return s

    ##
    #   Definieer eerst een inwendige hulpklasse
    #   Deze stelt een iteratorobject voor,
    #   voor een gegeven lijst
    class _Iterator:
        # maak een nieuwe iterator op basis van een lijst
        def __init__(self,ledenlijst):
            # als iterator nemen we gewoon die die reeds
            # bestaat voor lijsten
            self._iterator = ledenlijst.__iter__()

        def __next__(self):
            # De next methode moet bestaan op een iterator
            # deze geeft het volgende element, als het bestaat
            # of een foutmelding als we ten einde zijn.
            # die foutmelding wordt door de for afgehandeld
            # (op basis daarvan wordt beslist de for te stoppen)
            return self._iterator.__next__()


    ##
    #   Implementeer daarna de methode die een
    #   iterator maakt voor deze klasse:
    def __iter__(self):
        # geef een object van de anonieme klasse terug
        # dat is een iterator voor de comiteledenlijst
        return self._Iterator(self._comiteleden)

