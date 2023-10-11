import math
# Opmerking: je kan in PyCharm makkelijk de lijncomments verwijderen via
# het menu Code/Comment with line comment...
#

# print('dit is een opdracht')
# print('daarna volgt de opdracht op de volgende lijn')
# print('enzovoort')
#
# a = int(input("Geef een geheel getal in: "))
# if a < 0:
#     print(a*-1)
# else:
#     print(a)
#
# teller = 0
# while teller < 10:
#     print(str(teller) + ". herhaling")
#     teller += 1
#
# print('De teller heeft nu waarde',teller)


#
# a = input("Woord :")
# b = input("Letter:")
# p = 0
# while p < len(a) and a[p] != b:
#     p += 1
# print("Eerste positie waar " + b + " zou kunnen voorkomen is " + str(p))

#
# antwoord = input("Antwoord: ")
# while antwoord != "42":
#     antwoord = input(antwoord + " is niet juist, antwoord: ")
# print("Juist!")
#
# a = int(input("Een positief geheel getal:  "))
# b = int(input("Nog zo een positief getal:  "))
# while a != b:
#     if a < b:
#         b -= a
#     else:
#         a -= b
# print("Het antwoord is:",a)

# ##
# # Bereken de som en het gemiddelde van een aantal getallen
# #
# aantal = int(input("Aantal getallen: "))
# aantalReedsIngegeven = 0
# som = 0
# while aantalReedsIngegeven < aantal:
#     volgende = int(input("Getal " + str(aantalReedsIngegeven + 1) + " : "))
#     som += volgende
#     aantalReedsIngegeven += 1
# print("Som :",som,", gemiddelde :",som/aantal)

##
# Bereken de som en het gemiddelde van een reeks positieve getallen
#
# aantal = 0
# som = 0
# getal = int(input("Geef een positief getal: "))
# while getal >= 0:
#     som += getal
#     aantal += 1
#     getal = int(input("Geef een positief getal, -1 om te stoppen: "))
# print("Som :",som,", gemiddelde :",som/aantal)
#


##
# Bereken de som en het gemiddelde van een reeks positieve getallen
# Lees niet vooraf
# #
# aantal = 0
# som = 0
# klaar = False
# while not klaar:
#     getal = int(input("Geef een positief getal, -1 om te stoppen: "))
#     if getal >= 0:
#         som += getal
#         aantal += 1
#     else:
#         klaar = True
# print("Som :",som,", gemiddelde :",som/aantal)



# ##
# # Bereken het minimum en het maximum van een aantal getallen
# #
# aantal = int(input("Aantal getallen: "))
# ingegeven = 0
# minimum = math.inf
# maximum = -math.inf
# while ingegeven < aantal:
#     volgende = int(input("Getal " + str(ingegeven + 1) + " : "))
#     if volgende < minimum:
#         minimum = volgende
#     if volgende > maximum:
#         maximum = volgende
#     ingegeven += 1
# print(minimum,maximum)

# ##
# # Bereken het gemiddelde van
# # de eerste 10 getallen van
# # Fibonacci
# fib1 = 1
# fib2 = 1
# print(1, ":", fib1)
# print(2, ":", fib2)
# som = fib1 + fib2
# for i in range(3,11):
#     fib = fib1 + fib2
#     print(i,":",fib)
#     som += fib
#     fib1 = fib2
#     fib2 = fib
# print(som/10)

##
# Tel de klinkers in een zin
#
# zin = input("Geef een zin: ")
# aantal = 0
# for letter in zin:
#     if letter in "aeiouy":
#         aantal += 1
# print("Aantal klinkers:",aantal)

#
# zin = input("Geef een zin: ")
# aantal = 0
# for letter in zin:
#     if letter == ".":
#         break
#     if letter in "aeiouy":
#         aantal += 1
# print("Aantal klinkers:",aantal)


# zin = input("Geef een zin:")
# aantal = 0
# positie = 0
# while positie < len(zin) and zin[positie] != ".":
#     if zin[positie] in "aeiouy":
#         aantal += 1
#     positie += 1
# print("Aantal klinkers:",aantal)

#
# ##
# # Voor de getallen van 1 tot en met 9
# # geef de 2de, 3de, 4de macht
# for n in range(1,10):
#     lijn = str(n)
#     for m in range(2,5):
#         lijn += "  " + str(n**m)
#     print(lijn)
#


# ##
# # Voor de getallen van 1 tot en met 9
# # geef de 2de, 3de, 4de macht
# for n in range(1,10):
#     lijn = "%5d" %(n)       # links uitlijnen: gebruik minteken: "%-5d"
#     for m in range(2,5):
#         lijn += "%10d" %(n**m)
#     print(lijn)


# lijst = [] # een lege lijst
# print(lijst)
# waarde = input("Volgende: ")
# while waarde != "":
#     lijst.append(waarde) # kan niet met een string
#     waarde = input("Volgende: ")
# print(lijst)
# if 'muis' in lijst:
#     print('got you')
#     lijst.remove('muis')
# print(lijst)


# lijst = []
# waarde = input("Volgende: ")
# while waarde != "":
#     lijst.append(waarde)
#     waarde = input("Volgende: ")
# for pos in range(len(lijst)):
#
#     if lijst[pos] == 'muis':
#         lijst[pos] = 'gevangen!'
# print(lijst)

# lijst = [1,2,3,4,5,6,7]
# for pos in range(len(lijst)):
#     print("%5d : %5d" %(pos,lijst[pos]))
# lijst[7] = 1000
# print(lijst)

# lijst = ['appel', 'citroen', 'muis', 'peer']
# andereLijst = lijst
# derdeLijst = list(lijst)
# print(lijst, andereLijst, derdeLijst)
# lijst[2] = 'gevangen'
# print(lijst, andereLijst, derdeLijst)
#


# s = 'Dit is een string'
# print(s[3])
# s[3] = 's'
# print(s)

# lijst = []
# volgende = input("? ")
# while volgende != "":
#     lijst.append(volgende)
#     volgende = input("? ")
# print('Onderzoek',lijst)
# for r in range(len(lijst)):
#     if lijst[r] != lijst[-(r+1)]:
#         print(lijst,"is geen palindroom")
#         break
# if r == len(lijst) - 1:
#     print(lijst,"is een palindroom")


lijst = []
volgende = input("? ")
while volgende != "":
    lijst.append(volgende)
    volgende = input("? ")
print('Onderzoek',lijst)
isPalindroom = True
for r in range(len(lijst)//2):
    if lijst[r] != lijst[-(r+1)]:
        isPalindroom = False
        break
if isPalindroom:
    print(lijst,"is een palindroom")
else:
    print(lijst, "is geen palindroom")

