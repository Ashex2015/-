def probel():
     
    print('Написать программу, которая удаляет в данном тексте все лишние пробелы.')

    while True:
        f = input('Введите текст: ')
        

        try:
            f = f.split(' ')
            text=''
            k=0
            for i in f:
                if k == 0 and i != '':
                      text = text + i
                      k +=1 
                if i != '' and k==1:
                    text = text + ' ' + i 
        except ValueError:
             print('Ошибка')
             continue

        print(f'Текст без лишних пробелов: {text}')
        break


