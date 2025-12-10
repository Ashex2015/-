def proverka(j):
        if j.find(';') > 0:
            return(True)
        else:
          print('Неверный формат')
          ygolnik() 
          return(False)
def ygolnik():
    while True:
        print('Выпуклый четырехугольник задан координатами своих вершин. \n'
        'Найти площадь  этого четырехугольника как сумму площадей треугольников.') 
        a = input('Введите первую вершину четерехугольника (пример ввода x1;y1): ')
        if not proverka(a):
             exit()
        b = input('Введите adaвторую вершину четерехугольника (пример ввода x2;y2): ')
        if not proverka(b):
             exit()
        c = input('Введите третию вершину четерехугольника (пример ввода x3;y3): ')
        if not proverka(c):
             exit()
        d = input('Введите четвертую вершину четерехугольника (пример ввода x4;y4): ')
        if not proverka(d):
             exit()


        x1,y1 = a.split(';')
        x2,y2 = b.split(';')
        x3,y3 = c.split(';')
        x4,y4 = d.split(';')

        try:

             x1, y1 = float(x1), float(y1)
             x2, y2 = float(x2), float(y2)
             x3, y3 = float(x3), float(y3)
             x4, y4 = float(x4), float(y4)
             break
        except:
             print("Не число")
             continue
    
    S = abs(((x1 - x2)*(y1 + y2) + (x2 - x3)*(y2 + y3) + (x3 - x4)*(y3 + y4) + (x4 - x1)*(y4 + y1)) / 2)
    

    print (f'Площадь четырехугольника: {S}')
