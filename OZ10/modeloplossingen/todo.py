
class Taak:
    """
    Klasse voor taak
    """
    def __init__(self, omschrijving, toegewezene=None, deadline=None):
        """
        Constructor voor klasse Taak
        Parameters
        ----------
        omschrijving: str
        toegewezene: Persoon
        deadline: List(int)  # beter om gebruik te maken van de bibliotheek datetime
        """
        self._omschrijving = omschrijving
        self._status = "wachtrij"
        self._toegewezene = toegewezene
        self._deadline = deadline
        
    def get_toegewezene(self):
        """
        Getter voor toegewezene
        Returns
        -------
        Persoon
        """
        return self._toegewezene
    
    def set_toegewezene(self, toegewezene):
        """
        Setter voor toegewezene, deze kan veranderd worden
        Parameters
        ----------
        toegewezene: Persoon
        """
        self._toegewezene = toegewezene
    
    def get_status(self):
        """
        Getter voor status
        Returns
        -------
        str
        """
        return self._status
    
    def set_status(self, status):
        """
        Setter voor status
        Parameters
        ----------
        status: str
        """
        if status in ['wachtrij', 'actief', 'vervolledigd']:
            self._status = status
        else:
            print("Geen correcte invoer, status moet een van volgende opties zijn: [wachtrij, actief, vervolledigd]")
    
    def __str__(self):
        """
        Implementatie voor printen van een taak
        Returns
        -------
        str
        """
        return self._omschrijving
    
class ToDoLijst:
    """
    ToDoLijst klasse
    """
    def __init__(self):
        """
        Constructor voor de todolijst
        """
        self._taken = []
        self._personen = []
    
    def get_taken(self):
        """
        Getters van taken
        Returns
        -------
        list(Taak)
        """
        return list(self._taken)
    
    def get_personen(self):
        """
        Getter van personen
        Returns
        -------
        list(Persoon)
        """
        return list(self._personen)
    
    def voeg_taak_toe(self, taak):
        """
        Voeg taak toe aan de takenlijst
        Parameters
        ----------
        taak: Taak
        """
        self._taken.append(taak)
    
    def verwijder_taak(self, taak):
        """
        Verwijder taak van takenlijst
        Parameters
        ----------
        taak: Taak
        """
        if taak in self._taken:
            self._taken.remove(taak)
        else:
            print(f"Taak: {taak} niet op de todo lijst")
    
    def bereken_statistieken_voor_lijst_taken(self, taken):
        """
        Bereken de statistieken voor lijst van taken
        Parameters
        ----------
        taken: list(Taak)

        Returns
        -------
        dict
            Per categorie het percentage van aantal taken
        """
        statistieken = {"wachtrij": 0, "actief": 0, "vervolledigd": 0}
        for taak in taken:
            statistieken[taak.get_status()] += 1
        
        for categroie in statistieken:
            statistieken[categroie] = statistieken[categroie]/len(taken)*100
        
        return statistieken

    def print_statistieken_per_status(self, personen=None):
        """
        Druk de statistiekn af, in totaal of per persoon
        Parameters
        ----------
        personen: [None, list(Persoon)]
            Indien None worden de totaal statistieken afgedrukt, anders per persoon.
        """
        if personen is None:
            print("Totale statistiek:")
            statistieken = self.bereken_statistieken_voor_lijst_taken(self.get_taken())
            for categorie in statistieken:
                print(f" - {categorie:<20}{statistieken[categorie]:>10.02f}%")
        
        else:
            print("Persoonlijke statistiek:")
            for persoon in personen:
                # Merk op dat je hier ook gewoon print(persoon) kan zetten
                # Aangezien __str__ geimplementeerd is voor de klasse Persoon.
                print(f"{persoon.get_naam()}")
                statistieken = self.bereken_statistieken_voor_lijst_taken(self.get_taken())
                for categorie in statistieken:
                    print(f" - {categorie:<20}{statistieken[categorie]:>10.02f}%")
        
    
class Persoon:
    """
    Persoon klasse
    """
    def __init__(self, naam):
        """
        Constructor voor de klasse Persoon
        Parameters
        ----------
        naam: str
        """
        self._naam = naam
    
    def get_naam(self):
        """
        Getter voor attribuut naam
        Returns
        -------
        str
        """
        return self._naam
    
    def __str__(self):
        return self._naam
    

if __name__ == '__main__':
    
    todos = ToDoLijst()
    casper = Persoon("Casper")
    melchior = Persoon("Melchior")
    balthasar = Persoon("Balthasar")
    
    taak1 = Taak("Gras afrijden", casper)
    todos.voeg_taak_toe(taak1)
    taak2 = Taak("Ramen kuisen", melchior)
    todos.voeg_taak_toe(taak2)
    taak3 = Taak("Spagetti maken", balthasar)
    taak3.set_status('actief')
    todos.voeg_taak_toe(taak3)
    
    todos.print_statistieken_per_status()
    
    
    