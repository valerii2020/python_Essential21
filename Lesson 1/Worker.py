class Worker:
    name = ' '
    age = ' '
    day = 0
    def Work(self):
        print('рабочий день')
    def Holliday(self):
        print('выходной день')


worker = Worker()
worker.name = input('введите имя рабочего  ')
worker.age = input('введите возраст рабочего  ')
worker.day = int(worker.day)

while worker.day > 7 or worker.day == 0:
    worker.day = int(input('введите номер дня недели от 1 до 7 '))

if worker.day <= 5:
    worker.Work()
    print('рабочий', worker.name, 'идет на работу')
else:
    worker.Holliday()





