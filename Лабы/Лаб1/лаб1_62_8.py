
def form ():
    print('.По заданной формуле члена ряда с номером k составить две программы:\n'
    'а) программу вычисления суммы первых n членов заданного ряда;\n '
    'б) программу вычисления всех членов ряда, не меньших заданного числа E.')


    while True:
        num = input('Выберете задание (а или б): ')

        if num == 'а':
            try:
                final = 0
                chislo = int(input('Введите целое число: '))

                for i in  range (1, chislo+1):
                    summa = (3*i-1)/(7*i**2+9)
                    final = summa+final
                print(f'Сумма первых {chislo} членов задоного ряда: {final}')

                break
            except ValueError:
                print('Число не является целым или введено не число!!')
                continue
            
        elif num == 'б':
            k=1
            try:
                final = []
                chislo = float(input('Введите число (например: 1.345): '))
                i=1
                while True:
                    summa = (3*i-1)/(7*i**2+9)
                    if summa >= chislo:
                        final.append(summa)
                    else:
                        break
                    i += 1
                for i in final:
                    print(f'Для E = {chislo}, найдены следующие члены ряда: k[{k}]={i}')
                    k += 1
                break
            except ValueError:
                print('Число не является дясятичным или введено не число!!')
                continue
        else:
            print("Нет такого задания!")