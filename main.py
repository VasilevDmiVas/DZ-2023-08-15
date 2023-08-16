import os

somelists = []

while True:
    print('1 - Для записи в файл необходимо нажать единицу')
    print('2 - Для чтения из файла необходимо нажать двойку')
    print('3 - Для выхода из программы необходимо нажать три')

    option = input('Выберите действие из списка: ')

    if option == '1':
        with open('text.txt', 'w', encoding='utf-8') as textFile:
            newText = input('Введите текст для записи в файл: ')
            somelists.append(newText)
            textFile.writelines([i + '\n' for i in somelists])

    elif option == '2':
        with open('text.txt', 'r', encoding='utf-8') as textFile:
            textRead = textFile.readlines()
            somelists = [i.rstrip('\n') for i in textRead]
            print(f'Содержимое файла - {somelists}')

    elif option == '3':
        break

print('Вы вышли из программы \n До свидания')