'''
Se dorește să se implementeze o aplicație de administrare a citirilor contoarelor de apa caldă și apa rece pentru o familie.
În fiecare lună o familie trebuie să predea valorile contoarelor de apă caldă și apă rece la administrator
împreună cu consumul pe luna curentă. Se dorește simplificarea acestei activități printr-o aplicație cu următoarele funcționalități:
Adăugare - citire pe o anumită luna
Ștergere - citire pe o anumită luna
Afișare consum - pe o anumită luna
Iesire
La adăugarea unei citiri utilizatorul trebuie să introducă anul și luna în format ian, feb, mar, ... dec,
apoi valoarea contorului de apa rece și valoarea contorului de apa calda.
Utilizatorul va primi un mesaj de eroare dacă anul sau luna nu sunt corecte, dacă deja exista o citire pentru luna respectivă
sau valoarea contoarelor este invalida (valoarea curentă a contorului este mai mică decât valoarea de pe luna precedentă).
La ștergerea unei citiri utilizatorul trebuie să introducă anul și luna. Se va primi un mesaj de eroare dacă anul și
luna sunt invalide sau nu există o citire pentru anul și luna introduse.
La afișare se vor afișa valorile contoarelor pe luna precedenta și luna curentă și în plus consumul pe luna curentă, exemplu:
ian 2018
Apa calda 100
Apă rece 105
feb 2018 consum
104 4
110 5
La introducerea lunilor programul trebuie să fie case insensitive, adică atât “feb” cât și “FEB” înseamna același lucru.
Valoarea anului nu trebuie validata în vreun fel.
Nu se dorește salvarea datelor astfel încât acestea să rămână persistente după oprirea programului.

'''
import datetime

print('APOMETRU pt FAMILIA POP:')
print(' ')

list_month = ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'nov', 'dec']
apa_calda = {
    0: 30,
    1: 33,
    2: 36,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}
apa_rece = {
    0: 45,
    1: 50,
    2: 55,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}

print(' ')
print('Alege o optiune')
print('1. Adaugare')
print('2. Stergere')
print('3. Afisare consum')
print('4. Iesire')
option = int(input('Scrie numarul actiunii dorit: '))

while option != 4:  # pana cand nu cere iesirea, se poate manevra intre optiuni
    y = int(input('Da te rog anul: '))
    while y != datetime.datetime.today().year:
        y = int(input('Ai gresit anul, da te rog din nou: '))
    m = input('Da te rog luna: ')
    while m.lower()[:3] not in list_month:
        m = input('Ai scris o luna inexistenta, da te rog din nou: ')

    index_month = list_month.index(m.lower()[:3])

    if option == 1:  # Optiunea adaugare
        curent_warm = int(input('Adauga valoarea pentru apa calda: '))
        if apa_calda[index_month] > 0:
            print(f'Ai introdus deja valoarea, si este {apa_calda[index_month]}')
        else:
            while curent_warm < apa_calda[index_month - 1]:
                print(f'Ai gresit, trebuie sa fie mai mare valoarea ca: {apa_calda[index_month - 1]}')
                curent_warm = int(input('Adauga valoarea pentru apa calda: '))

            apa_calda[
                index_month] = curent_warm  # cand deja e mai mare iese din while, si il pune in ddictionar valoarea

        curent_cold = int(input('Adauga valoarea pentru apa rece: '))
        if apa_rece[index_month] > 0:
            print(f'Ai introdus deja valoarea, si este {apa_rece[index_month]}')
        else:
            while curent_cold < apa_rece[index_month - 1]:
                print(f'Ai gresit, trebuie sa fie mai mare valoarea ca: {apa_rece[index_month - 1]}')
                curent_cold = int(input('Adauga valoarea pentru apa rece:'))

            apa_rece[index_month] = curent_cold

    elif option == 2:  # Optiunea Stergere
        if apa_calda[index_month] == 0 and apa_rece[index_month] == 0:
            print(f'Nu exista valori care se poate sterge pentru luna {m}')
        else:
            apa_rece[index_month] = 0
            apa_calda[index_month] = 0

    elif option == 3:  # Optiunea consum
        print(f'Indexul pentru {y}-{list_month[index_month - 1]}:')
        print(f'Apa calda: {apa_calda[index_month - 1]}')
        print(f'Apa rece: {apa_rece[index_month - 1]}')
        print(f'Indexul pentru {y}-{list_month[index_month]}:')
        print(f'Apa calda: {apa_calda[index_month]}')
        print(f'Apa rece: {apa_rece[index_month]}')
        print(f'Consumul:')
        print(f'Apa calda: {apa_calda[index_month] - apa_calda[index_month - 1]}')
        print(f'Apa rece: {apa_rece[index_month] - apa_rece[index_month - 1]}')

    option = int(input('Scrie numarul actiunii dorit: '))  # Cerem din nou, ce vrea sa faca
