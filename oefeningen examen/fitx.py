def irs(a1, a2):
    r = []
    i = 0
    while i < len(a1):
        j = len(a2)
        while j > 0:
            if a1[i] == a2[j-1]:
                if a2[j-1] not in r:
                    r.append(a1[i])
            j -= 1
        i += 1
    return r


print(irs("sneeuw", "skien"))
print(irs([1, 2, 5, 10, 20, 40], [20, 10, 5, 1, 0]))
print(irs(range(50), range(0, 20, 2)))
