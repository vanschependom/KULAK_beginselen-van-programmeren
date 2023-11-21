
global ROM_SYMB_WAARDE
ROM_SYMB_WAARDE = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}

def verifieerRomeinsCijfer(romeins_cijfer):
    """
    De functie kijkt na of het input romeins cijfer correct geformateerd is.
    Parameters
    ----------
    romeins_cijfer : str
        romeins input cijfer
    Returns
    -------
    bool
        True als romeins cijfer correct formaat heeft
    """
    
    correct_format = True
    
    # verifieer geen 3 opeenvolgende zelfde getallen
    vorig_cijfer = None
    counter = 0
    for cijfer in romeins_cijfer:
        if cijfer == vorig_cijfer:
            counter += 1
        else:
            counter = 0
            vorig_cijfer = cijfer
        
        if counter > 3:
            # Eventueel kan je hier al meteen returnen met False
            correct_format = False
    
    # Twee opeenvolgende kleinere getallen
    idx = 0
    while idx < len(romeins_cijfer) - 2:
        if ROM_SYMB_WAARDE[romeins_cijfer[idx]] < ROM_SYMB_WAARDE[romeins_cijfer[idx + 1]] and \
            ROM_SYMB_WAARDE[romeins_cijfer[idx + 1]] <= ROM_SYMB_WAARDE[romeins_cijfer[idx + 2]]:
            correct_format = False
            
    return correct_format

def decodeerRomeinsCijfer(romeins_cijfer):
    """
    Decodeer een gegeven romeins cijfer
    Parameters
    ----------
    romeins_cijfer : str
        Input romeins cijfer
    Returns
    -------
    int
        Geeft de decimale getal waarde terug van het romeins getal
    """
    romeins_cijfer = romeins_cijfer.upper()
    
    curr_idx = 0
    next_idx = curr_idx + 1
    waarde = 0
    
    while curr_idx < len(romeins_cijfer)-1:
        curr_waarde = ROM_SYMB_WAARDE[romeins_cijfer[curr_idx]]
        next_waarde = ROM_SYMB_WAARDE[romeins_cijfer[next_idx]]

        if curr_waarde < next_waarde:
            waarde += next_waarde-curr_waarde
            curr_idx = next_idx + 1
            next_idx = curr_idx + 1
        else:
            waarde += curr_waarde
            curr_idx = next_idx
            next_idx = curr_idx + 1
    
    if curr_idx == len(romeins_cijfer)-1:
        waarde += ROM_SYMB_WAARDE[romeins_cijfer[curr_idx]]
        
    return waarde


if __name__ == '__main__':
    print(f"IX == {decodeerRomeinsCijfer('IX')}")
    print(f"MMXXII == {decodeerRomeinsCijfer('MMXXII')}")


