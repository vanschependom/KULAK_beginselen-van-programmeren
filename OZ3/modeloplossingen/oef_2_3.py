# Multiset

set1 = {"appel": 3, "banaan": 4}
set2 = {"peer": 2, "banaan": 5}

# Unie:
set_unie = dict(set1)  # een kopie maken van set1
for key in set2:
    if key in set_unie:
        set_unie[key] += set2[key]
    else:
        set_unie[key] = set2[key]

print(set_unie)

# Verschil:
# maken van een kopie voor linker lid en rechter lid resp.
setll = dict(set1)
setrl = dict(set2)

set_verschil = dict()
for key in setll:
    if key in setrl:
        if setll[key] > setrl[key]:
            set_verschil[key] = setll[key] - setrl[key]
        else:
            pass
    else:
        set_verschil[key] = setll[key]

print(set_verschil)

# Doorsnede:

set_doorsnede = dict()
for key in set1:
    if key in set2:
        set_doorsnede[key] = min(set1[key], set2[key])

print(set_doorsnede)
