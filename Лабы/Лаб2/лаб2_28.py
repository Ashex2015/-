def text_simvol():
     
    print('Дан текст. Если первый символ текста не является малой латинской буквой,\n'
           'тооставить его без изменения. Если же это малая латинская буква,\n'
           'но за начальной группоймалых латинских букв не следует цифра, \n'
           'то также оставить текст без изменения. Иначекаждую цифру, \n'
           'принадлежащую группе цифр, следующей за начальной группой малыхлатинских букв, \n'
           'заменить символом «*».')

    while True:
        f = input('Введите текст: ')
        text=''

        try:
            if (f[0].islower()) == True:
                for i in f:
                    if '1' == i:
                        text = text + '*'
                    elif '2' == i:
                        text = text + '*'
                    elif '3' == i:
                        text = text + '*'
                    elif '4' == i:
                        text = text + '*'
                    elif '5' == i:
                        text = text + '*'
                    elif '6' == i:
                        text = text + '*'
                    elif '7' == i:
                        text = text + '*'
                    elif '8' == i:
                        text = text + '*'
                    elif '9' == i:
                        text = text + '*'
                    elif '0' == i:
                        text = text + '*'
                    else:
                        text= text + i
            else:
                text = f



        except ValueError:
             print('Ошибка')
             continue

        print(f'Преобразованный текст: {text}')
        break



text_simvol()