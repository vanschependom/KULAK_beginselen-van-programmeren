import math

class Cirkel:
    
    def __init__(self, straal):
        """
        Constructor voor klasse cirkel
        Parameters
        ----------
        straal: float
            Straal van de cirkel
        """
        self._straal = straal
    
    def getStraal(self):
        """
        getter voor straal
        Returns
        -------
        flaot:
            geeft straal terug
        """
        return self._straal
    
    def berekenOmtrek(self):
        """
        bereken omtrek
        Returns
        -------
        float:
            De omtrek van de cirkel
        """
        return 2 * math.pi * self._straal
    
    def berekenOppervlakte(self):
        """
        bereken de oppervlakte van de cirkel
        Returns
        -------
        float:
            De oppervlakte van de cirkel
        """
        return math.pi * self._straal**2





class Cilinder:
    """
    Klasse van een Cilinder
    """
    def __init__(self, straal, hoogte):
        """
        Constructor van de cilinder
        Parameters
        ----------
        straal: float
            straal de cirkel die het grondoppervlak definieerd
        hoogte: float
            hoogte van de cilinder
        """
        self._grondOppervlak = Cirkel(straal)
        self._hoogte = hoogte
    
    def berekenOppervlakte(self):
        """
           bereken de oppervlakte van de Cilinder
           Returns
           -------
           float:
               De oppervlakte van de Cilinder
        """
        return 2 * self._grondOppervlak.berekenOppervlakte() + self._grondOppervlak.berekenOmtrek() * self._hoogte
    
    def berekenVolume(self):
        """
           bereken de volume van de Cilinder
           Returns
           -------
           float:
               De volume van de Cilinder
        """
        return self._grondOppervlak.berekenOppervlakte() * self._hoogte

