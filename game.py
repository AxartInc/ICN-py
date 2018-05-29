from tkinter import *
from random import randint

who = 1
whe = 0

who = randint(0, 1)

if who == 0:
    whe = 1

def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY,PosX2,PosY2,who,whe,basex,basey
    touche = event.keysym
    print(touche)
      
    #JOUEUR 1 
    
    # déplacement vers le haut
    if touche == 'Up':
        PosY -= 20
    # déplacement vers le bas
    if touche == 'Down':
        PosY += 20
    # déplacement vers la droite
    if touche == 'Right':
        PosX += 20
    # déplacement vers la gauche
    if touche == 'Left':
        PosX -= 20
        
    #JOUEUR 2    
    
    # déplacement vers le haut
    if touche == 'z':
        PosY2 -= 20
    # déplacement vers le bas
    if touche == 's':
        PosY2 += 20
    # déplacement vers la droite
    if touche == 'd':
        PosX2 += 20
    # déplacement vers la gauche
    if touche == 'q':
        PosX2 -= 20
        
    
    # saut
    #if touche == 'space':
    #    if  PosY >= 280:
    #        PosY -= 20
    
    if PosX<0:
        PosX=0
        
    if PosY<0:
        PosY=0
        
    if PosX>480:
        PosX=480
        
    if PosY>320:
        PosY=320
        
    if PosX2<0:
        PosX2=0
        
    if PosY2<0:
        PosY2=0
        
    if PosX2>480:
        PosX2=480
        
    if PosY2>320:
        PosY2=320
        
    if PosY==PosY2:
        if PosX==PosX2:
            PosX = 460
            PosY = 300
            
            PosX2 = 20
            PosY2 = 20
            
            if who == 1:
                who = 0
                whe = 1
                basex = (20 * randint(1, 23)) 
                basey = (20 * randint(1, 15)) 
            elif whe == 1:
                who = 1
                whe = 0
                basex = (20 * randint(1, 23)) 
                basey = (20 * randint(1, 15)) 
                
    if PosX==basex:
        if PosY==basey:
            PosX = 460
            PosY = 300
            
            PosX2 = 20
            PosY2 = 20
            
            basex = (20 * randint(1, 23))
            basey = (20 * randint(1, 15))
            
            
    if PosX2==basex:
        if PosY2==basey:
            PosX = 460
            PosY = 300
            
            PosX2 = 20
            PosY2 = 20
            
            basex = (20 * randint(1, 23))
            basey = (20 * randint(1, 15))
    
         
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion,PosX -10, PosY -10, PosX +10, PosY +10)
    Canevas.coords(Pion2,PosX2 -10, PosY2 -10, PosX2 +10, PosY2 +10)
    
    Canevas.coords(Base1,basex-10, basey-10, basex+10, basey+10)
        
    
    if who==1:
        Canevas.itemconfig(Pion, outline ='red')
        Canevas.itemconfig(Pion2, outline ='white')
        
        Canevas.coords(Base1,basex -10, basey -10, basex +10, basey +10)
        
    elif whe==1:
        Canevas.itemconfig(Pion, outline ='white')
        Canevas.itemconfig(Pion2, outline ='blue')
        
        Canevas.coords(Base1,basex -10, basey -10, basex +10, basey +10)
        

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Epic Games')

# position initiale du pion
PosX = 460
PosY = 300

PosX2 = 20
PosY2 = 20

basexf = (20 * randint(1, 23))
baseyf = (20 * randint(1, 15))


# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='black')

Base1 = Canevas.create_rectangle(basexf,baseyf,basexf,baseyf,width=0.001,outline='gray',fill='gray')

Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='red',fill='red')
Pion2 = Canevas.create_oval(PosX2-10,PosY2-10,PosX2+10,PosY2+10,width=2,outline='blue',fill='blue')

Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.pack(padx =1, pady =1)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=1,pady=1)

Mafenetre.mainloop()
