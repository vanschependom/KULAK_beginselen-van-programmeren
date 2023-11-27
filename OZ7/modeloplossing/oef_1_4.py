
def genereerPaden(startpunt, eindpunt, buurmatrix, huidig_pad=[]):
    """
    Genereer alle paden tussen startpunt en eindpunt
    Parameters
    ----------
    startpunt: int
        index van startpunt op basis van de buurmatrix
    eindpunt: int
        index van het einpunt op basis van de buurmatrix
    buurmatrix: list
        matrix met de gewichten van bogen in de graaf
    huidig_pad: list
        Het reeds afgelegde pad
    Returns
    -------
    list
        lijst van tuples met de afstand en de paden
    """
    # Basisgeval
    if startpunt == eindpunt:
        huidig_pad.append(eindpunt)
        # output bevat de afstand van het pad met een lijst van het pad
        return [(0, huidig_pad)]
    
    output_paden = []

    huidig_pad.append(startpunt)
    
    # loop over alle buren van het huidig punt
    for buur_idx, buur_afstand in enumerate(buurmatrix[startpunt]):
        # elke indien de afstand bestaat (> 0 en niet None) is de buur gedefinieerd
        if buur_afstand is not None and buur_afstand != 0 and buur_idx not in huidig_pad:
            # genereer de paden vanaf de buur tot het eindpunt recursief
            volgende_paden = genereerPaden(buur_idx, eindpunt, buurmatrix,  list(huidig_pad))
            for afstand, vpad in volgende_paden:
                # update voor elk pad de afstand en het pad
                afstand += buur_afstand
                output_paden.append((afstand, vpad))

    return output_paden
    
if __name__ == '__main__':
    buurmatrix = [[0, 1, 2, 1, None, None, None],
                  [1, 0, 1, None, 5, None, None],
                  [2, 1, 0, None, 3, 1, None],
                  [1, None, None, 0, None, 5, None],
                  [None, 5, 3, 0, None, None, 1],
                  [None, None, None, 5, None, 0, 2],
                  [None, None, None, None, 1, 2, 0]]
    
    paden = genereerPaden(0, 6, buurmatrix)
    for afstand, pad in paden:
        out_str = f"{afstand}: "
        for element in pad:
            out_str += f"{chr(65+element)}"
        print(out_str)