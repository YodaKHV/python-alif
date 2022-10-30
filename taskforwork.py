import os

#создание класса для продуктов
class Products:
 
    def __init__(self, name, price):
        self.name = name    # название 
        self.price = price  # цена


prdcts = list() #пустой список, в котором будут храниться объекты продуктов

#функция для добавления нового объекта продукта в список
def add_to_list(name, price):
    prdcts.append(Products(name,price))

# функция отображения объектов списка с порядковыми номерами 
def show_prdcts(productlist):
    i =0
    for obj in productlist:
        i +=1
        print(str(i) + '.', obj.name, obj.price)


#объявление переменной файла + цикл проверки на заполненность
filename = ''
while filename == '':
    filename = input('Введите имя файла: ')
else:
    
    print("Имя введеого файла " + filename)
#"пробуем" открыть файл
try:
    f= open(filename , 'r+', encoding='utf-8')
    
    for line in f: #считываем построчно файл
        line = line.replace('\n', '') #удаляем символ новой строки путем замены на пустое значение
        line = line.split(' — ') #делим значения по разделителю ' — '
        add_to_list(line[0],line[1]) # добавляем объект в список 
        


    #Выбираем действие для работы со списком
    action = ''
    while action != '6': #Цикл для работы со списком до тех пор пока не будет введено "6"
        print('\n1. Добавить продукт в список\n2. Изменить продукт в списке\n3.'+ 
        +'Удалить продукт из списка\n4. Расчитать общую сумму продуктов \n5. Посмотреть список продуктов\n6. Выйти')
        action = input("Выберите нужное действие: ")
        
        if action == '1': #Если вводим 1 "Добавить продукт в список"
            add_to_list(input('Введите название продукта: '),input('Введите цену: '))
        
        elif action == '2': #Если вводим 2 "Изменить продукт в списке"
            show_prdcts(prdcts)
            choicenum = int(input("Выберите порядковый номер позиции для изменения: "))
            choicenum -= 1
            prdcts[choicenum].name = input("Введите название: ")
            prdcts[choicenum].price = input("Введите цену: ")
    
        elif action == '3': #Если вводим 3 "Удалить продукт из списка"
            show_prdcts(prdcts)
            choicenum = int(input("Выберите порядковый номер позиции для удаления: "))
            choicenum -= 1
            prdcts.pop(choicenum)
        
        elif action == '4': #Если вводим 4 "Расчитать общую сумму продуктов"
            sum = 0
            for obj in prdcts:
                sum += int(obj.price)
            print('Сумма = ', str(sum))
        
        elif action == '5': #Если вводим 5 "Посмотреть список продуктов"
            show_prdcts(prdcts)

    f.seek(0,0) #возращаем курсор в начало списка
    for prdc in prdcts: #для каждого элемента списка формируем строку по формату исходной и записываем в файл
        rowtofile = str(prdc.name)+ ' — ' + str(prdc.price) + "\n"
        f.write(rowtofile)
    f.close() #закрываем файл


#исключение в случае, если файл не найден, программа завершается и выводит сообщение
except FileNotFoundError:
     print('Файл с таким именем не найден, повторите попытку.')

#input() #пустой инпут, для отладки