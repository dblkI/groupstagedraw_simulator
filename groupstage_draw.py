# Qatar 2022 world cup group stage draw
#
# Author: dblkl_

import random
from pure_eval import group_expressions


def run():

# Lists
    Pot1 = ['Qatar','Brazil','Belgium','France','Argentina','England','Spain','Portugal']
    Pot2 = ['Mexico','Netherlands','Denmark','Germany','Uruguay','Switzerland','USA','Croatia']
    Pot3 = ['Senegal','IR Iran','Japan','Morocco','Serbia','Poland','Korea Republic','Tunisia']
    Pot4 = ['Cameroon','Canada','Ecuador','Saudi Arabia','Ghana','CONMEBOL/AFC','CONCACAF/OFC','UEFA']

# Code starts here
    groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in groups:
        print("\nGROUP " +i)
        p = random.randint(0,len(Pot1)-1)
        print(Pot1[p])
        Pot1.pop(p)
        p = random.randint(0,len(Pot2)-1)
        print(Pot2[p])
        Pot2.pop(p)
        p = random.randint(0,len(Pot3)-1)
        print(Pot3[p])
        Pot3.pop(p)
        p = random.randint(0,len(Pot4)-1)
        print(Pot4[p])
        Pot4.pop(p)
        
        amount_ofteams = Pot1+Pot2+Pot3+Pot4
        if len(amount_ofteams) < 4:
            print("\nGroup stage draw is over\n")
        else:
            print("Amount of teams without group: " +str(len(amount_ofteams)))
    

if __name__ == '__main__':
    run()
