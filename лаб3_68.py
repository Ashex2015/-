from random import randint
print('68.	Дан файл f, компоненты которого являются целыми числами. Получить в файле g все компоненты файла f: а) являющимися четными числами; б) делящиеся на 3 и не делящиеся на 7; в) являющимися точными квадратами.')
n = int(input ('Введите сколько чисел будет сгенерировано в файле: '))

f=''
a = []
b = []
c = []

with open('лаб3_68.txt', 'w', encoding='utf-8') as file:
    for i in range (n):
        file.write(str(randint(0,1000)) +'\n')



with open('лаб3_68.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    f= f+content

f = f.split('\n')
print(f)
try:
        for i in f:
            if i!='':
                if int(i)%2 == 0:
                     a.append(i)
                    
                elif int(i)%3==0 and int(i)%7!=0:
                    b.append(i)
                for n in range (1,int(i)):
                     if int(n)*int(n)==int(i):
                          c.append(i)
except:
        print('123')



with open('лаб3_68_G.txt', 'w', encoding='utf-8') as file:
     file.write('Четные числа:'+'\n')
     for i in a:
          if i != a[-1]:
               file.write(str(i)+', ')
          else:
               file.write(str(i))
     file.write('\n'+'делящиеся на 3 и не делящиеся на 7:'+'\n')
     for i in b:
          if i != b[-1]:
               file.write(str(i)+', ')
          else:
               file.write(str(i))
     file.write('\n'+'являющимися точными квадратами:'+'\n')
     for i in c:
          if i != c[-1]:
               file.write(str(i)+', ')
          else:
               file.write(str(i))



