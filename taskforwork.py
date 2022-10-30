import os

#создание класса для продуктов
class Products:
 
    def __init__(self, name, price):
        self.name = name    # название 
        self.price = price  # цена


prdcts = list() #пустой список, в котором будут храниться объекты овощей

def add_to_list(name, price):
    prdcts.append(Products(name,price))

def show_prdcts(productlist):
    i =0
    for obj in productlist:
        i +=1
        print(str(i) + '.', obj.name, obj.price)



filename = ''
while filename == '':
    filename = input('Введите имя файла: ')
else:
    
    print("Имя введеого файла " + filename)

try:
    f= open(filename , 'r+', encoding='utf-8')
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
            add_to_list(input('Введите название продукта: '),input('Введите цену: '))
        
        elif action == '2':
            show_prdcts(prdcts)
            choicenum = int(input("Выбери порядковый номер позиции для изменения: "))
            choicenum -= 1
            prdcts[choicenum].name = input("введите название: ")
            prdcts[choicenum].price = input("введите цену: ")
    
        elif action == '3':
            show_prdcts(prdcts)
            choicenum = int(input("Выбери порядковый номер позиции для удаления: "))
            choicenum -= 1
            prdcts.pop(choicenum)
        
        elif action == '4':
            sum = 0
            for obj in prdcts:
                sum += int(obj.price)
            print('Сумма = ', str(sum))
        
        elif action == '5':
            show_prdcts(prdcts)


    for vegi in prdcts:
        f.write(vegi.name, ' — ',vegi.price)
    f.close()


except FileNotFoundError:
     print('Файл с таким именем не найден, повторите снова.')

input()