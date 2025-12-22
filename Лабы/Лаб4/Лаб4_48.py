import random

print('В анкетных данных обозначены фамилия, пол, рост. Определите средний рост \n '
'женщин, фамилию самого высокого мужчины, есть ли в группе хотя бы два человека \n'
'одного роста. \n')
M = ['Андрей','Иван', 'Антон', 'Михаил']
G = ['Анна', 'Вика', 'Алена','Наталья']
j = ["G","M"]
k = int(input('Введите количество анкет: '))
g=0
rost = []
rost_all = []
max_rost = -1
user = ''
for i in range(k):
    f = j[random.randint(0,1)]
    if 'G' == f:
        pol = 'Ж'
        rostt = int(random.randint(70,200))
        name = G[random.randint(0,3)]
    if 'M' == f:
        pol = 'М'
        rostt = int(random.randint(70,200))
        name = M[random.randint(0,3)]
    if pol == 'Ж':
        rost.append(rostt)
    if pol == 'М':
        if rostt > max_rost:
            max_rost = rostt
            user = name
    print (f'Анкета № {i+1}')
    print(f'Имя: {name}')
    print(f'Пол: {pol}')
    print(f'Рост: {rostt}')

if len(rost)== 0:
    pass
else: 
    g = sum(rost)/ len(rost)
print('-'*80)
if g == 0:
    pass
else:
    print(f'Средний рост женщин: {g}')
if user=='':
    pass
else:
    print(f'Самый высокий мужчина: {user}')
if len(rost_all) != len(set(rost_all)):
    print('Есть в группе два человека одного роста')
else:
    print('Нету два человека одного роста')


