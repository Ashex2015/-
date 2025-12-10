def faban ():
        print( 'Вывести на экран все числа последовательности Фибоначчи,\n'
        ' не превышающие числа m.')

        while True:
            m = input ('Введите число:')
            try:
                m = int(m)
                break

            except ValueError:
                print('Введите число!!')
                continue



        f1, f2, = 0, 1
        while f1<=m:
                print (f1, end=' ')
                f1,f2=f2,f1+f2


faban()