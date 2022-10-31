#Tri pas tas 

def entasser_max(l,n,i):
    max_val = i
    gauche= 2*i+1
    droite = 2*i+2
    
    if gauche<n and l[max_val]< l[gauche]:
            max_val = gauche
    
    if droite < n and l[max_val]< l[droite]:
        max_val = droite

    if max_val!=i:
        l[i],l[max_val] = l[max_val],l[i]
        
        entasser_max(l, n, max_val)
      
def contruire_tas_max(l):
    n = len(l)

    for i in range((n//2), -1,-1):
       entasser_max(l, n, i)

def tri_pas_tas(l):
    n = len(l)
    contruire_tas_max(l)

    for i in range(n-1,-1,-1):

        l[i], l[0] = l[0],l[i]
        entasser_max(l, i, 0)

l = [11,39,9,2,8,87,92,74,6]
print(f'Tableau non trier: {l}')
tri_pas_tas(l)
print(f'Tableau trier {l}')
