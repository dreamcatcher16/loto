import random
import numpy
brojevi = [0,0,0,0,0,0,0]

def izaberi7(lotobrojevi):

    lotobrojevi = [0,0,0,0,0,0,0]
    res = [0,0,0,0,0,0,0]
    
    #print (lotobrojevi)
    while len(res) > 0:
        lotobrojevi[0] = random.randrange(1,40,1)
        lotobrojevi[1] = random.randrange(1,40,1)
        lotobrojevi[2] = random.randrange(1,40,1)
        lotobrojevi[3] = random.randrange(1,40,1)
        lotobrojevi[4] = random.randrange(1,40,1)
        lotobrojevi[5] = random.randrange(1,40,1)
        lotobrojevi[6] = random.randrange(1,40,1)
        res = [idx for idx, val in enumerate(lotobrojevi) if val in lotobrojevi[:idx]] 
        

    return lotobrojevi

s = sorted(izaberi7(brojevi))   

mkomb1 = sorted(izaberi7(brojevi))
mkomb2 = sorted(izaberi7(brojevi))
mkomb3 = sorted(izaberi7(brojevi))
mkomb4 = sorted(izaberi7(brojevi))
mkomb5 = sorted(izaberi7(brojevi))
mkomb6 = sorted(izaberi7(brojevi))
mkomb7 = sorted(izaberi7(brojevi))
mkomb8 = sorted(izaberi7(brojevi))

#print (s, mkomb1, mkomb2, mkomb3, mkomb4)
#print (mkomb5, mkomb6, mkomb7, mkomb8)
brojac1 = 0 
brojac2 = 0 
brojac3 = 0 
brojac4 = 0 
brojac5 = 0 
brojac6 = 0 
brojac7 = 0 
brojac8 = 0
brojizvlacenja = 0
while (brojac1 or brojac2 or brojac3 or brojac4 or brojac5 or brojac6 or brojac7 or brojac8) < 6:
    brojizvlacenja += 1
    izvucenakombinacija1 = sorted(izaberi7(brojevi))
    istielementi1 = [i for i, j in zip(izvucenakombinacija1, mkomb1) if i == j]
    istielementi2 = [i for i, j in zip(izvucenakombinacija1, mkomb2) if i == j]
    istielementi3 = [i for i, j in zip(izvucenakombinacija1, mkomb3) if i == j]
    istielementi4 = [i for i, j in zip(izvucenakombinacija1, mkomb4) if i == j]
    istielementi5 = [i for i, j in zip(izvucenakombinacija1, mkomb5) if i == j]
    istielementi6 = [i for i, j in zip(izvucenakombinacija1, mkomb6) if i == j]
    istielementi7 = [i for i, j in zip(izvucenakombinacija1, mkomb7) if i == j]
    istielementi8 = [i for i, j in zip(izvucenakombinacija1, mkomb8) if i == j]
    brojac1 = len(istielementi1)
    brojac2 = len(istielementi2)
    brojac3 = len(istielementi3)
    brojac4 = len(istielementi4)
    brojac5 = len(istielementi5)
    brojac6 = len(istielementi6)
    brojac7 = len(istielementi7)
    brojac8 = len(istielementi8)

print (izvucenakombinacija1)
print (mkomb1, mkomb2, mkomb3, mkomb4, mkomb5, mkomb6, mkomb7, mkomb8)

print (brojizvlacenja)
