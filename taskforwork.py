import os

filename = ''
while filename == '':
    filename = input('Введите имя файла: ')
else:
    
    print("Имя введеого файла " + filename)

try:
    f= open(filename , 'r', encoding='utf-8')
    for line in f:
        print(line)
except FileNotFoundError:
     print('Файл с таким именем не найден, повторите снова.')



input()