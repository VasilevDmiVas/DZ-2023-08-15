while True:
    try:
        someString = input('Введите слова через запятую:\n ')
        if not ',' in someString:
            raise Exception('Слова введены не через запятую')
        someString1 = someString.split(',')
        someString2 = []
        print(f'Из строки: {someString} - удалены повторяющиеся слова')
        for index in someString1:
            if someString1.count(index) == 1:
                someString2.append(index)
        print(f"Результат: {', '.join(someString2)}")
        break
    except Exception as error:
        print(f'Ошибка {error}')
