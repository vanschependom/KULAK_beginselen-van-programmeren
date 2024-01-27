
## klasse student
# eigenschappen: voornaam, familienaam, lijst van examens
class Student:
    """
    klasse student
    eigenschappen: voornaam, familienaam, lijst van examens
    """

    def __init__(self, voornaam, familienaam):
        """
        Constructor:
        Parameters
        ----------
        voornaam: str
        familienaam: str
        """
        self._voornaam = voornaam
        self._familienaam = familienaam
        self._examens = []
    
    def getVoornaam(self):
        """
        getter voor attribuut voornaam
        Returns
        -------
        str
        """
        return self._voornaam
    
    
    def getFamilienaam(self):
        """
        getter voor attribuut familienaam
        Returns
        -------
        str
        """
        return self._familienaam
    
    
    def addExamen(self, examen):
        """
        Voeg examen toe aan de examenlijst
        """
        self._examens.append(examen)

    def berekenTotaleScore(self):
        """
        geeft de totale score van de student weer, gewogen op het aantal studiepunten
        Returns
        -------
        float:
            gewogen score
        """
        totaleStudiePunten = 0
        totaleSomGewogen = 0
        for examen in self._examens:
            totaleSomGewogen += examen.berekenScore()*examen.getVak().getStudiePunten()
            totaleStudiePunten += examen.getVak().getStudiePunten()
        return totaleSomGewogen/totaleStudiePunten
    
    def __str__(self):
        """
        Output voor het printen van Student
        Returns
        -------
        str
        """
        output = 'Student: {0} {1}\t{2}'.format(self._voornaam, self._familienaam, self.getTotaleScore())
        return output
    

class Examen:
    
    """
    Klasse Examen
    eigenschappen: vak, scoreTheorie, scoreOefeningen
    """
    
   
    def __init__(self, vak, theorie, oefeningen):
        """
        Constructor van Examen
        Parameters
        ----------
        vak: Vak
        theorie: float
            punten voor het theorie gedeelte
        oefeningen: float
            punten voor het oefeningen gedeelte
        """
        self._vak = vak
        self.setScoreTheorie(theorie)
        self.setScoreOefeningen(oefeningen)
    
    def getVak(self):
        """
        Getter voor vak
        Returns
        -------
        Vak
        """
        return self._vak
    
    def getScoreThoerie(self):
        """
        Getter voor score theorie
        Returns
        -------
        float
        """
        return self._scoreTheorie

    def getScoreOefeningen(self):
        """
        Getter voor score oefeningen
        Returns
        -------
        float
        """
        return self._scoreOefeningen
    

    def setScoreTheorie(self, score):
        """
        Setter voor score theorie
        Parameters
        ----------
        score: float
        """
        if score > 0:
            self._scoreTheorie = score
        else:
            self._scoreTheorie = 0
    

    def setScoreOefeningen(self, score):
        """
        Setter voor score oefeningen
        Parameters
        ----------
        score: float
        """
        if score > 0:
            self._scoreOefeningen = score
        else:
            self._scoreOefeningen = 0
    

    def berekenScore(self):
        """
        Bereken score voor het examen
        Returns
        -------
        float
            score van het examen
        """
        return (self._scoreTheorie * self._vak.getWegingsFactor()) + (self._scoreOefeningen * (1-self._vak.getWegingsFactor()))

class Vak:
    
    """
    Klasse Vak
    eigenschappen: naam, studiepunten, wegings factor
    """
    
    def __init__(self, naam, studiePunten,wegingsFactor):
        """
        Constructor
        Parameters
        ----------
        naam: str
             de naam van het vak
        studiePunten: int
        wegingsFactor: float
            het percentage van de totale score die wordt ingenomen door het theorie deel
        """
        self.setNaam(naam)
        self.setStudiePunten(studiePunten)
        self.setWegingsFactor(wegingsFactor)
    

    def getNaam(self):
        """
        getter voor Naam
        Returns
        -------
        str
        """
        return self._naam
    
    
    def getStudiePunten(self):
        """
        Getter voor studiepunten
        Returns
        -------
        int
        """
        return self._studiePunten
    
    
    def getWegingsFactor(self):
        """
        Getter voor wegings factor
        Returns
        -------
        float
        """
        return self._wegingsFactor
    
    def setNaam(self, naam):
        """
        Setter voor Naam
        Parameters
        ----------
        naam: str
        """
        self._naam = naam
    
    
    def setStudiePunten(self,studiePunten):
        """
        Setter voor studiepunten
        Parameters
        ----------
        studiePunten: int
        """
        self._studiePunten = studiePunten
    
    
    def setWegingsFactor(self, wegingsFactor):
        """
        Setter voor Wegingsfactor
        Parameters
        ----------
        wegingsFactor: float
        """
        self._wegingsFactor = wegingsFactor
        
        
        
