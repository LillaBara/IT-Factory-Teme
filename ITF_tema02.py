#  S2_Sesiunea3_Exercitii
#  Partea 2 - Operatori, condiționale
from random import randint


# 16
'''16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
print(30 * ' ')
print('exercitiu 16')
string = 'Coral is either the stupidest animal or the smartest rock'
xx = int(input(f'Da un numar intre 0 si {len(string)}: '))
if 0 <= xx <= len(string):
    stringscurtat = string[:(len(string) - xx)]   # stringscurtat = string[: -xx)]
    print(stringscurtat)
else:
    print('Ai dat numar din afara intervalului')

# 17
'''Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.'''
print(30 * ' ')
print('exercitiu 17')
stringnou = string[:5] + string[-5:]
print(stringnou)

# 18
'''
18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' 
'''
print(30 * ' ')
print('exercitiu 18')
rockindex = string.index('rock')
print(f'Indexul de start a cuvantului rock este: {rockindex}')
print('Verificare:', string[rockindex:(rockindex + 4)])
print(string[:rockindex])

# 19
'''
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''
print(30 * ' ')
print('exercitiu 19')
value = randint(1, 6)
dice_roll = int(input('Ce numar ai dat cu zarul: '))
if not (1 <= dice_roll <= 6):      # in range(1,6)
    print('Ai dat numar invalid de zar')
elif dice_roll < value:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {value}.')
elif dice_roll > value:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {value}.')
else:
    print(f'Ai ghicit. Felicitări! Ai ales {dice_roll} si zarul a fost {value}.')

# 20
'''
20. Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''
print(30 * ' ')
print('exercitiu 20')
# nu stiu
propozitie = input("Introduceti propozitia: ")
primul_caracter = propozitie[0].upper()
ultimul_caracter = propozitie[-1].upper()
print(f'Primul_caracter este {primul_caracter}')
print(f'Ultimul_caracter este {ultimul_caracter}')
assert primul_caracter == ultimul_caracter, 'Primul caracter nu este egal cu ultimul'



# 21
'''
21. Având stringul '0123456789'
Afișează doar numerele pare 
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''
print(30 * ' ')
print('exercitiu 21')
numere = '0123456789'

lungimestring = len(numere)
print('Numerele pare sunt:')
while lungimestring > 0:
    # verificam daca e par
    if int(numere[lungimestring-1])%2 == 0:
        print(numere[lungimestring-1])
    lungimestring = lungimestring - 1

lungimestring = len(numere)
print('Numerele impare sunt:')
while lungimestring > 0:
    # verificam daca e par
    if int(numere[lungimestring-1])%2 != 0:
        print(numere[lungimestring-1])
    lungimestring = lungimestring - 1

