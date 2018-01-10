'''
Created on 2 janv. 2018

@author: mohail
'''
from PIL.Image import * 
from Image import Image
import time
from Couleur import *
from Pixel import *

img=open('loutres.jpg')
nl,nc = img.size
 

debut=time.time()
imgLtr = Image(img)
fin=time.time()
print (fin-debut)

debut=time.time()
for p in imgLtr : 
    p.calculeEnergie()
fin=time.time()
print (fin-debut)

debut=time.time()
dictio=imgLtr.min_energie()
fin=time.time()
print (fin-debut)

