# In PyCharm kan je snel codeblokken
# in commentaar zetten of uit commentaar halen:
# Selecteer de code en kies in het menu:
# Code/Comment with Line Comment
#

import math

# Dit is mijn eerste Python programma
# Het is de Python versie van het eerste programma in
# "The C Programming Language", Kernighan and Ritchie, 1971

# print("Hello World!")

# print(3.2**2)
# print(32**2)
# print(10/0)
# print(math.e)

#
# print(math.pi / 100000000)
#
#
# aantal = 10
# waarde = 1234
# gemiddelde = waarde / aantal

#print(aantal, waarde, gemiddelde)

#naam = "Johan"
#print(naam / aantal)

import math

# print(22 + 7, 22 - 7, 22 * 7, 22 / 7)
# print(7 + 22, 7 - 22, 7 * 22, 7 / 22)
# print()
# print( 22 //  7,  22 %  7)
# print(-22 //  7, -22 %  7)
# print( 22 // -7,  22 % -7)
# print(-22 // -7, -22 % -7)
# print()
# print(  7 //  22,  7 %  22)
# print( -7 //  22, -7 %  22)
# print(  7 // -22,  7 % -22)
# print( -7 // -22, -7 % -22)


#print(3**2)
#print(32**2)
#print(3.2**2)
#print(3.2**0.5)

#
# a = b = c = d = e = f = g = 103
#
# print(a,b,c,d,e,f,g)
# a+= 10
# b-=10
# c*=10
# d/=10
# e%=10
# f//=10
# g**=10
# print(a,b,c,d,e,f,g)


#a = 42
#print("Het antwoord is", a)
#
a = -10
b = abs(a)
# print('|',a,'|=',b)
# print('|'+str(a)+'| = '+str(b))
#
# eenString = "42"
# eenGetal = int(eenString)
# #print(eenString / 2)
# print(eenGetal / 2)
#
# print("Strings met escape character: \' \" \\")
# print("De lengte van een string bekomen we met de functie len(.).")
# print("len('Dit is een string.') = " + str(len('Dit is een string.')))
# print("De lengte van de lege string is",len(""))


#a = "Hello"
#b = "World"
#print(a + " " + b + "!")
#print(a + "."*3 + b + "!")
#c = 42
#d = "42"
#print(d + "."*int(d) + "puntjes")

#print(ord('a'))
#print(ord('A'))
#print(chr(98))
#print(chr(66))
#
# tekst = "I am from Barcelona."
# print(tekst[0])
# print(tekst[len(tekst)-1])
# print(tekst[-1])
# print(tekst.upper())
# print(tekst.lower())
# print(tekst) # De string is niet gewijzigd!
# print(tekst.replace(" ","_"))
# print(tekst.replace(" ","\n")) # end-of-line character
#
# a = int(input("Geef een geheel getal in:"))
# print("De absolute waarde ervan is: "+ str(abs(a)))
#
# print("PI is ongeveer %.2f." %(22/7))
#
# leeftijd = int(input("Geef een leeftijd: "))
# naam = input("Geef een naam: ")
# if leeftijd >= 21:
#    print(naam,"is al lang meerderjarig.")
# print("KLAAR")

#
# leeftijd = int(input("Geef een leeftijd: "))
# if leeftijd <= 10:
#     print("Kind")
# elif leeftijd < 20:
#     print("Tiener")
# elif leeftijd < 30:
#     print("Twintiger")
# elif leeftijd == 100:
#     print("Eeuweling")
# else:
#     print("Tram",str(leeftijd)[-2])
#
#
# leeftijd = int(input("Geef een leeftijd: "))
# if leeftijd <= 10:
#     print("Kind")
# else:
#     if leeftijd < 20:
#         print("Tiener")
#     else:
#         if leeftijd < 30:
#             print("Twintiger")
#         else:
#             if leeftijd == 100:
#                 print("Eeuweling")
#             else:
#                 print("Tram",str(leeftijd)[:-1])

# print("Quiz!")
# antwoord = input("Welk wezen heerst over het universum? ")
# if "muis" in antwoord.lower():
#     print("Proficiat!")
# else:
#     print("Niet juist!")
#
#
# print("Quiz!")
# antwoord = float(input("Hoeveel is 3.2 ** 2 ? "))
# epsilon = 10E-6
# if 3.2**2 - epsilon <= antwoord <= 3.2**2 + epsilon:
#     print("Proficiat!")
# else:
#     print("Niet juist!")
#

# r = float(input("Aardbeving op de schaal van Richter: "))
# if r >= 8.0:
#     print("Er staat niks meer recht.")
# if r >= 7.0:
#     print("Er is veel verwoest.")
# if r >= 6.0:
#     print("Er is heel wat schade.")
# if r > 4.5:
#     print("Er is beperkte schade aan zwakke woningen.")

r = float(input("Aardbeving op de schaal van Richter: "))
ramp = r >= 8.0
ernstig = r >= 7.0 and r < 8.0
aanzienlijk = r >= 4.5 and r < 7.0
zwak = r < 4.5
if ramp == True or ernstig == True:
    print("Activeer het rampenfonds!")













