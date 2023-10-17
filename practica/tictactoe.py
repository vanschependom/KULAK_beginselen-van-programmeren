import random

bord = [
    ["","",""],
    ["","",""],
    ["","",""]
]

winnaar = ""
spelBezig = True
aanZet = 0

def genereer_nieuw_bord():

    # We loopen over de rijen (niet inclusief voor de eindwaarde!)
    for rij in range(3):
        
        lijn = ""

        # We loopen over de kolommen (ook niet inclusief voor de eindwaarde)
        for kolom in range(3):

            # De eerste kolom moet een extra lijntje hebben ervoor
            if kolom == 0: lijn += "|"

            lijn += " %1s |" % (bord[rij][kolom])
        
        # De eerste rij moet een extra lijntje hebben erboven
        if rij == 0: print(("-------------"))
        print(lijn)
        print(("-------------"))


# Controleren of een speler een horizontaal heeft veroverd
def controleer_horizontaal():

    for rij in range(0,3):

        aantalJuistRij = 0

        for kolom in range(0,3):

            if bord[rij][kolom] == bord[rij][kolom-1] and bord[rij][kolom] != "":

                aantalJuistRij += 1
        
        if aantalJuistRij == 3:
            global winnaar
            winnaar = bord[rij][0]
            return True
        
    return False

# Controleren of een speler een verticaal heeft veroverd
def controleer_verticaal():

    for kolom in range(0,3):

        aantalJuistKolom = 0

        for rij in range(0,3):
            
            if bord[rij][kolom] == bord[rij-1][kolom] and bord[rij][kolom] != "":

                aantalJuistKolom += 1
        
        if aantalJuistKolom == 3:
            global winnaar
            winnaar = bord[0][kolom]
            return True
        
    return False

# Controleren of een speler een diagonaal heeft veroverd
def controleer_diagonaal():

    aantalJuist = 0

    for i in range(0,3):

        if bord[i][i] == bord[i-1][i-1] and bord[i][i] != "":

            aantalJuist += 1

    if aantalJuist == 3:

        global winnaar
        winnaar = bord[0][0]
        return True
    
    for i in range(0,3):

        if bord[-i][-i] == bord[-i-1][-i-1] and bord[-i][-i] != "":

            aantalJuist += 1

    if aantalJuist == 3:

        winnaar = bord[2][2]
        return True
    
# Controleren of een zet valid is
def controleer_zet(x,y):

    if bord[x-1][y-1] == "" and (1 <= x <= 3) and (1 <= y <= 3):

        return True
    
    else:

        return False
    
# Main functie
def main():

    aanZet = random.randint(1,2)

    global spelBezig
    while spelBezig:

        genereer_nieuw_bord()

        inputX = int(input(f"SPELER {aanZet}:  Welke rij wil u plaatsen? (1, 2 of 3) "))
        inputY = int(input(f"SPELER {aanZet}:  Welke kolom wil u plaatsen? (1, 2 of 3) "))

        while not controleer_zet(inputX,inputY):

            print("Dat is geen goede zet. Probeer opnieuw.")
            inputX = int(input(f"SPELER {aanZet}:  Welke rij wil u plaatsen? (1, 2 of 3) "))
            inputY = int(input(f"SPELER {aanZet}:  Welke kolom wil u plaatsen? (1, 2 of 3) "))

        if aanZet == 1: bord[inputX-1][inputY-1] = "O"
        else:           bord[inputX-1][inputY-1] = "X"

        if controleer_diagonaal() or controleer_horizontaal() or controleer_verticaal():

            genereer_nieuw_bord()
            print(f"SPELER {aanZet} HEEFT GEWONNEN!")
            spelBezig = False

        else:

            if aanZet == 1: aanZet = 2
            else: aanZet = 1

main() 