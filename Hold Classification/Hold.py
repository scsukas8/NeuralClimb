import HoldCategory

class Hold:
    '''
    This python class represents the hold on the wall

    Attributes:
        Size: the area that represents the circled area of the hold
        Color: (R,G,B)
        Positivity: a double from 0 to 1 that represents how easy 
                    it is to maintain contact with a hold
        Position: (x, y)
    '''

    def __init__(self, size, position, color = None, positivity = .5):
        self.size = size
        self.position = position
        self.color = color
        self.positivity = positivity

    def getPositivity(self):
        '''
        Gets the positivity of the hold
        '''
        return self.positivity

    def setPositivity(positivity):
        '''
        Gets the positivity of the hold
        '''
        self.positivity = positivity