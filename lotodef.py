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
print (s)