def chisla():
     
    print('.Сформировать и вывести на экран в порядке возрастания все числа из четырехn\n'
    'цифр, причем внутри числа не должно быть двух одинаковых цифр. Например,\n'
    'такими числами являются 123(0123), 2715 и т.д. Число 24 таким не является (24 =0024).')

    while True:
        f = input('Введите числа (формате: 1234, 4565, 2345....): ')

        try:
            f= f.replace(' ','')
            f= f.split(',')
        except ValueError:
             print('Не верный формат введиние числел')
             continue
        try:
            for i in f:
                i = int(i)
                if 4!=len(str(i)):
                     raise ValueError ('Введено число меньше или больше 41 значного или буквы')
                     continue
        except ValueError:
             print ('Введено число меньше или больше 4 значного или буквы')
             continue

            
        j=0
        gh= []
        h=0
        for g in range (len(f)):
                for j in f[g]:
                    for k in f[g]:

                        if k==j and j != '0' and j!= '' and k!='' and k!=0:
                            
                            h+=1                        
                if h<=4:
                    gh.append(f[g])
                h=0    
        if len(gh)==0:
            # break
             pass
        else:
            gh.sort()
            print ('Числа в порядке возростания:')
            for i in gh:
                print (i)
            break



chisla()