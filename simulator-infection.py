import random
import matplotlib.pyplot as plt
import numpy as np
def init(taille):
    grille=[]
    for i in range(taille):
        grille.append(taille*[0])
    x=random.randint(0,taille)
    y=random.randint(0,taille)
    grille[x][y]=1
    return grille
def proba(p):
    tirage=random.random()
    if p<=tirage:
        return 0
    else:
        return 1

def exposition(i,j):
    taille=len(grille)
    if i==0 and j==0:
        if grille[i+1][j]==1 or grille[i+1][j+1]==1 or grille[i][j+1]==1:
            return True
        else:
            return False
    elif i==0 and j==taille-1:
        if grille[i+1][j]==1 or grille[i+1][j-1]==1 or grille[i][j-1]==1:
            return True
        else:
            return False
    elif i==taille-1 and j==0:
        if grille[i][j+1]==1 or grille[i-1][j]==1 or grille[i-1][j+1]==1:
            return True
        else:
            return False
    elif i==taille-1 and j==taille-1:
        if grille[i][j-1]==1 or grille[i-1][j]==1 or grille[i-1][j-1]==1:
            return True
        else:
            return False
    elif i==0:
        if grille[i][j-1]==1 or grille[i][j+1]==1 or grille[i+1][j+1]==1 or grille[i+1][j-1]==1 or grille[i+1][j]==1:
            return True
        else:
            return False
    elif i==taille-1:
        if grille[i][j-1]==1 or grille[i][j+1]==1 or grille[i-1][j+1]==1 or grille[i-1][j-1]==1 or grille[i-1][j]==1:
            return True
        else:
            return False
    elif j==0:
        if grille[i][j+1]==1 or grille[i+1][j+1]==1 or grille[i-1][j+1]==1 or grille[i-1][j]==1 or grille[i+1][j]==1:
            return True
        else:
            return False
    elif j==taille-1:
        if grille[i][j-1]==1 or grille[i-1][j-1]==1 or grille[i+1][j-1]==1 or grille[i-1][j]==1 or grille[i+1][j]==1:
            return True
        else:
            return False
    else:
        if grille[i-1][j-1]==1 or grille[i-1][j]==1 or grille[i-1][j+1]==1 or grille[i][j+1]==1 or grille[i+1][j]==1 or grille[i-1][j+1]==1 or grille[i][j-1]==1 or grille[i+1][j+1]==1:
            return True
        else:
            return False

from copy import deepcopy
grille=init(100)
grille_init=deepcopy(grille)
for k in range(100):
    H=deepcopy(grille)
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]==0 and exposition(i,j)==True and proba(0.5):
                H[i][j]=1
            elif grille[i][j]==1:
                if proba(0.6)==0:
                    H[i][j]=3
                else :
                    H[i][j]=2
            else:
                H[i][j]=grille[i][j]
    grille=H
    plt.imshow(np.array(H),interpolation='nearest')
    plt.pause(0.01)