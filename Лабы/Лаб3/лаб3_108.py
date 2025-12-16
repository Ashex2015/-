print('108.	Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел делилась на 5 и при этом была максимально возможной. Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число – максимально возможную сумму, соответствующую условиям задачи.')

f=''
g=[]
with open('108_1.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    f = content+f

with open('108_2.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    j = content+f

def files(f):
    f = f.split('\n')

    for i in f:
        try:
            N=int(i)
        except ValueError:
                     i= i.split(' ')
                     g.append(i)

    sum = 0
    if 1 <=  N <= 10000: 
       # print(g)
        for i in g:
            min_num = min(i)
            max_num = max(i)

            sum = max(int(min_num), int(max_num))+sum
    num = 0
    max_sum = 0
    for i in g:
           #print(i)
            min_num = min(i)
            max_num = max(i)
            num = max(int(min_num), int(max_num))+sum
            sum = sum-int(num)
            num=min(int(min_num), int(max_num))+sum
            sum = sum+int(num)

            if sum%5==0:
                 
                 if max_sum<=sum:
                      max_sum=sum
                      
            else:
                num=int(min(i))
                sum = sum-num
                num= int(max(i))
                sum = sum+num
    return(max_sum)

print(f'Максимально возможное число в файле 108_1: {files(f)}')
print(f'Максимально возможное число в файле 108_2: {files(j)}')

