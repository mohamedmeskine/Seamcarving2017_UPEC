# Seamcarving2017_UPEC
Le but de de ce projet, est de redimensionner une image intelligemment : c'est à dire lors du redimensionnement les informations importantes ne soient pas effacées, déformées ou trop altérées visuellement.
L'idée est de calculer puis supprimer les chemins d’énergie minimale jusqu’à ce que l’image aie atteint la taille souhaitée.
# Approche utilisée
La démarche adoptée pour ce travail consiste en premier lieu de représenter une image comme un objet ayant trois attributs :

 - hauteur et largeur : représentent respectivement les dimensions de l'image.
 - premier : objet de type Pixel, et qui représente le premier pixel de l'image (coin haut gauche).

le constructeur de cette classe consiste à partir d'un tableau de couleur qui représente l'image, de traduire chaque case du tableau a un objet Pixel.

Cette classe contient les 3 méthodes principales :

 - supprimer_chemin : qui supprime une liste de pixels passée en paramètre, cette méthode sera appelé pour réduire la largeur de l'image.
 - remettre_chemin : c'est l'inverse de la méthode précédente, elle sera appelé pour agrandir la largeur de l'image après avoir la réduire (taille max = taille initiale de l'image).
 - min_energie : qui retourne la liste des énergies de chaque seam, ordo  

 

 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNjY3NDM1NjBdfQ==
-->