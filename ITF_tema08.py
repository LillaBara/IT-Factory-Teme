# 2.

import math


def detaliipatrat(latura):
    diagonala = latura * math.sqrt(2)  # este radacina patrata din 2
    perimetru = 4 * latura
    return diagonala, perimetru


lungimelatura = 4
diagonala, perimetru = detaliipatrat(lungimelatura)
print(f'diagonala patratului: {diagonala: .2f}, perimetru: {perimetru}')
        # .2f - hany tizedessel jelenitse meg az eredmenyt


# 3.
def lungimeipotenuza(cateta1, cateta2):
    ipotenuza_patrat = cateta1 ** 2 + cateta2 ** 2
    return math.sqrt(ipotenuza_patrat)


# cateta1 = 6
# cateta2 = 8
print('atlo hossza:', lungimeipotenuza(5, 4))


# 4.
def poate_forma_triunghi(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a, b, c, 'pot forma un triunghi'  # segmentele pot forma un triunghi
    else:
        return a, b, c, 'nu pot forma un triunghi'  # segmentele nu pot forma triunghi

print(poate_forma_triunghi(3,5,7))
print(poate_forma_triunghi(1,2,3))
