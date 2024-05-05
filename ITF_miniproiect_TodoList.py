'''
TodoList
    Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

     Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizează_task(nume) - se va sterge din dict
afișează_todo_list() - doar cheile
afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
Dacă acesta răspunde nu - la revedere
Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
'''

class TodoList:
    todo = {}

    def add_task(self, name, details):
        self.todo[name] = details

    def final_task(self, name):
        self.todo.pop(name)

    def list_todo(self):
        print(f'Lista de taskuri: {list(self.todo.keys())}')

    def list_details(self, name):
        if name in self.todo.keys():
            print(self.todo[name])
        else:
            r = input(f'Nu exista acest task cu numele {name}, vrei sa adaugi? y/n: ')
            if r.lower() == 'y':
                new_details = input('Detaliaza task-ul: ')
                self.todo[name] = new_details
            else:
                print(f'Esti liber :)')

hetfo = TodoList()
hetfo.add_task('coffee', 'drink coffee with old classmate')
hetfo.add_task('mail','checking mails')
hetfo.add_task('christening', 'editing the christening ceremony of Mark')
hetfo.add_task('raport', 'designing the new variant of sustenability raport')
hetfo.add_task('bike', 'go to biking on the specific training route')

hetfo.list_todo()
print(' ')
hetfo.list_details('raport')
print(' ')
hetfo.final_task('mail')
print(' ')
hetfo.list_todo()
print(' ')
hetfo.list_details('meeting')
print(' ')
hetfo.list_todo()


