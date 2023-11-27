
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
            s += "\n\t" + repr(klacht)
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
            s += "\n\t" + repr(act)
        return s


