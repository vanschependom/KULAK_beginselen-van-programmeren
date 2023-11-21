
def swap(lijst):
    """
    Verwisselt het eerste en laatste element van een lijst
    Parameters
    ----------
    lijst : list
        de input lijst
    Returns
    -------
    list
        Geeft de lijst terug met gewisselde elementen
    """
    laatste_element = lijst[-1]
    lijst[-1] = lijst[0]
    lijst[0] = laatste_element
    return lijst

def shift(lijst):
    """
    schuit alle elementen van een lijst een plaats op
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug waarvan element een plaats zijn opgeschoven
    """
    laatste_element = lijst[-1]
    lijst.insert(0, laatste_element)
    return lijst[:-1]

def shift_alt(lijst):
    """
    schuit alle elementen van een lijst een plaats op
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug waarvan element een plaats zijn opgeschoven
    """
    lijst.insert(0, lijst.pop())
    return lijst

def shift_alt_alt(lijst):
    """
    schuit alle elementen van een lijst een plaats op
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug waarvan element een plaats zijn opgeschoven
    """
    out_lijst = [lijst[-1]]
    for element in lijst[:-1]:
        out_lijst.append(element)
    return out_lijst

def replaceEvenWithZeros(lijst):
    """
    Vervang van een lijst elke even getal door 0
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug met nullen op plaat van even getallen
    """
    for idx in range(len(lijst)):
        if lijst[idx] % 2 == 0:
            lijst[idx] = 0
    return lijst

def replaceEvenWithZeros_alt(lijst):
    """
    Vervang van een lijst elke even getal door 0
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug met nullen op plaat van even getallen
    """
    
    # bekijk alle verschillende elementen in de lijst
    set_lijst = set(lijst)
    for getal in set_lijst:
        # als getal even is en verschillend van nul veranderen we het getal in de lijst
        if getal % 2 == 0 and getal != 0:
            while getal in lijst:
                # we nemen de index van het getal in de lijst, en veranderen de lijst op die plaats in een nul
                lijst[lijst.index(getal)] = 0
    return lijst
    

def moveEvenToFront(lijst):
    """
    Verplaats alle even getallen van een lijst naar begin.
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Lijst met vooraan de even getallen
    """
    even_lijst = []
    oneven_lijst = []
    for getal in lijst:
        if getal % 2 == 0:
            even_lijst.append(getal)
        else:
            oneven_lijst.append(getal)
    
    even_lijst.extend(oneven_lijst)
    output_lijst = even_lijst
    
    return output_lijst


def moveEvenToFront_alt(lijst):
    """
    Verplaats alle even getallen van een lijst naar begin.
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Lijst met vooraan de even getallen
    """
    idx = 0
    pos_idx = 0
    # We werken hiet met while aangezien we in de lus de lijst aanpassen
    # for getal in lijst zou problemen veroorzaken.
    while idx < len(lijst):
        # als getal even is verwijderen we het van de locatie
        # en voegen we het in na het laatst gekend even getal vooraan de lijst
        if lijst[idx] % 2 == 0:
            getal = lijst.pop(idx)
            lijst.insert(pos_idx, getal)
            pos_idx += 1
            
        idx += 1
    return lijst

def reverse(lijst):
    """
    Keer de volgorde van een lijst om
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug met omgekeerde volgorde
    """
    # Gebruik van de slice operator
    omgekeerde_lijst = lijst[::-1]
    return omgekeerde_lijst


def reverse_alt(lijst):
    """
    Keer de volgorde van een lijst om
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug met omgekeerde volgorde
    """
    # gebruik ingebouwde functie
    lijst.reverse()
    return lijst

def reverse_alt_alt(lijst):
    """
    Keer de volgorde van een lijst om
    Parameters
    ----------
    lijst : list
        input lijst
    Returns
    -------
    list
        Geeft lijst terug met omgekeerde volgorde
    """
    omgekeerde_lijst = []
    idx = len(lijst)-1
    while idx >= 0:
        omgekeerde_lijst.append(lijst[idx])
        idx -= 1
    return omgekeerde_lijst


if __name__ == "__main__":
    
    lijst = [8, 8, 23, 14, 11, 5, 7, 4]
    print(f"originele lijst: {lijst}")
    print(f"swap: {swap(list(lijst))}")
    print(f"shift: {shift(list(lijst))}")
    print(f"shift alt: {shift_alt(list(lijst))}")
    print(f"shift alt alt: {shift_alt_alt(list(lijst))}")
    print(f"replace: {replaceEvenWithZeros(list(lijst))}")
    print(f"replace alt : {replaceEvenWithZeros_alt(list(lijst))}")
    print(f"move even to front :{moveEvenToFront(list(lijst))}")
    print(f"move even to front alt :{moveEvenToFront_alt(list(lijst))}")
    print(f"reverse : {reverse(list(lijst))}")
    print(f"reverse alt : {reverse_alt(list(lijst))}")
    print(f"reverse alt alt : {reverse_alt_alt(list(lijst))}")

