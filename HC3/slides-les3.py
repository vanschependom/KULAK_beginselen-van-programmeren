import math
# Opmerking: je kan in PyCharm makkelijk de lijncomments verwijderen via
# het menu Code/Comment with line comment...
lijst = [4,9,1,3,5,2]
#
# klaar = False
# lijst = []
# while not klaar:
#     invoer = input("Geef een getal, druk enter om te stoppen: ")
#     if invoer != "":
#         lijst.append(int(invoer))
#     else:
#         klaar = True
#
# print(lijst)
#
# # I: alle elementen in lijst met een index < goed
# #    staan op hun plaats in de gesorteerde lijst
# for goed in range(len(lijst)):
#     # zoek de index van het kleinste element in de lijst met
#     # een index >= goed
#     i_min = goed
#     for i in range(goed+1,len(lijst)):
#         if lijst[i] < lijst[i_min]:
#             i_min = i
#     # wissel het gevonden element met
#     # element op de huidige index goed
#     if goed != i_min:
#         h = lijst[goed]
#         lijst[goed] = lijst[i_min]
#         lijst[i_min] = h
# print(lijst)
#


# lijst = []
# for i in range(3):
#     lijst.append(int(input("Geef een getal in: ")))
# print(lijst)
#
# if lijst[0] <= lijst[1] <= lijst[2]:
#     print(lijst[0],lijst[1],lijst[2])
# elif lijst[0] <= lijst[2] <= lijst[1]:
#     print(lijst[0],lijst[2],lijst[1])
# elif lijst[1] <= lijst[0] <= lijst[2]:
#     print(lijst[1],lijst[0],lijst[2])
# elif lijst[1] <= lijst[2] <= lijst[0]:
#     print(lijst[1],lijst[2],lijst[0])
# elif lijst[2] <= lijst[0] <= lijst[1]:
#     print(lijst[2],lijst[0],lijst[1])
# else:
#     print(lijst[2],lijst[1],lijst[0])
#
# lijst = ['muis', 42, 3.14, math.pi, ["een", "twee"]]
#
# print(lijst[3])
#
# andereLijst = list(lijst) # kopie maken
# legeLijst = []
# nogEenLegeLijst = list()
#
# lijst.append("nog een string")
# lijst.remove(3.14)
# lijst[0] = 'gevangen!'
#
# print(lijst)
#
# nullen = [0]*5
# print(nullen)
# a = ["deel1","deel2"]
# b = ["deel3","deel4"]
# l = a+b
# print(a,b)
# print(l)
# a.extend(b)
# print(a)
#
# l.insert(2,'-')
# print(l)
#
# print(l.pop())
# print(l)
# print(l.pop(0))
# print(l)

# lijst = [10,2,6,8,0,4]
# print(lijst)
# print(len(lijst))
# print(min(lijst))
# print(max(lijst))
# print(sum(lijst))

# lijst = ['muis', 42, 3.14, math.pi, ["een", "twee"]]
# andereLijst = lijst
# naam = "Harry"
# andereNaam = naam
#
# andereLijst[0] = 'gevangen!'
# print(lijst,andereLijst)
# #andereNaam[4] = 'i'
# andereNaam = "Harri"
# print(naam,andereNaam)

#
# s1 = "Dit is geen muis"
# s2 = s1
# s1 += "."
# print(s1)
# print(s2)
#
# l1 = [2,3,6,20, 168, 7581]
# l2 = l1
# l1 += [7828354]
# print(l1)
# print(l2)

#
# lijst = [2,3,6,20,168,1729,7581,7828354]
# for dn in lijst:
#     print(dn)
#
# pos = 0
# while pos < len(lijst):
#     print(pos,lijst[pos])
#     pos += 1
#
# for pos in range(len(lijst)):
#     print(pos,lijst[pos])


# lijst = [2,3,6,20,168,1729,7581,7828354]
# print(lijst[1:4])
# print(lijst[0:4])
# print(lijst[:4])
# print(lijst[6:len(lijst)])
# print(lijst[6:])
# print(lijst[6:-3])

# lijst = [1,2,3,4,5,6,7,8,9]
# pl = lijst[2:5]
# print(lijst)
# print(pl)
# for p in range(len(pl)):
#     pl[p] *= 2
# print(lijst)
# print(pl)

# lijst = [2,3,6,20,168,1729,7581,7828354]
#
# print(lijst)
# lijst.insert(3,14)
# print(lijst)
#
# print(lijst.index(168))
# print(lijst.index(42))
#
#
# l1 = [2,3,6,20,168,1729,7581,7828354]
# l2 = [2,3,6,20,168,1729,7581,7828354]
# print(1,l1 == l2)
#
# l1 = [2,3,6,20,168,1729,7581,7828354]
# l2 = [2,3,6,20,168,7581,7828354]
# print(2,l1 == l2)
#
# l1 = [2,3,6,20,168,1729,7581,7828354]
# l2 = [2,3,6,14,168,1729,7581,7828354]
# print(3,l1 == l2)
#
# l1 = [2,3,6,20,168,1729,7581,7828354]
# l2 = [2,3,6,20,168,7581,7828354]
# print(4,l1[:5] == l2[:5])
# print(5,l1[6:] == l2[5:])
#
# l1 = [2,3,6,20,168,1729,7581,7828354]
# l2 = [2,3,6,20,168,1729,7581,7828354]
# print(6,l1 is l2)
#
# l1 = [2,3,6,20,168,1729,7581,7828354]
# l2 = l1
# print(7,l1 is l2)
#

# lijst = [6,3,9,2,5,1,0]
#
# print(lijst)
# print(sorted(lijst))
# print(lijst)
# lijst.sort()
# print(lijst)

# matrix = []
# matrix.append([1,0,0,0])
# matrix.append([0,1,0,0])
# matrix.append([0,0,1,0])
# matrix.append([0,0,0,1])
#
# print(matrix)
#
# for line in matrix:
#     print(line)
#
# for line in matrix:
#     for element in line:
#         print(element, end='\t')
#     print()
#
#
#
# t1 = (1,"Jan")
# t2 = (2,"Piet")
# t3 = (3,"Joris")
# t4 = (5,"Korneel")
#
# oorsprong = (0.0,0.0,0.0)
# xxx = uiterstehoek = (1.0,1.0,1.0)
# xoo = (1.0,0.0,0.0)
# oxx = (0.0,1.0,1.0)
#
# # notatie zonder haakjes
# midden = 0.5,0.5,0.5
#
# print(midden[1])
# print(t1,oorsprong,xxx,xoo,midden)

# a = [3]
# b = [4]
# tupel = (a,b)
# print(tupel)
# a+=[7]
# print(tupel)
#
# a = "immutable"
# b = "string"
# tupel = (a,b)
# print(tupel)
# a+= " tralala"
# print(tupel)


#
# studenten = {"Jan","Piet","Joris","Korneel"}
# print(studenten)
# studenten.add("Carolien")
# print(studenten)
# studenten.remove("Korneel")
# print(studenten)
# studenten.add("Korneel")
# print(studenten)
# studenten.add("Korneel")
# print(studenten)
#

# praesidium = {"Carolien","Jan"}
# print(praesidium)
# studenten = {"Joris","Korneel","Jan","Piet"}
# print(studenten)
# unie = studenten | praesidium
# print(unie)
# doorsnede = studenten & praesidium
# print(doorsnede)
# verschil = studenten - praesidium
# print(verschil)
# verschil = praesidium - studenten
# print(verschil)
#
#
# studenten = {"Jan","Piet","Joris","Korneel"}
# docenten = set()
# print(docenten,len(docenten))
# print("Carolien is een student:","Carolien" in studenten)
# print("Carolien is een docent :","Carolien" in docenten)
# for student in studenten:
#     print(student.upper())
# print()
# for student in sorted(studenten):
#     print(student.upper())
# print(sorted(studenten))


# studenten = {"Jan","Piet","Joris","Korneel"}
# docenten = set()
# studenten.discard("Korneel")
# docenten.discard("Korneel")
# print(studenten)
# print(docenten)
#
# studenten = {"Jan","Piet","Joris","Korneel"}
# studenten.clear()
# print(studenten)
# # dit werkt ook voor lijsten!
# studentenLijst = ["Jan","Piet","Joris","Korneel"]
# studentenLijst.clear()
# print(studentenLijst)
#

# set1 = {'a','b','c'}
# set2 = {'c', 'd', 'e'}
#
# print(set1,set2)
# print(set1 | set2)
# print(set1,set2)
# print(set1.union(set2))
# print(set1,set2)
#
#
#




# telefoonboek = {} # een lege dictionary
# telefoonboek["jens"] = "7657"
# telefoonboek["jarne"] = "7657"
# telefoonboek["michiel"] = "2402"
#
# print(telefoonboek)
# telefoonboek["michiel"] = "1010"
# print(telefoonboek)

telefoonboek = {"jens":7657, "jarne":7657, "michiel":2402}
legeD = dict()
print(legeD)
kopie = dict(telefoonboek)
print(kopie)

print(kopie['jarne'])
print(kopie.get("michiel"))
print(kopie.get("patrick",-1))
print(kopie.pop('jens'))
print(kopie)
kopie.pop()
print(kopie)

# telefoonboek = {"jens":7657, "jarne":7657, "michiel":2402}
# print(telefoonboek.keys())
# print(telefoonboek.values())
# print(telefoonboek.items())
#
# print(sorted(telefoonboek))
# print(sorted(telefoonboek.items()))


#
#
# tekst = input("Enter text: ")
# telling = {} # we gaan het voorkomen van tekens tellen
# for c in tekst:
#     if c not in telling:
#         telling[c] = 1
#     else:
#         telling[c] += 1
# print(telling)
# print(sorted(telling))
# for c in sorted(telling):
#     if 'a' <= c.lower() <= 'z':
#         print(c,telling[c])

#
# tekst = input("Enter text: ")
# telling = {}
# for c in tekst:
#     if c not in telling:
#         telling[c] = 1
#     else:
#         telling[c] += 1
# teken = input("Karakter: ")
# while teken != "":
#     print(teken+": "+str(telling.get(teken,0)))
#     teken = input('Karakter, stop met "": ')
#
#
#
# a = {'a','b','c'}
# b = {'a','d','e'}
#
# a.union(b)
# print(a)