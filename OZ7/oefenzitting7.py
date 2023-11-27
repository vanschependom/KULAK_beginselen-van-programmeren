buurmatrix = [[0, 1, 2, 1, None, None, None],
              [1, 0, 1, None, 5, None, None],
              [2, 1, 0, None, 3, 1, None],
              [1, None, None, 0, None, 5, None],
              [None, 5, 3, 0, None, None, 1],
              [None, None, None, 5, None, 0, 2],
              [None, None, None, None, 1, 2, 0]]

# buurmatrix = [
#     [0, 1, 2, 0],
#     [1, 0, 1, 5],
#     [2, 1, 0, 3],
#     [0, 5, 3, 0]
# ]


def genereerWegen(start, eind, buurmatrix, huidigPad=[]):

    if start == eind:

        return [(0, huidigPad)]

    huidigPad.append(start)

    output = []

    for i, lengteTotBuur in enumerate(buurmatrix[start]):

        if lengteTotBuur != None and lengteTotBuur != 0 and i not in huidigPad:

            padenVanafBuur = genereerWegen(
                i, eind, buurmatrix, list(huidigPad))

            for volgendeAfstand, volgendPad in padenVanafBuur:

                output.append(
                    (volgendeAfstand + lengteTotBuur, volgendPad))

    return output


alleWegen = genereerWegen(0, 6, buurmatrix)

for weg in alleWegen:

    print(f"Lengte: {weg[0]}, pad: {weg[1]}")
