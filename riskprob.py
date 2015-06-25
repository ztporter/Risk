
# riskprob.py
# Zach Porter

from random import*

def main():
    att = int(input("Enter number of attacking die (1-3): "))
    while att<1 or att>3:
        att = int(input("Enter number of attacking die (1-3): "))
    df = int(input("Enter number of defending die (1-2): "))
    while df<1 or df>2:
        df = int(input("Enter number of defending die (1-2): "))
    aloss = 0
    dloss = 0
    for i in range(1000000):
        attlist = []
        for i in range(att):
            attlist.append(randrange(1,7))
        dflist = []
        for i in range(df):
            dflist.append(randrange(1,7))
        if df == 1:
            high = attlist[0]
            for dice in attlist:
                if dice>high:
                    high = dice
            if high > dflist[0]:
                dloss+=1
            else:
                aloss+=1
        else:
            if len(attlist)==1:
                if len(dflist)==1:
                    if attlist>dflist:
                        dloss+=1
                    else:
                        aloss+=1
                else:
                    if attlist>dflist:
                        dloss+=1
                    else:
                        aloss+=1
            else:
                high = attlist[0]
                for dice in attlist:
                    if dice>high:
                        high = dice
                attlist.remove(high)
                high2 = attlist[0]
                for dice in attlist:
                    if dice>high2:
                        high2 = dice
                if dflist[0]>=dflist[1]:
                    dhigh = dflist[0]
                    dhigh2 = dflist[1]
                else:
                    dhigh = dflist[1]
                    dhigh2 = dflist[0]
                if high>dhigh:
                    dloss+=1
                else:
                    aloss+=1
                if high2>dhigh2:
                    dloss+=1
                else:
                    aloss+=1
    print("average loss for attacker is: ",(aloss/1000000))
    print("average loss for defender is: ",(dloss/1000000))
main()
