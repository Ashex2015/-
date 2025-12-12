
f = ''
g=''
ff=''
gg=''

with open('108_1.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    f= f+content

with open('108_2.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    ff= ff+content

f = f.split('\n')
for i in f:
    g= str(i)+' '+g

g = g.split(' ')
f=[]
for i in g:
    if bool(i)== True:
        f.insert(0, i)

ff = ff.split('\n')
for i in ff:
    gg= str(i)+' '+gg
gg =gg.split(' ')
ff=[]
for i in gg:
    if bool(i)== True:
        ff.insert(0, i)

def proverka(index):

    if index < 0 or index >= len(f):
         return "Указанный индекс вне диапазона"
    if f[index] in ff:
        return f'Элемент {f[index]} присутствует во втором списке'
    else:
        return f'Элемент {f[index]} отсутствует во втором списке'

index = int(input('Введите интекс: '))
print(proverka(index))
