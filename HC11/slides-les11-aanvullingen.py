from buurtfeesten import *
import random

def main():

    feest = Buurtfeest("Feestje")
    feest.voegComitelidToe(Comitelid("An Dijvie", "Hoogweg 12, 8560 Wevelgem"))
    feest.voegComitelidToe(Comitelid("Peter Selie", "Kortrijkstraat 402, 8510 Marke"))
    feest.voegComitelidToe(Comitelid("Cas Tanje", "Heirbaan 2298, 8520 Kuurne"))
    feest.voegComitelidToe(Comitelid("May O'Naise", "Mellestraat 1, 8501 Heule"))
    feest.voegComitelidToe(Comitelid("Peter Selie", "Kortrijkstraat 215, 8510 Marke"))

    for lid in sorted(feest.getComiteleden()):
        print(lid)

    try:
        feest.voegComitelidToe(Comitelid("Beau ter Ham",""))
    except TypeError as e:
        print("Verkeerd type!")
        print("( -> "+e.args[0]+")")
    except ValueError as e:
        print("Lege string!")
        print("( -> "+e.args[0]+")")

#main()


def demoFinally():

    def writeSomething():
        try:
            f = open("demofile.txt")
            try:
                f.write("Lorum Ipsum")
                return "done"
            except:
                print("Something went wrong when writing to the file")
                raise Exception("A serious problem occured!")
            finally:
                f.close()
        except:
            print("Something went wrong when opening the file")
            raise Exception("Could not open the file!")

    writeSomething()


def demoReflection():

    x = 5
    s = "Marga Riene"
    y = [1,2,3]

    print(type(x))
    print(type(s))
    print(type(y))

    print(isinstance(x,str))
    print(isinstance(x,int))
    print(isinstance(x,list))
    print(isinstance(s,str))
    print(isinstance(y,list))
    print(isinstance(y,(list,tuple,Buurtfeest)))


    print(dir(Comitelid))



def demoComprehension():

    random.seed()
    getallen = [random.randint(0,9) for x in range(100)]
    print(getallen)

    evenGetallen = [x for x in getallen if x % 2 == 0]
    print(len(evenGetallen))



demoComprehension()

expression = 1
iterable = []
condition = True


newlist = [expression for item in iterable if condition]

