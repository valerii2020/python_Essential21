class Worker:
    name = ' '
    age = ' '
    day = 0
    def Work(self):
        pass
    def Holliday(self):
        pass
    def Day(self):
        worker.day = input('введите номер дня недели от 1 до 7 ')
        return worker.day

worker = Worker()
worker.name = input('введите имя рабочего  ')
worker.age = input('введите возраст рабочего  ')
worker.day = int(worker.day)
worker.Day()
if worker.day >= 7 or worker.day == 0:
    worker.Day()
else:
    print('non')
