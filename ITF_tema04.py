# Ex.1 Declară o listă note_muzicale în care să pui do re mi etc până la do:

print(30*'-')
print('Exercitiu 1')
note_muzicala = ['do','re','mi','fa','so','la','si','do']
print('Nota muzicala:', note_muzicala)
note_muzicala = note_muzicala[::-1]
print('Nota muzicala inversata:', note_muzicala)
note_muzicala.reverse()
print('Folosit metoda reverse:', note_muzicala)

# Ex.2 De câte ori apare ‘do’?
print(30*'-')
print('Exercitiu 2: De câte ori apare "do"?')
do = note_muzicala.count('do')
print(f'Nota muzicala "do" apare de {do} ori')

# Ex.3 Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
print(30*'-')
print('Exercitiu 3 - Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.')
note_tuple = tuple(note_muzicala)
print('In format tuple, asa arata:', note_tuple)
# nota_tupla = nota_tupla.__add__('re')
re_tupla = ('re','mi')
note_tuple = note_tuple.__add__(re_tupla)
print('Se poate adauga in tupla noua element, ca o noua tupla cu functia __add__: ', note_tuple)
note_tuple = note_tuple + ('re',)
print('Se poate adauga in tupla noua element cu modul de a aduna doua truple ()+(): ', note_tuple)

print(type(note_tuple))

# Ex.4  Declara un dictionar cu notele muzicale de mai sus.
# Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. Afiseaza-l.
print(30*'-')
print('Exercitiu 4 - Declara un dictionar cu notele muzicale de mai sus.')
note_dict = {
    'do':note_muzicala.count('do'),
    're':note_muzicala.count('re'),
    'mi':note_muzicala.count('mi'),
    'fa':note_muzicala.count('fa'),
    'so':note_muzicala.count('so'),
    'la':note_muzicala.count('la'),
    'si':note_muzicala.count('si')

}
print('Dictionar cu notele muzicala:', note_dict)