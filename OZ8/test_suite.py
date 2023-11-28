def timeIt(statement, args):
    import time
    startTime = time.process_time()
    statement(*args)
    endTime = time.process_time()
    return endTime - startTime

def collect(statement, setup, aRange):
    result = []
    for count in aRange:
        print("Functie:", statement.__name__, "Inputgrootte:", int(count))
        
        m = 1
        t = [timeIt(statement, setup(int(count))) for _ in range(m)]
        result.append(sum(t) / len(t))


    return result

def show(title, axis, axisName, data, names):
    import matplotlib.pyplot as plt
    plt.close()
    plt.xlabel(axisName)
    plt.title(title)
    plt.plot(base=2)
    for p in range(len(data)):
        plt.plot(axis, data[p], label = names[p])
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

import numpy
#numpy.logspace(1,10,num=10, base=2)
def test(statements, setup, aRange=numpy.logspace(10,25,num=25, base=2)):
    collected = []
    stringRep = []
    for idx, statement in enumerate(statements):
        if isinstance(setup, list):
            collected.append(collect(statement, setup[idx], aRange))
        else:
            collected.append(collect(statement, setup, aRange))
        stringRep.append(statement.__name__ )
    show("Resultaat", aRange, "Aantal Elementen", collected, stringRep)