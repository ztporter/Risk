# risksim.py
# Zach Porter
# pre: number of attackers and defenders
# post: average loss for each and chance of victory

from random import*

def main():
    atroop = int(input("Number of attacking troops: "))
    while atroop <2:
        atroop = int(input("Number of attacking troops: "))
    dtroop = int(input("Number of defending troops: "))
    while dtroop<1:
        dtroop = int(input("Number of defending troops: "))
    aloss = 0
    dloss = 0
    v = 0
    for i in range(10000):
        acount = atroop
        dcount = dtroop
        while dcount>0 and acount>1:
            if acount>3:
                attlist=[]
                dflist=[]
                for j in range(3):
                    attlist.append(randrange(1,7))
                    high = attlist[0]
                for dice in attlist:
                    if dice>high:
                        high = dice
                attlist.remove(high)
                high2 = attlist[0]
                for dice in attlist:
                    if dice>high2:
                        high2 = dice
                if dcount>=2:
                    for j in range(2):
                        dflist.append(randrange(1,7))
                    if dflist[0]>=dflist[1]:
                        dhigh = dflist[0]
                        dhigh2 = dflist[1]
                    else:
                        dhigh = dflist[1]
                        dhigh2 = dflist[0]
                    if high > dhigh:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
                    if high2>dhigh2:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
                elif dcount==1:
                    dhigh = randrange(1,7)
                    if high > dhigh:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
            elif acount==3:
                attlist = []
                dflist = []
                for j in range(2):
                    attlist.append(randrange(1,7))
                    high = attlist[0]
                if attlist[0]>=attlist[1]:
                        high = attlist[0]
                        high2 = attlist[1]
                else:
                    high = attlist[1]
                    high2 = attlist[0]
                if dcount>=2:
                    for j in range(2):
                        dflist.append(randrange(1,7))
                    if dflist[0]>=dflist[1]:
                        dhigh = dflist[0]
                        dhigh2 = dflist[1]
                    else:
                        dhigh = dflist[1]
                        dhigh2 = dflist[0]
                    if high > dhigh:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
                    if high2>dhigh2:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
                elif dcount==1:
                    dhigh = randrange(1,7)
                    if high > dhigh:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
            elif acount==2:
                dflist = []
                high = randrange(1,7)
                if dcount>=2:
                    for j in range(2):
                        dflist.append(randrange(1,7))
                    if dflist[0]>=dflist[1]:
                        dhigh = dflist[0]
                    else:
                        dhigh = dflist[1]
                    if high > dhigh:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
                elif dcount==1:
                    dhigh = randrange(1,7)
                    if high > dhigh:
                        dcount-=1
                        dloss+=1
                    else:
                        acount-=1
                        aloss+=1
        if dcount == 0:
            v+=1
    print("Average attacker troop loss: ",(aloss/10000))
    print("Average defender troop loss: ",(dloss/10000))
    print("Chance of victory: ",(v/10000*100),'%')
    
main()            
