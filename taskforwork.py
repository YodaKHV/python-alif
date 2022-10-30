import os

#создание класса для овощей
class Vegitable:
 
    def __init__(self, name, price):
        self.name = name    # название 
        self.price = price  # цена


vegtbls = list() #пустой список, в котором будут храниться объекты овощей

def add_to_list(name, price):
    vegtbls.append(Vegitable(name,price))

def show_vegtbls(veglist):
    i =0
    for obj in veglist:
        i +=1
        print(str(i) + '.', obj.name, obj.price)



filename = ''
while filename == '':
    filename = input('Введите имя файла: ')
else:
    
    print("Имя введеого файла " + filename)

try:
    f= open(filename , 'r', encoding='utf-8')
    #veg = 0
    for line in f:
        #veg += 1
        
        line = line.replace('\n', '')
        line = line.split(' — ')
        add_to_list(line[0],line[1])
        



    action = ''
    while action != '6':
        print('\n1. Добавить в список\n2. Изменить запись в списке\n3. Удалить из списка\n4. Вычесть общую сумму\n5. Посмотреть список\n6.Выйти')
        action = input("Выберете нужное действие: ")
        if action == '1':
            add_to_list(input('Введите название овоща: '),input('Введите цену: '))
        
        elif action == '2':
            show_vegtbls(vegtbls)
            choicenum = int(input("Выбери порядковый номер позиции для изменения: "))
            choicenum -= 1
            vegtbls[choicenum].name = input("введите название: ")
            vegtbls[choicenum].price = input("введите цену: ")
    
        elif action == '3':
            show_vegtbls(vegtbls)
            choicenum = int(input("Выбери порядковый номер позиции для удаления: "))
            choicenum -= 1
            vegtbls.pop(choicenum)
        
        elif action == '4':
            sum = 0
            for obj in vegtbls:
                sum += int(obj.price)
            print('Сумма = ', str(sum))
        
        elif action == '5':
            show_vegtbls(vegtbls)

except FileNotFoundError:
     print('Файл с таким именем не найден, повторите снова.')

input()