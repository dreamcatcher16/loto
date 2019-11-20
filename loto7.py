import random
import numpy
brojevi = [0,0,0,0,0,0,0]

def median(x):
    if len(x)%2 != 0:
        return sorted(x)[len(x)//2]
    else:
        midavg = (sorted(x)[len(x)//2] + sorted(x)[len(x)//2-1])/2.0
        return midavg



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

brojac1 = 0 
brojac2 = 0 
brojac3 = 0 
brojac4 = 0 
brojac5 = 0 
brojac6 = 0 
brojac7 = 0 
brojac8 = 0
brojac9 = 0 
brojac10 = 0 
brojac11 = 0 
brojac12 = 0 
brojac13 = 0 
brojac14 = 0 


brojpogodaka = 6
poslenizvlacenja = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for pokusaj in range (20):
    brojac1 = 0 
    brojac2 = 0 
    brojac3 = 0 
    brojac4 = 0 
    brojac5 = 0 
    brojac6 = 0 
    brojac7 = 0 
    brojac8 = 0
    brojac9 = 0 
    brojac10 = 0 
    brojac11 = 0 
    brojac12 = 0 
    brojac13 = 0 
    brojac14 = 0 

    brojizvlacenja = 0

    while (brojac1 or brojac2 or brojac3 or brojac4 or brojac5 or brojac6 or brojac7 or 
    brojac8 or brojac9 or brojac10 or brojac11 or brojac12 or brojac13 or brojac14) < brojpogodaka:
        brojizvlacenja += 1
        izvucenakombinacija1 = sorted(izaberi7(brojevi))

        mkomb1 = sorted(izaberi7(brojevi))
        mkomb2 = sorted(izaberi7(brojevi))
        mkomb3 = sorted(izaberi7(brojevi))
        mkomb4 = sorted(izaberi7(brojevi))
        mkomb5 = sorted(izaberi7(brojevi))
        mkomb6 = sorted(izaberi7(brojevi))
        mkomb7 = sorted(izaberi7(brojevi))
        mkomb8 = sorted(izaberi7(brojevi))
        mkomb9 = sorted(izaberi7(brojevi))
        mkomb10 = sorted(izaberi7(brojevi))
        mkomb11 = sorted(izaberi7(brojevi))
        mkomb12 = sorted(izaberi7(brojevi))
        mkomb13 = sorted(izaberi7(brojevi))
        mkomb14 = sorted(izaberi7(brojevi))
        

        istielementi1 = [i for i, j in zip(izvucenakombinacija1, mkomb1) if i == j]
        istielementi2 = [i for i, j in zip(izvucenakombinacija1, mkomb2) if i == j]
        istielementi3 = [i for i, j in zip(izvucenakombinacija1, mkomb3) if i == j]
        istielementi4 = [i for i, j in zip(izvucenakombinacija1, mkomb4) if i == j]
        istielementi5 = [i for i, j in zip(izvucenakombinacija1, mkomb5) if i == j]
        istielementi6 = [i for i, j in zip(izvucenakombinacija1, mkomb6) if i == j]
        istielementi7 = [i for i, j in zip(izvucenakombinacija1, mkomb7) if i == j]
        istielementi8 = [i for i, j in zip(izvucenakombinacija1, mkomb8) if i == j]
        istielementi9 = [i for i, j in zip(izvucenakombinacija1, mkomb9) if i == j]
        istielementi10 = [i for i, j in zip(izvucenakombinacija1, mkomb10) if i == j]
        istielementi11 = [i for i, j in zip(izvucenakombinacija1, mkomb11) if i == j]
        istielementi12 = [i for i, j in zip(izvucenakombinacija1, mkomb12) if i == j]
        istielementi13 = [i for i, j in zip(izvucenakombinacija1, mkomb13) if i == j]
        istielementi14 = [i for i, j in zip(izvucenakombinacija1, mkomb14) if i == j]

        brojac1 = len(istielementi1)
        brojac2 = len(istielementi2)
        brojac3 = len(istielementi3)
        brojac4 = len(istielementi4)
        brojac5 = len(istielementi5)
        brojac6 = len(istielementi6)
        brojac7 = len(istielementi7)
        brojac8 = len(istielementi8)
        brojac9 = len(istielementi9)
        brojac10 = len(istielementi10)
        brojac11 = len(istielementi11)
        brojac12 = len(istielementi12)
        brojac13 = len(istielementi13)
        brojac14 = len(istielementi14)
        

    #print (izvucenakombinacija1)
    #print (mkomb1, mkomb2, mkomb3, mkomb4)
    #print (mkomb5, mkomb6, mkomb7, mkomb8)
    #print (mkomb9, mkomb10, mkomb11, mkomb12)
    #print (mkomb13, mkomb14)
    print ('ovo je ', pokusaj,'. pokusaj.')
    print ('Potreban broj izvlacenja: ', brojizvlacenja)
    #print (brojpogodaka)
    poslenizvlacenja[pokusaj] = brojizvlacenja
print('Medijana je ', median(poslenizvlacenja), ' za ', brojpogodaka, ' pogodjena broja.')
print(sorted(poslenizvlacenja))
