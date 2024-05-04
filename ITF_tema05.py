"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișează a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișează ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișează ‘mai ai z schimbări’
"""
echipa_fotbal = ['Andrei', 'Botond', 'Cosmin', 'Daniel', 'Ervin']
schimbari_efectuate = int(input('Cate schimburi efectuate au fost: '))
jucator = input('Introdu numele jucatorului: ')
jucator = jucator.capitalize()
schimbari_max = 3

if schimbari_efectuate < schimbari_max:
    if jucator in echipa_fotbal:
        jucator_nou = input('Se efectueaza schimbarea, noul jucator: ')
        jucator_nou = jucator_nou.capitalize()
        echipa_fotbal.remove(jucator)
        echipa_fotbal.append(jucator_nou)
        schimbari_efectuate += 1
        print(f'Aceasta a fost a {schimbari_efectuate} schimbare')
        print(f'A intrat {jucator_nou} in locul lui {jucator}, si mai ai {schimbari_max-schimbari_efectuate} schimbari')
    else:
        print(f'Nu se poate efectua schimbare deoarece {jucator} nu este in teren')
        print(f'Mai ai {schimbari_max-schimbari_efectuate} schimbari disponibile')
else:
    print(f'Ai epuizat schimbarile, nu poti sa efectuezi schimbarea')

# cu functia while
echipa_fotbal = ['Andrei', 'Botond', 'Cosmin', 'Daniel', 'Ervin']
schimbari_efectuate = int(input('Cate schimburi efectuate au fost: '))
schimbari_max = 3
dif_schimbari = schimbari_max - schimbari_efectuate
while dif_schimbari > 0:
    jucator = input('Introdu numele jucatorului: ')
    jucator = jucator.capitalize()
    if jucator in echipa_fotbal:
        jucator_nou = input('Se efectueaza schimbarea, noul jucator: ')
        jucator_nou = jucator_nou.capitalize()
        echipa_fotbal.remove(jucator)
        echipa_fotbal.append(jucator_nou)
        # schimbari_efectuate += 1
        # print(f'Aceasta a fost a {schimbari_efectuate} schimbare')
        dif_schimbari = dif_schimbari - 1
        print(f'A intrat {jucator_nou} in locul lui {jucator}, si mai ai {dif_schimbari} schimbari')
        print('Jucatorii pe teren sunt:', echipa_fotbal)
    else:
        print(f'Nu se poate efectua schimbare deoarece {jucator} nu este in teren')
        print(f'Mai ai {dif_schimbari} schimbari disponibile')
print(f'Ai epuizat schimbarile')

'''
# dat de prof

lista_jucatori = ["jucator_1", "jucator_2", "jucator_3", "jucator_4", "jucator_5", "jucator_6",]
schimbari_efectute = 2
schimbari_maxime = 3

schimb = input("Vrei sa faci o schimbare? (y/n)")

if schimb == "y":
    jucator_scos = input("Introdu jucatorul pe care vrei sa il scoti: ")
    if jucator_scos not in lista_jucatori:
        print(f"Nu se poate efectua schimbarea. Jucatorul {jucator_scos} nu exista in teren \n"
              f"Mai ai {schimbari_maxime - schimbari_efectute} schimbari")
    else:
        lista_jucatori.remove(jucator_scos)
        jucator_adaugat = input("Introdu jucatorul pe care vrei sa il adaugi: ")
        lista_jucatori.extend(jucator_adaugat)
        print(f"A iesit jucatorul {jucator_scos} si a intrat {jucator_adaugat} \n"
              f"Mai ai {schimbari_maxime - schimbari_efectute} schimbari")

'''



