from quiz import *

def main():

    vragen = []
    v1 = Vraag("Van welke cactussoort wordt tequila gemaakt?","Agave")
    vragen.append(v1)
    v2 = Meerkeuzevraag("Welke cocktail bestaat uit Vodka, limoensap en gemberbier?",
                        ["Mojito", "Moscow Mule", "Long Island Iced Tea", "Negroni"], 1)
    vragen.append(v2)
    v3 = NumeriekeVraag("Hoeveel ml gaat er in 1 oz?", 29.5735296875, 0.1)
    vragen.append(v3)

    for vraag in vragen:
        print(vraag.getVraagString())
        antwoord = input("Antwoord: ")
        if(vraag.checkAntwoord(antwoord)):
            print("Correct!")
        else:
            print("Jammer!")


main()

