# Qatar 2022 world cup group stage draw
#
# Author: dblkl_

import random

from pure_eval import group_expressions


def run():

    # Dictionaries
    Pot1 = [
        'Qatar',
        'Brazil',
        'Belgium',
        'France',
        'Argentina',
        'England',
        'Spain',
        'Portugal'
    ]

    Pot2 = [
        'Mexico',
        'Netherlands',
        'Denmark',
        'Germany',
        'Uruguay',
        'Switzerland',
        'USA',
        'Croatia'
    ]

    Pot3 = [
        'Senegal',
        'IR Iran',
        'Japan',
        'Morocco',
        'Serbia',
        'Poland',
        'Korea Republic',
        'Tunisia'
    ]

    Pot4 = [
        'Cameroon',
        'Canada',
        'Ecuador',
        'Saudi Arabia',
        'Ghana',
        'CONMEBOL/AFC',
        'CONCACAF/OFC',
        'UEFA'
    ]


# Code starts here

   
    print("\nGROUP A")
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

    print("\nGROUP B")
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

    print("\nGROUP C")
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

    print("\nGROUP D")
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

    print("\nGROUP E")
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

    print("\nGROUP F")
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

    print("\nGROUP G")
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

    print("\nGROUP H")
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
# Print results
    #teams = Pot1 + Pot2 + Pot3 + Pot4
    #print("\nPot1: " + str(Pot1))
    #print("Pot2: " + str(Pot2))
    #print("Pot3: " + str(Pot3))
    #print("Pot4: " + str(Pot4))
    #print("\nParticipating national teams: " + str(len(teams)))
    

if __name__ == '__main__':
    run()
