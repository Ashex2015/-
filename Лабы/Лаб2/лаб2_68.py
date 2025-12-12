def text_CSS():
     
    print(' Дана строка из заглавных латинских букв и точек. Определите максимальное \n'
            'количество идущих подряд символов, среди которых нет букв Y, а количество точек не \n'
            'превышает 5.')

    while True:
        text = input('Введите текст: ')
        k=0
        text_p = ''
        text_pp = ''
        lentext = 0
        try:
            for i in text:
                if 'Y'==i or 'y'==i:
                        if lentext == 0:
                            lentext= len(text_p)
                        elif len(text_p) > lentext:
                             text_pp=text_p
                             lentext = len(text_pp)
                        text_p = ''
                elif '.'==i:
                    k +=1
                    text_p=text_p+i
                    if k == 5:
                        text_p = ''
                    if lentext == 0:
                        lentext= len(text_p)
                        text_p = ''
                    elif 'Y'==i or 'y'==i:
                        if len(text_p) > lentext:
                             text_p = ''
                             k=0
                        text_p = ' '
                        k=0
                    elif len(text_p) > lentext:
                        text_p = ''
                        lentext = len(text_pp)
                        k=0
                else:
                    print(i)
                    text_p = text_p+i
                if len(text_p)>=lentext:
                    text_pp=text_p
                



        except ValueError:
             print('Ошибка')
             continue

        print(f'Преобразованный текст: {text_pp}')
        break



text_CSS()