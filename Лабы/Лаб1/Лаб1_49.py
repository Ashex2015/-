
def drobi():
    print('Написать программу сложения (вычитания) двух данных рациональных чисел.\n'
          'Ответ должен быть несократимой дробью.')
    while True:
        a = input ('Введите первое рациональное число (например a/b): ')
        b = input ('Введите второе рациональное число (например a/b): ')

        try:
            a1, a2 = a.split('/')
            b1, b2 = b.split('/') 

            a1, a2, b1,b2 = int(a1), int(a2), int(b1), int(b2)
            break
        except ValueError:
            print('Ошибка: введено не число')
            continue
    zam = a2 * b2
    new_a = a1 * b2
    new_b = b1 * a2

    while True:
        f = input ("Выберите операцию (+ или -): ")
        if f == '-':
            sum = new_a - new_b
            break
        elif f== '+':
            sum = new_a + new_b
            break
        else:
            print("Нет такой операции!")


    

    drob = 1
    print(min(sum,zam))
    for i in range(min(sum, zam), 1, -1):

        if sum % i == 0 and zam % i == 0:
            drob = i
            break


    final_ches = sum // drob
    final_zam = zam // drob


    print(final_ches, "/", final_zam) 



drobi()