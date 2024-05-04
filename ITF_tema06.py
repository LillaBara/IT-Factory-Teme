'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
'''

print(30 * '-')
print('Exercitiu 1:')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# prin iterare:
# for i in range(len(masini)):
#     print('Masina mea preferata este', masini[i])

# cu for each:
# for i in masini:
#     print('Masina mea preferata este',i)

# while:
i = 0
while i < len(masini):
    print('Masina mea preferata este', masini[i])
    i += 1

'''
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
'''

print(30 * '-')
print('Exercitiu 2:')
for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
    print(masini)

# varianta 2
print(30 * '-')
print('Exercitiu 2: varianta 2')

for index, elem in enumerate(
        masini):  # functia enumerate este folosita pt a obtine indexul cat si valoarea fiecare element din lista
    print(index, elem)
    if index == 0 or index == len(masini) - 1:
        masini[index] = elem.upper()
    else:
        masini[index] = elem.lower()
else:
    print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
'''

print(30 * '-')
print('Exercitiu 3:')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Mercedes':
        print('Am gasit masina dorita, Mercedes.')
        break
    else:
        print(f'Am gasit masina {i}. Mai cautam')

'''
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.

'''

print(30 * '-')
print('Exercitiu 4:')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Trabant' or i == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {i}')
