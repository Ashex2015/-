print('Подсчитать общее количество цифр и знаков «+», «-», и «*», входящих в строку s.')


def pot():
    k=0
    while True:
        try:

            s = input('Введите цифры и знаки ')
            s= s.replace(' ','')
            for i in s:
                if i == '1' or i== '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0' or i == '+' or i == '-' or i == '*':
                    k =  k+1
            print(f'Общее количество цифр и знаков: {k}')
            break


        except ValueError:
            print('Ошибка')
            break

pot()