import random
import time

BORD_GROOTTE = 3
bord = [["" for i in range(BORD_GROOTTE)] for i in range(BORD_GROOTTE)]

def main():

    spelBezig = True
    gebruikerAanzet = True

    while spelBezig:

        genereer_nieuw_bord()

        if gebruikerAanzet:

            inputX = int(input(f"Welke rij wil u plaatsen? (1, 2 of 3) "))
            inputY = int(input(f"Welke kolom wil u plaatsen? (1, 2 of 3) "))

            while not zet_geldig(inputX,inputY):

                print("Dat is geen goede zet. Probeer opnieuw.")
                inputX = int(input(f"Welke rij wil u plaatsen? (1, 2 of 3) "))
                inputY = int(input(f"Welke kolom wil u plaatsen? (1, 2 of 3) "))

            bord[inputX-1][inputY-1] = "X"

        else:

            time.sleep(0.5)
            print("De computer is aan zet...")
            time.sleep(1)
            computerZet()

        if controleer_diagonaal() == 'pc' or controleer_horizontaal() == 'pc' or controleer_verticaal() == 'pc':

            genereer_nieuw_bord()
            print("De computer heeft gewonnen :/")
            spelBezig = False

        elif controleer_diagonaal() == 'player' or controleer_horizontaal() == 'player' or controleer_verticaal() == 'player':

            genereer_nieuw_bord()
            print("Proficiat, u heeft gewonnen van de computer!")
            spelBezig = False

        elif bord_vol():

            genereer_nieuw_bord()
            print("Gelijkstand...")

        else:

            # Toggle gebruikerAanzet
            gebruikerAanzet = not gebruikerAanzet

def genereer_nieuw_bord():

    # We loopen over de rijen (niet inclusief voor de eindwaarde!)
    for rij in range(BORD_GROOTTE):
        
        lijn = "|"

        # We loopen over de kolommen (ook niet inclusief voor de eindwaarde)
        for kolom in range(BORD_GROOTTE):

            lijn += " %1s |" % (bord[rij][kolom])
        
        # De eerste rij moet een extra lijntje hebben erboven
        if rij == 0: print("----"*BORD_GROOTTE)
        print(lijn)
        print("----"*BORD_GROOTTE)

def controleer_horizontaal():

    for rij in range(0,BORD_GROOTTE):

        n = 1

        for kolom in range(1,BORD_GROOTTE):

            if bord[rij][kolom] == bord[rij][kolom-1] != "":

                n += 1

        if n == BORD_GROOTTE:

            # Computer wint
            if bord[rij][0] == "O":

                return "pc"
            
            # Player wint
            elif bord[rij][0] == "X":

                return "player"
            
    return None

def controleer_verticaal():

    for kolom in range(0,BORD_GROOTTE):

        n = 1

        for rij in range(1,BORD_GROOTTE):

            if bord[rij][kolom] == bord[rij-1][kolom] != "":

                n += 1

        if n == BORD_GROOTTE:

            # Computer wint
            if bord[0][kolom] == "O":

                return "pc"
            
            # Player wint
            elif bord[0][kolom] == "X":

                return "player"
            
    return None

def controleer_diagonaal():

    # diagonaal van links boven naar rechts onder

    n = 1

    for i in range(1,BORD_GROOTTE):

        if bord[i][i] == bord[i-1][i-1] != 0:

            n += 1

    if n == BORD_GROOTTE:

        # Computer wint
        if bord[0][0] == "O":

            return "pc"
        
        # Player wint
        elif bord[0][0] == "X":

            return "player"
        
    else:

        k = 1

        # diagonaal van rechts boven naar links onder

        for i in range(1, BORD_GROOTTE):

            if bord[-i][-i] == bord[-i-1][-i-1] != 0:

                k += 1

        if k == BORD_GROOTTE:

            # Computer wint
            if bord[-1][-1] == "O":

                return "pc"
            
            # Player wint
            elif bord[-1][-1] == "X":

                return "player"

def zet_geldig(x,y):

    if (1 <= x <= BORD_GROOTTE) and (1 <= y <= BORD_GROOTTE) and bord[x-1][y-1] == "":

        return True
    
    else:

        return False
    
def computerZet():

    klaar = False

    while not klaar:

        randomRij = random.randint(0,BORD_GROOTTE-1)
        randomKolom = random.randint(0,BORD_GROOTTE-1)

        if bord[randomRij][randomKolom] == "":

            bord[randomRij][randomKolom] = "O"
            klaar = True

def bord_vol():

    for rij in bord:

        for cel in rij:

            if cel == "":

                return False
            
        return True

main()
