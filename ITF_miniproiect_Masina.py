'''
Mașină
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
descrie() - se vor printa toate atributele, în afară de culori_disponibile
înmatriculare() - va schimba atributul înmatriculată în True
vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
                    altfel afișați o eroare
accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare,
                        dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
franeaza() - mașina se va opri și va avea viteza 0

'''


class Masina:
    marca = 'Dacia'
    vit_act = 0
    color = 'gri'
    culori_disponibile = {'argint', 'rosu', 'verde', 'turcoaz', 'negru', 'alb'}
    inmat = False

    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def descrie(self):
        if self.inmat == True:
            if self.vit_act > 0:
                print(
                    f'Masina {self.marca}-{self.model} cu culoarea {self.color} are viteza maxima {self.max_speed} km/h'
                    f' este inmatriculata si circula cu viteza {self.vit_act} km/h')
            else:
                print(
                    f'Masina {self.marca}-{self.model} cu culoarea {self.color} are viteza maxima {self.max_speed} km/h'
                    f' este inmatriculata si este oprita')
        else:
            if self.vit_act > 0:
                print(
                    f'Masina {self.marca}-{self.model} cu culoarea {self.color} are viteza maxima {self.max_speed} km/h'
                    f' nu este inmatriculata si circula cu viteza {self.vit_act} km/h')
            else:
                print(
                    f'Masina {self.marca}-{self.model} cu culoarea {self.color} are viteza maxima {self.max_speed} km/h'
                    f' nu este inmatriculata si este oprita')

    def inmatriculare(self):
        self.inmat = True

    def vopseste(self, new_color):
        if new_color.lower() in self.culori_disponibile:
            self.color = new_color
        else:
            print(f'Nu avem vopsea in aceasta culoare, {new_color}, nu putem vopsi masina {self.marca}-{self.model}')

    def accelerate(self, new_speed):
        if new_speed > self.max_speed:
            print(f'Acest masina {self.marca}-{self.model} nu poate sa accelereze pana la {new_speed} km/h,'
                  f' pentru ca are viteza maxima {self.max_speed} km/h')
            self.vit_act = self.max_speed
        else:
            self.vit_act = new_speed

    def franeaza(self):
        self.vit_act = 0


s = Masina('Spring', 160)
d = Masina('Duster', 220)
l = Masina('Logan', 240)
j = Masina('Jogger', 220)
j2 = Masina('Jogger', 220)

s.vopseste('Rosu')
s.inmatriculare()
s.accelerate(50)
s.descrie()

print(' ')
d.vopseste('Verde')
d.inmatriculare()
d.accelerate(250)
d.descrie()

print(' ')
l.vopseste('Maro')
l.descrie()
l.vopseste('Turcoaz')
l.inmatriculare()
l.accelerate(90)
l.descrie()

print(' ')
j.vopseste('Argint')
j.accelerate(40)
j.descrie()
j.franeaza()
j.descrie()

print(' ')
j2.vopseste('Negru')
j2.inmatriculare()
j2.accelerate(50)
j2.accelerate(70)
j2.descrie()
