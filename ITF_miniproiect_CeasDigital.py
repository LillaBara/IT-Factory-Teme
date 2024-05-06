'''
Să se realizeze o aplicație care afișează ora curentă sub forma unui ceas digital în mod text,
folosind caracterele _ și | astfel:
Ora curentă se va afișa la interval de 1 secundă. Valorile mai mici de 10 vor fi precedate de un 0.
Atenție la fusul orar, e posibil ca la ore să trebuiască adăugată o anumită valoare pentru a obține ora României.
Pentru separatorii dintre valori se va folosi caracterul 'o’.

Fiecare cifra din afișaj ar trebui să ocupe 4 caractere, iar punctele de separare - 3 caractere.

'''

import datetime


cifre = [
    {
        1: ' __ ',
        2: '|  |',
        3: '|__|'
    },
    {
        1: '    ',
        2: '   |',
        3: '   |'
    },
    {
        1: ' __ ',
        2: ' __|',
        3: '|__ '
    },
    {
        1: ' __ ',
        2: ' __|',
        3: ' __|'
    },
    {
        1: '    ',
        2: '|__|',
        3: '   |'
    },
    {
        1: ' __ ',
        2: '|__ ',
        3: ' __|'
    },
    {
        1: ' __ ',
        2: '|__ ',
        3: '|__|'
    },
    {
        1: ' __ ',
        2: '   |',
        3: '   |'
    },
    {
        1: ' __ ',
        2: '|__|',
        3: '|__|'
    },
    {
        1: ' __ ',
        2: '|__|',
        3: ' __|'
    }
]

ora = str(datetime.datetime.now().time())
print(ora)
# separ cifrele pentru ora, minut si secunda
unu = int(ora[0])
doi = int(ora[1])
trei = int(ora[3])
patru = int(ora[4])
cinci = int(ora[6])
sase = int(ora[7])

print(cifre[unu][1], cifre[doi][1], ' ', cifre[trei][1], cifre[patru][1], ' ', cifre[cinci][1], cifre[sase][1])
print(cifre[unu][2], cifre[doi][2], 'o', cifre[trei][2], cifre[patru][2], 'o', cifre[cinci][2], cifre[sase][2])
print(cifre[unu][3], cifre[doi][3], 'o', cifre[trei][3], cifre[patru][3], 'o', cifre[cinci][3], cifre[sase][3])
