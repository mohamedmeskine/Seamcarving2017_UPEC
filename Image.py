'''
Created on 2 janv. 2018

@author: M_MESKINE
'''
from Pixel import Pixel
from matplotlib.cbook import Null
from Couleur import Couleur
class Image(object):
    """
     Object image
     Hauteur : l'hauteur de l'image, type : int 
     Largeur  : la largeur de l'image, type : int
     premier : premier pixel de l'image (top left), type : Pixel
    """
    def __init__(self, tableau):
        (self.hauteur, self.largeur)=tableau.size
        self.premier = Null
        
        PI = Pixel (Couleur(255,255,255), Null , Null , Null, Null)
        PI.G = Pixel (Couleur(255,255,255), Null , PI , Null, Null)
        
        for i in range(0,self.hauteur,1):
#1-----------pixels de la 1er colonne de chaque ligne
            (r,g,b) = tableau.getpixel((i,0))
            PJ = Pixel(Couleur(r, g, b), Null , Null , PI, Null) 

            PJ.G = Pixel (Couleur(255,255,255), Null , PJ , PJ.H.G, Null) #Bordure noir pour la 1er colonne
    #2-----------bordure noir pour le pix de la derniere ligne, 1er colonne
            if (i+1) == self.hauteur :
                PJ.B = Pixel (Couleur(255,255,255), Null , Null , Null, Null)
                PJ.B.G = Pixel (Couleur(255,255,255), Null , Null , Null, Null)
    #2------------------------------------------------------
            PI.B = PJ
            if self.premier == Null:
                self.premier = PJ
#1-----------------------------------------------------------
            for j in range(1,self.largeur,1):
                (r,g,b) = tableau.getpixel((i,j))
                p= Pixel(Couleur(r, g, b) , Null , Null , Null, Null)
                if (PJ.H.D) == Null:    # Bordure haute de la 1er ligne
                    p.H = Pixel (Couleur(255,255,255), PJ.H , Null , Null, p)
                else :
                    PJ.H.D.B = p
                    p.H = PJ.H.D
                p.G = PJ
                PJ.D = p
#3---------------Bordure noir pour le reste des pix de la derniere ligne
                if (i+1) == self.hauteur :
                    p.B = Pixel (Couleur(255,255,255), PJ.B , Null , p, Null)
                    PJ.B.D = p.B
#3-----------------------------------------------------
                PJ = p
            PJ.D = Pixel (Couleur(255,255,255), PJ , Null , Null, Null) #Bordure noir pour la derniere colonne (2eme boucle terminee)
            PJ.D.H = Pixel (Couleur(255,255,255), PJ.H , Null , Null, Null)
            PJ.D.B = Pixel (Couleur(255,255,255), Null , Null , PJ.D, Null)
            PI = PI.B
            
#4-------pour l iterable    
        self.__idx = 0
        self.__I = self.premier 
        self.__J = self.premier 
#4--------------------------
    def __iter__(self):
            return self
    
    def next(self):
            if self.__idx > self.largeur -1:
                self.__I = self.__I.B
                self.__J = self.__I 
                self.__idx = 0
            if self.__I.B == Null:
                self.__idx = 0
                self.__I = self.premier 
                self.__J = self.premier
                raise StopIteration
            self.__idx += 1
            p = self.__J
            self.__J = self.__J.D
            return p
        
    def min3(self, pix1, pix2, pix3):
#         pixel non au bord
        if pix1.energie <= pix2.energie :
            return self.min(pix1, pix3)
        return self.min(pix2, pix3)
    
    def min(self,pix1 , pix2):
        if pix1.energie <= pix2.energie:
            return pix1
        return pix2
    
    def min_energie(self):
        energieChemin={}
        pix = self.premier
        for j in range(0,self.largeur,1):
            p = pix 
            cheminPixel=[p]
            s = p.energie
            while p.B <>Null :
                if p.B.G.G == Null:
                    p = self.min(p.B, p.B.D)
                elif p.B.D.D == Null:
                    p = self.min(p.B, p.B.G)
                else :
                    p = self.min3(p.B, p.B.G, p.B.D)
                s += p.energie
                cheminPixel.append(p)
            energieChemin[s]=cheminPixel
            pix = pix.D
        return energieChemin
    
    def supprimer_chemin(self, chemin):
        for pix in chemin:
            self.supprimer_pix(pix)
        
    def remettre_chemin(self, chemin):
        for pix in chemin:
            self.remettre_pix(pix)
    
    def supprimer_pix(self, pixel):
        pixel.G.D = pixel.D
        pixel.D.G = pixel.G
        pixel.H.B = pixel.B
        pixel.B.H = pixel.H
    
    def remettre_pix(self, pixel):
        pixel.G.D = pixel
        pixel.D.G = pixel
        pixel.H.B = pixel
        pixel.B.H = pixel
                