'''
@author: M_MESKINE
'''
from Couleur import Couleur
from math import sqrt
class Pixel(object):
    """
    Object pixel
    G : pixel adjacent a gauche
    D : pixel adjacent a droite
    H : du pixel adjacent en haut
    B : du pixel adjacent en bas
    couleur : couleur du pixel actuel, type couleur (R,G,B)
    energie : l'energie du pixel 
    b : intensite du pixel
    """
    def __init__(self,couleur, G, D, H, B):
        self.G = G
        self.D = D
        self.H = H
        self.B = B
        if (not couleur) :
            self.couleur = Couleur(255,255,255)
        else :
            self.couleur= couleur
        self.energie = 0
        self.b  = (self.couleur.R + self.couleur.G + self.couleur.B)/3
        
    def g_x(self):
#         b(i-1,j-1)+2b(i-1,j)+b(i-1,j+1)-b(i+1,j-1)-2b(i+1,j)-b(i+1,j+1)
        if self.couleur.getRGB() == (255,255,255):
            return 255
        return self.G.H.b + 2*self.H.b + self.D.H.b 
        - self.B.G.b - 2*self.B.b - self.B.D.b
    
    def g_y(self):
#         b(i-1,j-1)+2b(i,j-1)+b(i+1,j-1)-b(i-1,j+1)-2b(i,j+1)-b(i+1,j+1)
        if self.couleur.getRGB() == (255,255,255):
            return 255
        return self.H.G.b + 2*self.G.b + self.B.G.b
        - self.D.H.b - 2*self.D.b - self.D.B.b
    
    #     energie du pixel courant 
    
    def calculeEnergie(self):
        self.energie = sqrt( pow(self.g_x(), 2)+pow(self.g_y(), 2) )
    
    def __str__(self):
        return "({},{},{})".format(self.couleur.R, self.couleur.G, self.couleur.B)
    