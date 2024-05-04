import math

# 1.Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
print('')
print('1. Clasa Cerc:')

class Cerc:

    def __init__(self, raza, color):
        self.raza = raza
        self.color = color

    def descriere_cerc(self):
        print(f'Culoarea cercului este: {self.color}')
        print(f'Raza cercului este: {self.raza}')

    def aria(self):
        aria = self.raza**2 * math.pi
        return aria

    def diametru(self):
        return 2 * self.raza  # lehet igy is, nem kell egy kulon valtozo, egybol az egyenlet eremenyet adja vissza

    def circumferinta(self):
        return 2 * self.raza * math.pi

circle = Cerc(5, 'Rosu')
circle.descriere_cerc()
print(f'Aria cercului este: {circle.aria(): .2f}')
print(f'Diametru cercului este: {circle.diametru(): .2f}')
print(f'Circumferinta cercului este: {circle.circumferinta(): .2f}')

# 2. Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Poți verifica schimbarea culorii prin apelarea metodei descrie().

print('')
print('1. Clasa Dreptunghi:')

class Dreptunghi:

    def __init__(self, lung, lat, color):
        self.lung = lung
        self.lat = lat
        self.color = color

    def descriere_drept(self):
        print(f'Culoarea dreptunghiului este: {self.color}')
        print(f'Lungimea dreptunghiului este: {self.lung}')
        print(f'Latimea dreptunghiului este: {self.lat}')

    def aria(self):
        aria = self.lung * self.lat
        return aria

    def perimetrul(self):
        p = 2 * self.lung + 2 * self.lat
        return p

    def schimbă_culoarea(self, color_nou):
        self.color = color_nou


rectangle = Dreptunghi(3,5, 'Verde')
rectangle.descriere_drept()
print('')
print(f'Aria dreptunghiului este: {rectangle.aria():}')
print(f'Perimetrul dreptunghiului este: {rectangle.perimetrul():}')
print('')
rectangle.schimbă_culoarea('Galben')
rectangle.descriere_drept()
