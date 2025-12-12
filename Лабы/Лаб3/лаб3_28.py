
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
final = []
def proverka():
    for i in f:
        for h in ff:
            if i==h:
                final.append(i)
    return final
final = list(set(proverka()))
print('Элементы встречаются в списке: ')
for i in final:
    print(i)