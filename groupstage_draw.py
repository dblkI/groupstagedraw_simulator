# Qatar 2022 world cup group stage draw
#
# Author: dblkl_

import random
from pure_eval import group_expressions


def run():

    # Dictionaries
    Pot1 = ['Qatar','Brazil','Belgium','France','Argentina','England','Spain','Portugal']
    Pot2 = ['Mexico','Netherlands','Denmark','Germany','Uruguay','Switzerland','USA','Croatia']
    Pot3 = ['Senegal','IR Iran','Japan','Morocco','Serbia','Poland','Korea Republic','Tunisia']
    Pot4 = ['Cameroon','Canada','Ecuador','Saudi Arabia','Ghana','CONMEBOL/AFC','CONCACAF/OFC','UEFA']

# Code starts here
    amount_ofteams = Pot1+Pot2+Pot3+Pot4
    groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in groups:   
        print("\nGROUP " +i)
        p = random.randint(0,len(Pot1)-1)
        print(Pot1[p])
        Pot1.pop(p)
        print("amount of teams without group in Pot1: " +str(len(Pot1)))
        p = random.randint(0,len(Pot2)-1)
        print(Pot2[p])
        Pot2.pop(p)
        print("amount of teams without group in Pot2: " +str(len(Pot2)))
        p = random.randint(0,len(Pot3)-1)
        print(Pot3[p])
        Pot3.pop(p)
        print("amount of teams without group in Pot3: " +str(len(Pot3)))
        p = random.randint(0,len(Pot4)-1)
        print(Pot4[p])
        Pot4.pop(p)
        print("amount of teams without group in Pot4: " +str(len(Pot4)))
    

if __name__ == '__main__':
    run()
