
class Dieet:
    """
    Klas implementatie voor Dieet
    """
    def __init__(self, vegitarisch, allergieen=[], vis=True):
        """
        Constructor voor dieet
        Parameters
        ----------
        vegitarisch: bool
        allergieen: list(str)
        vis: bool
        """
        self._vegitarisch = vegitarisch
        # AANDACHT
        if vegitarisch:
            self._vis = vis
        else:
            self._vis = None
        self._allergieen = allergieen
    
    def getVegitarisch(self):
        return self._vegitarisch
    
    def getAllergieen(self):
        return list(self._allergieen)
    
    def getVis(self):
        return self._vis
    
    # AANDACHT
    def calculateCategorie(self):
        if len(self.getAllergieen()) > 0:
            return 'bijzonder'
        elif self.getVegitarisch():
            if self.getVis():
                return 'vegitarisch met vis'
            else:
                return 'vegitarisch zonder vis'
        else:
            return 'normaal'
    
    def __str__(self):
        return 'Dieet: ' + self.calculateCategorie()
    
    def __repr__(self):
        return self.__str__()
    
class Gevangene:
    """
    Klas implementatie voor Gevangene
    """
    def __init__(self, naam, dieet, internetToegang, bezoekdagen):
        """
        Constructor voor gevangene
        Parameters
        ----------
        naam: str
        dieet: Dieet
        internetToegang: bool
        bezoekdagen: list(str)
        """
        self._naam = naam
        self._dieet = dieet
        self._internetToegang = internetToegang
        self._bezoekdagen = bezoekdagen
    
    def getNaam(self):
        return self._naam
    
    def getInternetToegang(self):
        return self._internetToegang
    
    def getDieet(self):
        return self._dieet
    
    def getBezoekdagen(self):
        return self._bezoekdagen
    
    def __str__(self):
        output = 'Naam: {0}\n'.format(self.getNaam())
        output += '\t{0}\n'.format(str(self.getDieet()))
        output += '\tInternet toegang: {0}\n'.format(self.getInternetToegang())
        output += '\tBezoekdagen: {0}\n'.format(self.getBezoekdagen())
        return output

    def __repr__(self):
        return self.__str__()

class InternetAansluiting:
    """
    Klas implementatie voor InternetAansluiting
    """
    def __init__(self, aanwezig, actief):
        """
        Constructor voor internetaansluiting
        Parameters
        ----------
        aanwezig: bool
        actief: bool
        """
        self._aanwezig = aanwezig
        if self._aanwezig:
            self._actief = actief
        else:
            self._actief = False
        
    def getAanwezig(self):
        return self._aanwezig
    
    def getActief(self):
        return self._actief
    
    def setActief(self, actief):
        if self.getAanwezig():
            self._actief = actief
    
    #AANDACHT
    def hasToegang(self):
        return self._aanwezig and self._actief
    
    def __str__(self):
        return 'Internet aansluiting: [{0}, {1}]'.format(self.getAanwezig(), self.getActief())

    def __repr__(self):
        return self.__str__()

class Cel:
    """
    Klas implementatie voor Cel
    """
    
    # Klas variabele, voor elk object van de Cel zal deze variable bevatten met dezelfde waarde.
    _counter = 0
    def __init__(self, capaciteit, internetAansluiting):
        """
        Constructor voor klasse Cel
        Parameters
        ----------
        capaciteit: int
        internetAansluiting: bool
        """
        self._celNr = Cel._counter
        Cel._counter += 1
        assert capaciteit in [4,6,8], 'Capaciteit van cellen is 4, 6 of 8.'
        self._capaciteit = capaciteit
        self._internetAansluiting = internetAansluiting
        self._gevangenen = []

    def getInternetAansluiting(self):
        return self._internetAansluiting

    def getGevangenen(self):
        return list(self._gevangenen)
    
    # AANDACHT
    def addGevangene(self, gevangene):
        if len(self._gevangenen) < self._capaciteit:
            if not gevangene.getInternetToegang() and self.getInternetAansluiting().hasToegang():
                self.getInternetAansluiting().setActief(False)
            self._gevangenen.append(gevangene)
        else:
            print("Cel {0} is volzet".format(self._celNr))
    
    # AANDACHT
    def removeGevangen(self, gevangene):
        self._gevangenen.remove(gevangene)
        # logica voor het geval door gevange de toegang tot internet werd afgezet.
        if not self.getInternetAansluiting().getActive() and self.getInternetAansluiting().getAanwezig():
            toegang = True
            for gevangene in self.getGevangenen():
                if not gevangene.getInternetToegang:
                    toegang = False
            if toegang:
                self.getInternetAansluiting().setActive(True)
    
    def __str__(self):
        output = 'Cel [{0}]:\n'.format(self._celNr)
        output += '\tCapaciteit: {0}\n'.format(self._capaciteit)
        output += '\t{0}\n'.format(str(self.getInternetAansluiting()))
        for gevangene in self.getGevangenen():
            for lijn in str(gevangene).split('\n'):
                output += '\t{0}\n'.format(lijn)
        return output
        
    def __repr__(self):
        return self.__str__()

class Gevangenis:
    """
    Klas implementatie voor Gevangenis
    """
    def __init__(self):
        """
        Constructor voor gevangenis
        """
        self._cellen = []
    
    def getCellen(self):
        return self._cellen
    
    def addCel(self, cel):
        """
        Voeg cel toe
        Parameters
        ----------
        cel: Cel
        """
        
        self._cellen.append(cel)
    
    def removeCel(self, cel):
        self._cellen.remove(cel)
    
    # AANDACHT
    def makeMaaltijdenOverzicht(self):
        """
        Maak maaltijden overzicht
        Returns
        -------
        dict
            Overzicht van de maaltijden
        """
       
        overzicht = dict()
        # Eventueel kan je reeds het overzicht initialiseren
        # overzicht = dict({'normaal': 0, 'vegitarisch met vis': 0, 'vegitarisch zonder vis': 0, 'bijzonder': 0})
        for cel in self.getCellen():
            for gevangene in cel.getGevangenen():
                dieet_categorie = gevangene.getDieet().calculateCategorie()
                if dieet_categorie in overzicht.keys():
                    overzicht[dieet_categorie] += 1
                else:
                    overzicht[dieet_categorie] = 1
        return overzicht
    
    def __str__(self):
        """
        Geeft gevangenis object terug als string
        Returns
        -------
        str
        """
        output = "Gevangenis:\n"
        for cel in self.getCellen():
            for lijn in str(cel).split('\n'):
                output += '\t{0}\n'.format(lijn)
        return output
    
    def __repr__(self):
        return self.__str__()

def main():
    
    lisbon = Gevangene('Lisbon', Dieet(vegitarisch=True,allergieen=[],vis=True), internetToegang=True, bezoekdagen=['Maandag'])
    tokyo = Gevangene('Tokyo', Dieet(vegitarisch=True,allergieen=[], vis=False), internetToegang=False, bezoekdagen=['Dinsdag', 'Vrijdag'])
    oslo = Gevangene('Oslo', Dieet(vegitarisch=False,allergieen=['Rijst']), internetToegang=True, bezoekdagen=['Maandag'])
    professor = Gevangene('Professor', Dieet(vegitarisch=False, allergieen=['Couscous']), internetToegang=False, bezoekdagen=['Maandag'])
    rio = Gevangene('Rio', Dieet(vegitarisch=False, allergieen=['Rijst']), internetToegang=True, bezoekdagen=['Maandag'])
    berlin = Gevangene('Berlin', Dieet(vegitarisch=False), internetToegang=True, bezoekdagen=['Woensdag'])
    nairobi = Gevangene('Nairobi',Dieet(vegitarisch=True,allergieen=[], vis=True), internetToegang=True, bezoekdagen=['Woensdag'])
    
    cel1 = Cel(capaciteit=4, internetAansluiting=InternetAansluiting(True, True))
    cel2 = Cel(capaciteit=6, internetAansluiting=InternetAansluiting(False, False))
    cel3 = Cel(capaciteit=8, internetAansluiting=InternetAansluiting(True, True))
    
    gevangenis = Gevangenis()
    gevangenis.addCel(cel1)
    gevangenis.addCel(cel2)
    gevangenis.addCel(cel3)
    
    cel1.addGevangene(lisbon)
    cel1.addGevangene(tokyo)
    cel2.addGevangene(professor)
    cel3.addGevangene(oslo)
    cel3.addGevangene(rio)
    cel3.addGevangene(berlin)
    cel3.addGevangene(nairobi)
    
    print('Maaltijd overzicht:')
    print(gevangenis.makeMaaltijdenOverzicht())
    
    print(gevangenis)

    
main()