def text_CSS():
     
    print('Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S вставить строку S0.')

    while True:
        C = input('Введите строку C: ')
        S = input('Введите строку S: ')
        S0 = input('Введите строку S0: ')
        text=''

        try:
            for i in S:
                if C==i:
                    text= text+S0+i
                else:
                    text= text+i
                



        except ValueError:
             print('Ошибка')
             continue

        print(f'Преобразованный текст: {text}')
        break



text_CSS()