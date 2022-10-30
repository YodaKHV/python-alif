import os

#создание класса для овощей
class Vegitable:
 
    def __init__(self, name, price):
        self.name = name    # название 
        self.price = price  # цена


vegtbls = list() #пустой список, в котором будут храниться объекты овощей


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
        vegtbls.append(Vegitable(line[0],line[1]))
        print(line)
        
except FileNotFoundError:
     print('Файл с таким именем не найден, повторите снова.')



input()