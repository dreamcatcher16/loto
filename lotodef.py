import random
import numpy
brojevi = [0,0,0,0,0,0,0]


def izaberi7(lotobrojevi):

    lotobrojevi = [0,0,0,0,0,0,0]
    lotobrojevi[0] = random.randrange(1,40,1)
    j = 0
    #print (lotobrojevi)
    while j < 6:
        k = 0
        j += 1
        #lotobrojevi[i] = 1+random.randint(0,38)
        lotobrojevi[j] = random.randrange(1,40,1)
        while lotobrojevi[k] == lotobrojevi[j]:
        #for k in range(0,j-1):
            #if lotobrojevi[k] == lotobrojevi[j]:
            lotobrojevi[k] = random.randrange(1,40,1)
        k +=1
    return lotobrojevi

s = sorted(izaberi7(brojevi))   
print (s)