
class Handeling:
    def __init__(self, naam):
        self._naam = naam

    def get_naam(self):
        return self._naam

class Deeltaak:
    def __init__(self, handeling, standaardtijd, aantal):
        self._handeling = handeling
        self._standaardtijd = standaardtijd
        self._aantal = aantal
    
    def get_handeling(self):
        return self._handeling
    
    def get_standaardtijd(self):
        return self._standaardtijd
    
    def get_aantal(self):
        return self._aantal
    
class Stielman:
    def __init__(self, naam, ervaringen):
        self._naam = naam
        self._ervaringen = ervaringen
    
    def get_ervaringen(self):
        return dict(self._ervaringen)
    
    def get_naam(self):
        return self._naam
    
    def voeg_ervaring_toe(self, handeling, ervaring):
        self._ervaringen[handeling] = ervaring
    
    # Maakt het mogelijk de ervaring van de stielmannen te vergelijken.
    # Eventueel schrijf je een aparte klasse voor de ervaring en implementeer je op die klasse __lt__ en __gt__ methodes
    def get_ervaring_voor_handeling_quantitatief(self, handeling):
        if handeling not in self._ervaringen:
            return None
        else:
            if self._ervaringen[handeling].upper() == "BEGINNER":
                return 0
            elif self._ervaringen[handeling].upper() == "ERVAREN":
                return 1
            elif self._ervaringen[handeling].upper() == "EXPERT":
                return 2
        

class Project:
    def __init__(self, deeltaken, verhoogde_afwerking, toewijzing):
        self._deeltaken = deeltaken
        self._verhoogde_afwerking = verhoogde_afwerking
        self._toewijzing = toewijzing
    
    def get_deeltaken(self):
        return list(self._deeltaken)
        
    def get_verhoogde_afwerking(self):
        return self._verhoogde_afwerking
    
    def get_toewijzing(self):
        return dict(self._toewijzing)
    
    def set_toewijzing(self, toewijzing):
        self._toewijzing = toewijzing
    
    def bereken_doorlooptijd(self):
        doorlooptijd = 0
        for deeltaak in self._toewijzing:
            toegewezene = self._toewijzing[deeltaak]
            ervaring = toegewezene.get_ervaringen()[deeltaak]
            if ervaring.upper() == "BEGINNER":
                doorlooptijd += deeltaak.get_standaardtijd() * 1.5
            elif ervaring.upper() == "ERVAREN":
                doorlooptijd += deeltaak.get_standaardtijd()
            elif ervaring.upper() == "EXPERT":
                doorlooptijd += deeltaak.get_standaardtijd() * 0.75
            
        if self._verhoogde_afwerking:
            doorlooptijd *= 4/3
        
        return doorlooptijd

class Atelier:
    def __init__(self, projecten, stielmannen):
        self._projecten = projecten
        self._stielmannen = stielmannen
        
    def get_projecten(self):
        return list(self._projecten)
    
    def get_stielmannen(self):
        return list(self._stielmannen)
    
    def zoek_toewijzing_voor_minimale_doorlooptijd(self, project):
        # Hergebruik zoveel mogelijk bestaande functionaliteit
        if not self.ervaring_beschikbaar(project):
            return None
        
        toekenning = dict()
        
        for deeltaak in project.get_deeltaken():
            beste_stielman = None
            for stielman in self._stielmannen:
                if deeltaak.get_handeling() in stielman.get_ervaringen():
                    if project.get_verhoogde_afwerking():
                        if stielman.get_ervaringen()[deeltaak.get_handeling()].upper() == "EXPERT":
                            beste_stielman = stielman
                            break
                    else:
                        if stielman.get_ervaringen()[deeltaak.get_handeling()].upper() == "EXPERT":
                            beste_stielman = stielman
                            break
                            
                        if beste_stielman is None:
                            beste_stielman = stielman
                        elif stielman.get_ervaring_voor_handeling_quantitatief(deeltaak.get_handeling()) > \
                                beste_stielman.get_ervaring_voor_handeling_quantitatief(deeltaak.get_handeling()):
                            beste_stielman = stielman
            toekenning[deeltaak] = beste_stielman
        
        project.set_toewijzing(toekenning)
        # De minimale doorlooptijd kan dan berekend worden aan de hand van de calculate_doorlooptijd op de klas Project.
        return project
    
    def ervaring_beschikbaar(self, project):
        for deeltaak in project.get_deeltaken():
            deeltaak_ervaring_beschikbaar = False
            for stielman in self._stielmannen:
                if deeltaak.get_handeling() in stielman.get_ervaringen():
                    if project.get_verhoogde_afwerking():
                        if stielman.get_ervaringen()[deeltaak.get_handeling()].upper() == "EXPERT":
                            deeltaak_ervaring_beschikbaar = True
                            break
                    else:
                        deeltaak_ervaring_beschikbaar = True
                        break
            # Indien een deeltaak ervaring niet beschikbaar is geven we false terug
            if not deeltaak_ervaring_beschikbaar:
                return False
        # Indien we elke deeltaak overlopen hebben, en elke deeltaak beschikbaar was kunnen we true terug geven
        return True
        