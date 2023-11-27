
class Counter:
    '''
    Klasse die tellers voor het bijhouden van
    bezoekersaantallen voorstelt.
    '''

    def __init__(self):
        '''
        Maakt een nieuwe teller aan met waarde 0.
        '''
        self._value = 0

    def reset(self):
        '''
        Zet de waarde van de teller op 0.
        '''
        self._value = 0

    def click(self):
        '''
        Verhoogt de waarde van de teller met 1.
        '''
        self._value += 1

    def getValue(self):
        '''
        Geeft de waarde van de teller terug.
        Returns
        -------
        int
            de waarde van de teller
        '''
        return self._value

