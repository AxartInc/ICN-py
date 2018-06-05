import random

def init(taille):
    
    grille=[]
    
    for i in range(taille):
        grille.append(taille*[0])
    
    x = random.randint(0, taille)
    y = random.randint(0, taille)
    
    grille[x][y]=1
    
    return grille
    
    
def proba(P):
    tirage = random.random()
    if P <= tirage:
        return 0
    else:
        return 1
        
def infectable(i,j):
    
    if i == 0 and j == 0:
        if grille[i+1][j+1] == 1 or grille[i+1][j] == 1 or grille[i][j+1] == 1:
            return true
        else:
            return false
            
    elif i==taille-1 and j == 0
    if grille[i-1][j]==1 or grille[i][j+1]==1 or grille[i-1][j+1]==1:
        return true
    else:
        return false
    
    elif i==0 and j == taille-1
    if grille[i+1][j-1]==1 or grille[i+1][j]==1 or grille[i][j-1]==1:
        return true
    else:
        return false
        
        #not finish next
        
    elif i==0 and j == 0
    if grille[i-1][j]==1 or grille[i][j+1]==1 or grille[i-1][j+1]==1:
        return true
    else:
        return false
    
    
    
    if grille[i+1][j+1]==1 or grille[i][j+1]==1 or grille[i+1][j]==1 or grille[i][j-1]==1 or grille[i-1][j+1]==1 or grille[i-1][j-1]==1 or grille[i-1][j]==1 or grille[i+1][j-1]==1:  
        return 1
    else:
        return 0
        


        

    
    
