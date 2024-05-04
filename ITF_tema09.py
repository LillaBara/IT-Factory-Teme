print(30 * ' ')
print('14. max:')
# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
def maximum(a, b, c):
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    else:
        max = c
    return max


print('numarul cel mai mare:', maximum(3, 3, 4))

print(30 * ' ')
print('15. suma numerelor pana la x:')


# 15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

def suma_numere(x):
    suma = 0
    for i in range(x + 1):
        suma = suma + i
    return suma


print(suma_numere(3))

print(30 * ' ')
print('16. numere comune in doua liste:')


# 16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def nr_comune(lista1, lista2):
    raspuns = []
    for cifra in lista1:
        if cifra in lista2:
            raspuns.append(cifra)
    return raspuns


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(nr_comune(list1, list2))

print(30 * ' ')
print('17. reducere pret:')


# 17. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.

def reducere(pret, reduc):
    if 0 < reduc < 100:
        pret_nou = pret - (pret * reduc / 100)
        return pret_nou
    else:
        print(f'Reducerea de {reduc} e invalida, pretul ramane cel initial')
        return pret


print(reducere(250, 20))

print(30 * ' ')
print('18. data/ora curenta:')

#  18.Funcție care să afișeze data și ora curentă din România.
# (bonus: afișazăi și data și ora curentă din China)

from datetime import datetime
from pytz import timezone
import time


def data_ora():
    x = datetime.now()
    print(f'Data si ora curenta in Romania: {x.strftime("%Y/%m/%d %X")}')
    y = datetime.now(timezone('Asia/Shanghai'))
    print(f'Data si ora curenta in China: {y.strftime("%Y/%m/%d %X")}')

data_ora()

print(30 * ' ')
print('6. numere prime:')


#  6. Să se tipărească toate numerele prime aflate între doi întregi citiţi.
#  Programul va folosi o funcţie care testează dacă un număr este prim sau nu.

def numere_prime(nr1, nr2):
    lista_prime = []
    for numar in range(nr1 + 1, nr2):
        for i in range(2, numar):
            if numar % i == 0:
                break
        else:
            lista_prime.append(numar)
    return lista_prime


print('Numere prime:', numere_prime(4, 50))

print(30 * ' ')
print('7. divid cu suma cifrelor:')


#  7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite,
#  numere care se divid cu suma cifrelor lor.
#  Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.

def suma_cifre(nr):
    suma = 0
    string_nr = str(nr)
    for i in range(len(string_nr)):
        suma = suma + int(str(nr)[i])
    return suma


x = int(input('da prima numar: '))
y = int(input('da a doua numar: '))
if x > y:
    c = y
    y = x
    x = c

lista_numere = []

for i in range(x + 1, y):
    if i % suma_cifre(i) == 0:
        # print(f'Numarul {i} se divide cu suma cifrelor({suma_cifre(i)}).')
        lista_numere.append(i)

print(lista_numere)


