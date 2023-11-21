

def leesMagischVierkantIn(bestandsnaam):
    """
    Inlezen van magisch vierkant vanuit een tekstbestand.
    elementen moeten worden gescheiden door tabs, rijen door enters.
    Parameters
    ----------
    bestandsnaam : str
        bestandsnaam van het magisch vierkant
    Returns
    -------
    list
        geeft het magisch vierkant terug in lijst van lijsten. elementen zijn integers.
    """
    magisch_vierkant = []
    
    # de with context zorgt voor correct afsluiten van de file na het lezen
    # Dit is een alternatief voor fid=open() ... fid.close()
    with open(bestandsnaam, "r") as fid:
        for line in fid:
            getallen = line.split("\t")
            magisch_vierkant_regel = []
            for getal in getallen:
                magisch_vierkant_regel.append(int(getal))
            magisch_vierkant.append(magisch_vierkant_regel)
    
    return magisch_vierkant

def controleMagischVierkant(magisch_vierkant):
    """
    Controlleer of de input matrix een magisch vierkant is.
        - som van alle rijen, kolomen en diagonalen gelijk zijn aan elkaar
        - alle getallen van 1 - grote van het vierkant gebruikt zijn.
    Parameters
    ----------
    magisch_vierkant : list
        Magisch vierkant is een lijst van lijsten
    Returns
    -------
    bool
        True als het vierkant magisch is
    """
    
    dim_0 = len(magisch_vierkant)
    dim_1 = set()

    for rij in magisch_vierkant:
        dim_1.add(len(rij))
    if len(dim_1) > 1:
        print("Dimensies kloppen niet, geen vierkant")
        # Aangezien de dimensies niet gelijk zijn, hoeven we de rest niet meer te verifieren en kunnen we returnen.
        return False

    else:
        dim_1 = dim_1.pop()
        if dim_0 != dim_1:
            print("Dimensies kloppen niet, geen vierkant")
            return False

    
    # CHECK ALLE GETALLEN
    getallen = list(range(1, (dim_0*dim_1) + 1))
    for i in range(dim_0):
        for j in range(dim_1):
            getallen.remove(magisch_vierkant[i][j])
    
    if len(getallen) > 0:
        print(f"Niet alle getallen (0-{dim_0*dim_1}) werden gebruikt.")
        return False

    # RIJ
    # Bereken som van alle rijen:
    som_rijen = []
    for rij in magisch_vierkant:
        som_rijen.append(sum(rij))
    
    # controle of som elke rij gelijk is aan eerste rij
    for sr in som_rijen[1:]:
        if som_rijen[0] != sr:
            print(f"De som van de rijen is niet overal gelijk")
            return False

    # KOLOM
    # Bereken som van alle rijen:
    som_kolommen = []
    for j in range(dim_1):
        som_kolom = 0
        for i in range(dim_0):
            som_kolom += magisch_vierkant[i][j]
        som_kolommen.append(som_kolom)
    
    # Alternatieve manier om te verifieren dat alle elementen gelijk zijn.
    # for lus is binnen de if verificatie getrokken
    if not all(som_kolommen[0] == sk for sk in som_kolommen):
        print(f"De som van de kolommen is niet overal gelijk")
        return False
    
    # DIAGONAAL
    diag_0 = 0
    for i in range(dim_0):
        diag_0 += magisch_vierkant[i][i]
    
    diag_1 = 0
    for i in range(dim_0):
        diag_1 += magisch_vierkant[i][(dim_1-1)-i]
    
    if diag_0 != diag_1:
        print("De som van de diagonalen kloppen niet.")
        return False
    
    if diag_0 != som_rijen[0] or diag_0 != som_kolommen[0]:
        print("De som van rijen, kolomen en diagonalen zijn niet gelijk aan elkaar")
        return False
    
    # Indien we hier geraakt zijn in de functie zijn we zeker dat alle checks correct waren
    # en we niet vroegtijdig hebben gereturnt.
    return True
    
if __name__ == '__main__':
    
    mv_bestanden = ["magisch_vierkant.txt", "geen_magisch_vierkant.txt"]
    
    for mv_bestand in mv_bestanden:
    
        magisch_vierkant = leesMagischVierkantIn(mv_bestand)
        if controleMagischVierkant(magisch_vierkant):
            print(f"De file {mv_bestand} bevat een magisch vierkant")
        else:
            print(f"De file {mv_bestand} heeft een probleem in zn magisch vierkant")
