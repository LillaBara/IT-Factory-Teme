# 1. Clasa Angajat
#      Atribute: nume, prenume, salariu
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

import datetime

print('1. Clasa Angajat')
print(' ')


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul {self.prenume} {self.nume} are salariu de {self.salariu} ron')

    def nume_complet(self):
        nume_intreg = self.nume + ' ' + self.prenume
        print(f'Numele intreg: {nume_intreg}')
        return nume_intreg

    def salariu_lunar(self):
        salar_lunar = self.salariu
        return salar_lunar

    def salariu_anual(self):
        salar_anual = 12 * self.salariu
        print(f'Salarul anual este {salar_anual} Ron')
        return salar_anual

    def marire_salariu(self, marire):
        self.salariu = self.salariu + (marire * self.salariu / 100)
        print(f'Salarul sa marit pentru {self.nume} {self.prenume} cu {marire}%, si este {self.salariu} Ron')
        # return self.salariu


a1 = Angajat('Pop', 'Andrei', 3500)
a2 = Angajat('Sabau', 'Gabriella', 4000)

a1.descrie()
a1.nume_complet()
a1.salariu_lunar()
a1.salariu_anual()
a1.marire_salariu(12)
a1.descrie()
a2.descrie()

#  2. Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# schimbă_cantitatea(cantitate)
# schimbă_prețul(pret)
# schimbă_nume_produs(nume)
# generează_factura() - va printa tabelar dacă reușiți

print(' ')
print('2. Clasa Factura')
print(' ')


class Factura:
    seria = 'PYTH'

    def __init__(self, numar, nume_produs, cantitate, pret_bucata):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata

    def schimba_cantitatea(self, new_cantitate):
        self.cantitate = new_cantitate

    def schimba_pretul(self, new_pret):
        self.pret_bucata = new_pret

    def schimba_numele_produs(self, new_nume):
        self.nume_produs = new_nume

    def genereaza_factura(self):
        data_curenta = datetime.date.today()
        print(f'Factura {self.seria} numar {self.numar}')
        print('Data:', data_curenta)
        t = [
            ['Produs', 'Cantitate', 'Pret bucata', 'Total'],
            [self.nume_produs, self.cantitate, self.pret_bucata, self.cantitate * self.pret_bucata]
        ]
        for row in t:
            print('| {:10} | {:^10} | {:>12} | {:>10} |'.format(*row))


f1 = Factura(1, 'Telefon', 7, 700)
f2 = Factura(2, 'Tablet', 5, 1000)

f1.genereaza_factura()
print(' ')
f2.genereaza_factura()
