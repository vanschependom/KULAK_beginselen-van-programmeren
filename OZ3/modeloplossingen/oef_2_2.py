
# Initialiseer 3 sets
set1 = {1, 2, 3}
set2 = set([2, 4, 5])
set3 = set()
set3.add(2)
set3.add(4)
set3.add(5)
set3.add(6)

# VRAAG 1:
# een nieuwe set met alle waarden die in set1 of set2 voorkomen,
# maar niet in beide

# let op de haakjes
vraag1 = (set1 | set2) - (set1 & set2)

# VRAAG 2:
# een nieuwe set met alle waarden die in precies 1 van de drie sets
# voorkomen

vraag2 = set1.intersection(set2).intersection(set3)
print(vraag2)

# VRAAG 3:
# een nieuwe set met alle waarden die in exact twee sets voorkomen
vraag3 = set1.intersection(set2)
vraag3 = vraag3.union(set1.intersection(set3))
vraag3 = vraag3.union(set2.intersection(set3))
# het verschil met de set van vraag2,
# bevat elementen die in alle drie de sets zitten.
vraag3 = vraag3.difference(vraag2)
