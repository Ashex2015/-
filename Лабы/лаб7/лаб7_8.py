print('Написать регулярное выражение, определяющее является ли данная строчка\n'
'валидным е-mail адресом. Примеры правильных выражений: user@example.com,\n'
'root@localhost. Примеры неправильных выражений: bug@@@com.ru, @val.ru, Just Text2.')






def email(mail):
    k=0
    
    if mail.count('@') != 1:
        return False

    domen = mail.split('@')

    if '.' == domen[0][0]:
        return False
    


    if len(domen[1]) <= 2:
        return False

    tl = domen[1]
    tl = tl.split('.')[-1]

    if len(tl) < 2:
        return False
    
    return True


mail = input ("Проверка email: ")
s = email(mail)
print(f'Email: {s}')