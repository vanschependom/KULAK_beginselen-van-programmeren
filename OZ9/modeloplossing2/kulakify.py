
class Lied:
    """
    Klasse voor Lied
    """
    def __init__(self, naam, track_id, naam_muzikant):
        """
        Consturctor voor lied
        Parameters
        ----------
        naam: str
        track_id: int
            Volgnummer op het album
        naam_muzikant: str
        """
        self._naam = naam
        self._id = None
        self._track_id = track_id
        self._naam_muzikant = naam_muzikant
        self._nmb_of_likes = 0
    
    def get_naam(self):
        return self._naam
        
    def get_id(self):
        return self._id
    
    def set_id(self, nmb):
        self._id = nmb
    
    def get_naam_muzikant(self):
        return self._naam_muzikant
    
    def get_nmb_of_likes(self):
        return self._nmb_of_likes
    
    def add_like(self):
        self._nmb_of_likes += 1
    
    def subtract_like(self):
        self._nmb_of_likes -= 1
    
    def __str__(self):
        return f"{self._naam}"


class Muzieklijst:
    """
    Abstracte klasse voor Muzieklijst
    """
    def __init__(self, naam, liederen=None):
        """
        Constructor voor klasse Muzieklijst
        Parameters
        ----------
        naam: str
        liederen: list(Lied)
        """
        if liederen is None:
            liederen = list()
        self._naam = naam
        self._liederen = liederen
        
    def get_naam(self):
        return self._naam
    
    def get_liederen(self):
        return list(self._liederen)
    
    def __str__(self):
        return f"{self._naam}"

class Album(Muzieklijst):
    """
    Klasse voor Album
    """
    def __init__(self, naam, liederen):
        """
        Constructor voor Album
        Parameters
        ----------
        naam: str
        liederen: list(Lied)
        """
        super().__init__(naam, liederen)

        
class Afspeellijst(Muzieklijst):
    """
    Klasse voor Afspeellijst
    """
    def __init__(self, naam):
        """
        Constructor voor Afspeellijst
        Parameters
        ----------
        naam: str
        """
        super().__init__(naam)
        self._nmb_songs = 0
    
    def voeg_lied_toe(self, lied):
        self._liederen.append(lied)
        self._nmb_songs += 1
    
    def verwijder_lied(self, lied):
        if lied in self._liederen:
            self._liederen.remove(lied)
            self._nmb_songs -= 1
        else:
            print(f"Lied {lied} niet aanwezig in afspeellijst")
        
class Persoon:
    """
    Abstracte klasse voor een persoon
    """
    def __init__(self, naam, nmb):
        """
        Constructor voor klasse persoon
        Parameters
        ----------
        naam: str
        nmb: int
        """
        self._naam = naam
        self._id = nmb
    
    def get_id(self):
        return self._id
    
    def get_naam(self):
        return self._naam
    
    def __str__(self):
        return self._naam
    
class Muzikant(Persoon):
    """
    Klasse voor Muzikanten
    """
    def __init__(self, naam, nmb):
        """
        Constructor voor de klasse Muzikanten
        Parameters
        ----------
        naam: str
        nmb: int
        """
        super().__init__(naam, nmb)
        self._albums = []
        self._singles = []
        self._liederen = []
    
    def voeg_album_toe(self, album):
        self._albums.append(album)
    
    def voeg_single_toe(self, single):
        self._singles.append(single)
    
    def voeg_lied_toe(self, lied):
        self._liederen.append(lied)
    
    def get_liederen(self):
        return list(self._liederen)
    
    def get_albums(self):
        return list(self._albums)
    
    def get_singles(self):
        return list(self._singles)
    
    def print_oevre(self):
        print("ALBUMS:")
        for album in self._albums:
            print(f"{album}")
            for lied in album:
                print(f"\t{lied}")
        print("SINGLES")
        for single in self._singles:
            print(f"\t{single}")
    
class Muziekliefhebber(Persoon):
    """
    Klasse voor Muziekliefhebber
    """
    def __init__(self, naam, nmb):
        """
        Constructor voor Muziekliefhebber
        Parameters
        ----------
        naam: str
        nmb: int
        """
        super().__init__(naam, nmb)
        self._afspeellijsten = []
    
    def voeg_afspeellijst_toe(self, afspeellijst):
        self._afspeellijsten.append(afspeellijst)
    
    def verwijder_afspeellijst(self, afspeellijst):
        if afspeellijst in self._afspeellijsten:
            self._afspeellijsten.remove(afspeellijst)
        else:
            print(f"Afspeellijst {afspeellijst} niet bestaande")
    

class Kulakify:
    """
    Klasse Kulakify
    """
    def __init__(self):
        """
        Constructor voor Kulakify
        De klasse creert een overzicht van alle muziekanten, muziekliefhebbers en liedjes.
        """
        self._liederen = []
        self._muzikanten = dict()
        self._muziekliefhebbers = dict()
        self._nmb_liederen = 0
    
    def voeg_lied_toe(self, lied):
        if lied not in self._liederen:
            self._liederen.append(lied)
            lied.set_id(self._nmb_liederen)
            self._nmb_liederen += 1
        else:
            print(f"Lied {lied} reeds in de catalogus")
        
    def voeg_muzikant_toe(self, muzikant):
        """
        Functie voor het toevoegen van een muziekant aan kulakify
        Automatisch worden al zijn liederen ook toegevoegd.
        Parameters
        ----------
        muzikant: Muzikant
        """
        self._muzikanten[muzikant.get_id()] = muzikant
        for lied in muzikant.get_liederen():
            self.voeg_lied_toe(lied)
    
    def voeg_muziekliefhebber_toe(self, muziekliefhebber):
        self._muziekliefhebbers[muziekliefhebber.get_id()] = muziekliefhebber
    
    def print_catalogus(self):
        for muzikant_id in self._muzikanten:
            muzikant = self._muzikanten[muzikant_id]
            print(muzikant)
            muzikant.print_oevre()
            
    
if __name__ == "__main__":
    the_police = Muzikant("The Police", 1)
    roxanne = Lied("Roxanne", 1, "The Police")
    the_police.voeg_single_toe(roxanne)
    kulakify = Kulakify()
    
    kulakify.voeg_muzikant_toe(the_police)
    kulakify.print_catalogus()

