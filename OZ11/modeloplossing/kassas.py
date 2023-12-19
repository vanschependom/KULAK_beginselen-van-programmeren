import random
import matplotlib.pyplot as plt
import numpy as np

def genereerKlant(aankomstTijd, maxAantalProducten=20):
    """
    Genereer klant met ee
    Parameters
    ----------
    aankomstTijd
    maxAantalProducten

    Returns
    -------

    """
    return [aankomstTijd, random.randint(1, maxAantalProducten)]

def simulatie(kassasRate, aantalProducten, simulatieTijd, klantRate, mode):
    """
    
    Parameters
    ----------
    kassasRate
    aantalProducten
    simulatieTijd
    klantRate
    mode

    Returns
    -------

    """
    wachtendeKlanten = []
    wachttijd = []
    kassas = []
    for kr in range(len(kassasRate)):
        kassas.append([])
    
    for t in range(simulatieTijd):
        if t % klantRate == 0:
            klant = genereerKlant(t, aantalProducten)
            
            if mode == 'willekeurig':
                klantToKassa = random.randint(0,len(kassasRate)-1)
                kassas[klantToKassa].append(klant)

            elif mode == 'advies':
                achterstandWachttijd = []
                for kassaNr in range(len(kassas)):
                    voorwerpenAantal = 0
                    for klant in kassas[kassaNr]:
                        voorwerpenAantal += klant[1]
                    achterstandWachttijd.append(voorwerpenAantal/kassasRate[kassaNr])
                minAchterstand = min(achterstandWachttijd)
                klantToKassa = achterstandWachttijd.index(minAchterstand)
                kassas[klantToKassa].append(klant)

            else:
                aanKassa = False
                for kassa in kassas:
                    if len(kassa) == 0:
                        kassa.append(klant)
                        aanKassa=True
                        break
                if not aanKassa:
                    wachtendeKlanten.append(klant)
            
            
        for kassaNr in range(len(kassas)):
            kassaDeltaT = 1
            
            if mode in ['willekeurig','advies']:
                while kassaDeltaT > 0 and len(kassas[kassaNr])>0:
                    # Check als kassa i de eerste klant kan bedienen in tijdseenheid t -> t+1
                    if kassas[kassaNr][0][1] / kassasRate[kassaNr] <= kassaDeltaT:
                        wachttijdKlant = t - kassas[kassaNr][0][0] + kassas[kassaNr][0][1] / kassasRate[kassaNr]
                        wachttijd.append(wachttijdKlant)
                        kassaDeltaT -= kassas[kassaNr][0][1] / kassasRate[kassaNr]
                        del kassas[kassaNr][0]
                    else:
                        kassas[kassaNr][0][1] -= kassasRate[kassaNr] * kassaDeltaT
                        break
            else:
                while kassaDeltaT > 0 and (len(kassas[kassaNr])>0 or len(wachtendeKlanten)>0):
                    # Check als kassa i de eerste klant kan bedienen in tijdseenheid t -> t+1
                    if len(kassas[kassaNr]) == 0 and len(wachtendeKlanten)>0:
                        kassas[kassaNr].append(wachtendeKlanten[0])
                        del wachtendeKlanten[0]
                    if kassas[kassaNr][0][1] / kassasRate[kassaNr] <= kassaDeltaT:
                        wachttijdKlant = t - kassas[kassaNr][0][0] + kassas[kassaNr][0][1] / kassasRate[kassaNr]
                        wachttijd.append(wachttijdKlant)
                        kassaDeltaT -= kassas[kassaNr][0][1] / kassasRate[kassaNr]
                        del kassas[kassaNr][0]
                    else:
                        kassas[kassaNr][0][1] -= kassasRate[kassaNr] * kassaDeltaT
                        break

    return wachttijd

def main():
    
    kassasRate = [1,3,6,8]
    aantalProducten = 20
    simulatieTijd = 5000
    klantRate = 3
    
    wachttijdWillekeurig = simulatie(kassasRate, aantalProducten, simulatieTijd, klantRate, mode='willekeurig')
    wachttijdAdvies = simulatie(kassasRate, aantalProducten, simulatieTijd, klantRate, mode='advies')
    wachttijdEenRij = simulatie(kassasRate, aantalProducten, simulatieTijd, klantRate, mode='EenRij')
    
    print('RESULTATEN')
    print('----------')
    print('MEAN:')
    print('willekeurig: \t{0:.3f}s'.format(np.mean(wachttijdWillekeurig)))
    print('advies: \t\t{0:.3f}s'.format(np.mean(wachttijdAdvies)))
    print('een rij: \t\t{0:.3f}s'.format(np.mean(wachttijdEenRij)))

    print('\nMAX:')
    print('willekeurig: \t{0:.3f}s'.format(np.max(wachttijdWillekeurig)))
    print('advies: \t\t{0:.3f}s'.format(np.max(wachttijdAdvies)))
    print('een rij: \t\t{0:.3f}s'.format(np.max(wachttijdEenRij)))
    
    xlimmax = 30
    plt.figure()
    _, bins, _ = plt.hist(wachttijdWillekeurig, alpha=0.5, bins=xlimmax*2,range=[0,xlimmax], density=True)
    plt.hist(wachttijdAdvies, alpha=0.5, bins=bins, density=True)
    plt.hist(wachttijdEenRij, alpha=0.5, bins=bins, density=True)
    plt.grid()
    plt.legend(['willekeurig','advies','één rij'])
    plt.tight_layout()
    plt.show()

main()
        
