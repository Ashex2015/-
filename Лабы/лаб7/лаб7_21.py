import re 


def password(passwd):

    if not re.fullmatch (r'[A-Za-z0-9^$%@#&*!?]+', passwd):
        return False
    

    if len(passwd) < 8:
        return False
    
    if  not re.search(r'[A-Z]', passwd):
        return False
    
    if  not re.search(r'[a-z]', passwd):
       return False
    
    if  not re.search(r'[0-9]', passwd):
        return False

    sc = set(re.findall(r'[^$%@#&*!?]', passwd))

    print(sc)
    if len(sc) < 2 :
        return False
    
    if re.search(r'(.)\1', passwd):
        return False
    
    return True


def rgb(pas):
    if pas[0]=='#':
        pas = pas.split('#')
        if len(pas[1]) == 6:
            return True
        if len(pas[1]) == 3:
            return True
    else:
        k=0
        for i in pas:
            if i == '(':
                k=1
        if k==1:
            pas = pas.split('(')
            if pas[0] == 'rgb':
                pas = pas[1].split(')')
                pas = pas[0].split(',')
                k=0
                for i in pas:
                    if int(i) <= 255:
                        k+=1
                if k==3:
                    return True
                else:
                    return False
            if pas[0] == 'hsl':
                k=0
                pas = pas[1].split(')')
                pas = pas[0].split(',')
                for i in pas:
                    try:
                        if int(i)<=360:
                            k+=1
                    except:
                        try:
                            if i[-1]=='%':
                                i = i.split('%')
                                int(i[0])
                                k+=1
                        except:
                            return False
                if k==3:
                    return True
                else:
                    return False
                
def date(date):

    
    date = date.strip()
    

    months = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12,
        
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12,
        
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 
        'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 
        'oct': 10, 'nov': 11, 'dec': 12
    }
    
    # Дни в месяцах
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Високосный ли год?
    def leap_year(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    
   
    def check_one(day_str, month_str, year_str):
        try:
    
            year = int(year_str)
            if year < 0 or year > 9999:
                return False
            
    
            if month_str.isdigit():
                month = int(month_str)
            else:
                month = months.get(month_str.lower(), 0)
            
            if month < 1 or month > 12:
                return False
            
    
            day = int(day_str)
            
            
            days_in_month = month_days[month - 1]
            if month == 2 and leap_year(year):
                days_in_month = 29
            
            return 1 <= day <= days_in_month
            
        except:
            return False
    
    
    for sep in ['.', '/', '-']:
        if sep in date:
            parts = date.split(sep)
            if len(parts) == 3:
                
                if check_one(parts[0], parts[1], parts[2]):
                    return True
                
                if check_one(parts[2], parts[1], parts[0]):
                    return True
    
    
    parts = date.replace(',', ' ').split()
    
    if len(parts) == 3:
       
        if parts[0].isdigit() and parts[2].isdigit():
            if check_one(parts[0], parts[1], parts[2]):
                return True
        
        
        if parts[1].replace(',', '').isdigit() and parts[2].isdigit():
            if check_one(parts[1].replace(',', ''), parts[0], parts[2]):
                return True
        
        
        if parts[0].replace(',', '').isdigit() and parts[2].isdigit():
            if check_one(parts[2], parts[1], parts[0].replace(',', '')):
                return True
    
    return False




while True:
    s = int(input('Введите что хотите проверить: \n'
    '1. Формат даты\n' 
    '2. Цвета\n' 
    '3. Пароль\n' \
    'Введите число: '))

    if s == 1:
        s = input('Введите дату: ')
        if date(s)==True:
            print('Формат верный')
            break
        else:
            print('Формат не верный')
            break
    if s == 2:
        s = input('Введите код цевета(hex, rgb,  hsl): ')
        if date(s)==True:
            print('Формат верный')
            break
        else:
            print('Формат не верный')
            break
    if s == 3:
        s = input('Введите пароль: ')
        if date(s)==True:
            print('Пароль прошел проверку')
            break
        else:
            print('Пароль не прошел проверку')
            break
    