'''
Se dorește implementarea unei aplicații de tip mini - calculator în mod text în Python.
La pornire aplicația afișează valoarea inițială care este implicit 0.
Valoarea inițială se poate seta prin intermediul unui parametru din linia de comanda.
Apoi aplicația așteaptă o operație de la utilizator și afișează rezultatul acestuia.

Operațiile posibile sunt:
+număr - adună la valoarea curentă numărul respectiv
-număr - scade din valoarea curentă numărul respectiv
*număr - înmulțește valoarea curentă numărul respectiv
/număr - împarte valoarea curentă la numărul respectiv
=număr - setează valoarea curentă cu numărul respectiv
x - ieșire din program
După fiecare operație se va afișa valoarea curentă și se așteaptă din nou un input de la utilizator.
Linia pe care se așteaptă input-ul de la utilizator începe cu semnul "> ".

'''

print('CALCULATOR ( + , - , * , / , =) - cu x se iese')
print(' ')
x = 0.0
print(x)
y = input('> ')
while y.lower() != 'x':
    if y[0] == '+':
        x = x + int(y[1:])
    elif y[0] == '-':
        x = x - int(y[1:])
    elif y[0] == '*':
        x = x * int(y[1:])
    elif y[0] == '/':
        x = x / int(y[1:])
    elif y[0] == '=':
        x = int(y[1:])
    else:
        print('Invalid operation')
    print(x)
    y = input('> ')




