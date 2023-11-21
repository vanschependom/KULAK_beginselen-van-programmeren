
def voegLijnnummersToe(invoerFileLocatie, uitvoerFileLocatie):
    '''
        Deze functie voegt lijnnumeers toe aan een bestand met een gegeven naam en schrijft deze naar een ander bestand met gegeven naam.

    Parameters
    ----------
    invoerFileLocatie : string
        De naam van het invoerbestand waar de lijnnummers aan moeten worden toegevoegd.

    uitvoerFileLocatie : string
        De naam het weg te schrijven bestand

    '''

    # open de files
    fileInvoer = open(invoerFileLocatie)
    fileUitvoer = open(uitvoerFileLocatie,"w")

    # Voor elke lijnnummer en lijn in het inputbestand:
    for index, line in enumerate(fileInvoer):
        # schrijf de lijn weg met nummer ervoor
        fileUitvoer.write("/* " + str(index + 1) + " */ " + line)

    # sluit de files
    fileInvoer.close()
    fileUitvoer.close()


# main
def main():
    fIn = input("Geef een inputbestand in: ")
    fOut = input("Geef een outputbestand in: ")

    voegLijnnummersToe(fIn, fOut)
    # voegLijnnummersToe("mary.txt","newMary.txt")


# start de main
main()