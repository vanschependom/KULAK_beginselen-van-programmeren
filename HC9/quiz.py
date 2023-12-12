import string
##
# Deze module stelt quizvragen voor.
#


class Vraag:
    '''
    Algemene superklasse die vragen voorstelt.
    Een vraag bestaat (minstens) uit een tekst en een antwoord.
    '''

    def __init__(self, tekst, antwoord):
        '''
        Maakt een nieuwe vraag met gegeven tekst en antwoord.
        Parameters
        ----------
        tekst : str
        antwoord : str
        '''
        self._tekst = tekst
        self._antwoord = antwoord

    def setTekst(self,t):
        '''
        Stelt een nieuwe tekst in voor deze vraag.
        Parameters
        ----------
        t : str
        '''
        self._tekst = t

    def setAntwoord(self, a):
        '''
        Stelt een nieuw correct antwoord in voor deze vraag.
        Parameters
        ----------
        a : str
        '''
        self._antwoord = a

    def checkAntwoord(self,antwoord):
        '''
        Checkt of het gegeven antwoord correct is.
        Leestekens en witruimte worden genegeerd, niet hoofdlettergevoelig.
        Parameters
        ----------
        antwoord : str
        Returns
        -------
        bool
        '''
        return self._antwoord.lower().strip(string.punctuation) == antwoord.lower().strip(string.punctuation)

    def getVraagString(self):
        '''
        Geeft een propere string terug met daarin de vraagstelling.
        Returns
        -------
        str
        '''
        return self._tekst


class Meerkeuzevraag(Vraag):
    '''
    Klasse die meerkeuzevragen voorstelt.
    Subklasse van Vraag. Als extra eigenschap is er
    een lijst mogelijke antwoorden
    '''

    def __init__(self,tekst,opties,antwoordNr):
        '''
        Maakt een nieuwe meerkeuzevraag aan met gegeven tekst, opties en
        correct antwoordNr (de index van het juiste antwoord in de opties)
        Parameters
        ----------
        tekst : str
        opties : [str]
        antwoordNr : int
        '''
        super().__init__(tekst,opties[antwoordNr])
        self._opties = opties

    def voegOptieToe(self,antwoord,correct=False):
        '''
        Voegt een nieuwe optie toe aan de meerkeuzevraag.
        Parameters
        ----------
        antwoord : str
            De nieuwe optie
        correct : bool (default = False)
            boolean die aangeeft of de nieuwe optie het juiste antwoord is
        '''
        self._opties.append(antwoord)
        if correct:
            self.setAntwoord(self._opties[-1])

    def getVraagString(self):
        '''
        Geeft een propere string terug met daarin de vraagstelling.
        Overschrijft de methode uit de superklasse.
        De inhoud uit de superklasse wordt wel gebruikt, de opties
        worden eraan toegevoegd.
        Returns
        -------
        str
        '''
        vraag = super().getVraagString() + "\n"
        vraag += "\tMogelijke antwoorden:\n"
        nr = 1
        for optie in self._opties:
            vraag += "\t\t"+str(nr)+":\t"+optie+"\n"
            nr += 1
        return vraag

    def checkAntwoord(self,antwoord):
        '''
        Checkt of het gegeven antwoord correct is.
        Er zijn twee mogelijkheden: ofwel geeft men het tekstueel
        antwoord in, ofwel kiest men een cijfer.
        Deze methode zet het cijfer om naar het overeenkomstig
        tekstueel antwoord en roept daarna de methode uit
        de superklasse op.
        Parameters
        ----------
        antwoord : str
            tekstueel antwoord, of een string met het cijfer
        Returns
        -------
        bool
        '''
        if antwoord.isnumeric():
            antwoord = self._opties[int(antwoord)-1]
        return super().checkAntwoord(antwoord)


class NumeriekeVraag(Vraag):
    '''
    Klasse die numerieke vragen voorstelt.
    Hierbij wordt het antwoord als correct aanzien indien
    het voldoende dicht bij het opgegeven antwoord ligt.
    Er is dus een extra eigenschap die deze foutenmarge bijhoudt.
    '''

    def __init__(self,tekst,antwoord,foutmarge = 0.01):
        '''
        Maakt een nieuwe numerieke vraag aan.
        Parameters
        ----------
        tekst : str
        antwoord : float
        foutmarge : float (default = 0.01)
        '''
        super().__init__(tekst,str(antwoord))
        self._foutmarge = foutmarge

    def checkAntwoord(self,antwoord):
        '''
        Checkt of het gegeven antwoord correct is.
        Correct betekent dat het binnen de aanvaarde
        foutmarge ligt.
        Parameters
        ----------
        antwoord : str
        Returns
        -------
        bool
        '''
        # _antwoord uit de superklasse is een string!
        # parameter antwoord is ook een string!
        juistAntwoord = float(self._antwoord)
        min = juistAntwoord - self._foutmarge
        max = juistAntwoord + self._foutmarge
        return min <= float(antwoord) <= max