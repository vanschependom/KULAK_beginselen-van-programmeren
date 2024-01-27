buurmatrix = [[0, 1, 2, 1, None, None, None],
              [1, 0, 1, None, 5, None, None],
              [2, 1, 0, None, 3, 1, None],
              [1, None, None, 0, None, 5, None],
              [None, 5, 3, 0, None, None, 1],
              [None, None, None, 5, None, 0, 2],
              [None, None, None, None, 1, 2, 0]]


def allePaden(van, naar, buurmatrix, huidigPad=[]):

    huidigPad.append(van)

    if van == naar:

        return [(huidigPad, 0)]

    output = []

    for buur, afstandTotBuur in enumerate(buurmatrix[van]):

        if afstandTotBuur != None and afstandTotBuur != 0 and buur not in huidigPad:

            korterePaden = allePaden(buur, naar, buurmatrix, list(huidigPad))

            for pad, lengte in korterePaden:

                output.append((pad, lengte+1))

    return output


print(allePaden(1, 5, buurmatrix))
