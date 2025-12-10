def tabl():

    print('Напечатать числа в виде таблицы (запрашивать начальные значения перед\n'
          'построением: с какого числа начинать построение, количество строк и столбцов:')
    while True:
        a = input('Число для начало:')
        b = input('Введите количество строк: ')
        c = input('Введите количество столбцов: ')

        try:

            a,b,c = int(a), int(b), int(c)
            ff = ''
            sddd=[]
            for f in range (1, a+1):
                sddd.append(f)


            for i in range (b):
                sd=[]
                for j in range (c):
                    sd.append(a)
                    a= a+1
                for sdd in sd:
                   ff = str(sdd) + ' ' + ff
                formatted_row = '\t'.join([str(num) for num in sd])
                print(formatted_row)
            break
        except ValueError:
            print('Введено не число')


tabl()

