import random
import copy


def genereerRij(lengte):

    rij = [(x, random.uniform(2, 7)) for x in range(lengte)]

    return rij


def mogelijkeRijen(ferry, auto):

    rijen = list()

    for rij in range(len(ferry)):

        if ferry[rij][0] >= auto[1]:

            rijen.append(rij)

    return rijen


def alleFerries(autos, ferry):

    if len(autos) == 0 or len(mogelijkeRijen(ferry, autos[0])) == 0:

        return [ferry]

    mogelijk = mogelijkeRijen(ferry, autos[0])

    mogelijkeFerries = []

    for indx in mogelijk:

        kopie = copy.deepcopy(ferry)
        kopie[indx].append(autos[0])
        kopie[indx][0] -= autos[0][1]

        minderAutos = list(autos)
        minderAutos.pop(0)

        mogelijkeFerries.extend(alleFerries(minderAutos, kopie))

    return mogelijkeFerries


def main():

    ferry = [
        [12],
        [20],
    ]

    autoRij = genereerRij(4)
    ferries = alleFerries(autoRij, ferry)

    for ferry in ferries:

        print("------------")

        for rij in ferry:

            print(rij)


main()
