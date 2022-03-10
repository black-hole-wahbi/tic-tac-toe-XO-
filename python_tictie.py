import numpy as np
def saisir(n):
    while True:
        n=int(input("donne taille de matrice carre : "))
        if n>=3 :break
    return(n)
def remplir_matrice(m,n):
    s=0
    for j in range(n):
        for i in range(n):
            m[j][i]=str(s)
            s+=1
def pos_i(p,n,m):
    for j in range(n):
        for i in range(n):
            if str(m[j][i]) == "b'"+str(p)+"'" :
                return i
def pos_j(p,n,m):
    for j in range(n):
        for i in range(n):
            if str(m[j][i]) == "b'"+str(p)+"'" :
                return j
def verif(p,n,m,c):
    while p not in [str(h) for h in range(n*n)] :
        p=input('player  again: ')
    m[pos_j(p,n,m)][pos_i(p,n,m)]=c
def vertical(m,n,c,i):
    s=0
    for y in range(n):
        if str(m[y][i])=="b'"+c+"'" :
            s+=1
    return s
def horizontal(m,n,c,i):
    s=0
    for x in range(n):
        if str(m[i][x])=="b'"+c+"'" :
            s+=1
    return s
def diagonale(m,n,c):
    s=0
    s_i=0
    for j in range(n):
        for i in range(n):
            if (-j-i)==(-n+1) and str(m[j][i])=="b'"+c+"'" :
                s_i+=1
            if i==j and str(m[j][i])=="b'"+c+"'" :
                s+=1
    if n==s or n==s_i :
        return(True)
    return(False)
def victoire(m,n,c):
    b=False
    i=0
    while not b and i<= n-2 :
        if vertical(m,n,c,i)==n or horizontal(m,n,c,i)==n:
            b=True
        i+=1
    if diagonale(m,n,c) :
        b=True
    return b
def jeux(m,n):
    j=1
    while True :
        if j%2!=0 :
            p=input('player 1 : ')
            verif(p,n,m,"x")
        else :
            p2=input('player 2 : ')
            verif(p2,n,m,"o")
        j+=1
        print(m)
        if j==n*n or (victoire(m,n,"x") or victoire(m,n,"o") ):break;
    afficher(m,n)
def afficher(m,n):
    if victoire(m,n,"x") :
        print("jeuer 1 victoires .")
    elif victoire(m,n,"o") :
        print("jeuer 2 victoires .")
    else:
        print("personne n'a gagné .")

#programme principal 
n=int()
n=saisir(n)
m=np.chararray((n,n),itemsize=n)
remplir_matrice(m,n)
jeux(m,n)
