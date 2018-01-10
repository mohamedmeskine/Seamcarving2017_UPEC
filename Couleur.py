'''
@author: M_MESKINE
'''
class Couleur(object):
    """
    Object couleur
    R rouge
    G vert
    B bleu
    """
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
        
    def getRGB(self):
        return (self.R, self.G, self.B)
    
