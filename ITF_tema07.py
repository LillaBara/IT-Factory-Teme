import random
numar_secret = random.randint(1,5)
print(numar_secret)
while numar_secret == numar_secret:
   numar_ghicit = int(input('Introduceti un numar: '))
   if numar_ghicit < numar_secret:
       print('Nr secret este mai mare')
   elif numar_ghicit > numar_secret:
       print('Nr. secret este mai mic')
   else:
       print('Ai ghicit!')
       break


