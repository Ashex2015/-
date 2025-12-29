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


def variable (num):
  num= num.strip()
  variable1= [r"(^\D)",
             r'(?!pi|e|ln2|ln10|sqrt2|sin)\b\w*\b\s*\b'
             ]
  for patter in variable1:
     match = re.findall(patter,num)
     matchh=''
     for i in match:
         matchh +=i
     if len(match)> 0 and len(num)==len(matchh):
       k=True
     else:
        k=False
  return k



def number(num):
    
  number1= [r"([+*/-])"]
  fun = ''
  num= num.strip()

  for patter in number1:
      match = re.findall(patter,num)
      if len(match) == 0:
          fun=True
      else:
        if match[0] == '-' or match[0]=='+':
            fun = False
        else:
            fun = True
  if fun == True:
      number1= [r"([0-9])"]
      for patter in number1:
          match = re.findall(patter, num)
  else:
      fun=False
  return fun



def operator(num):
    
  num= num.strip()
  operator1= [r'[\\^*/+-]'
             ]

  for patter in operator1:
      match = re.findall(patter,num)
      if len(match) != 0 :
          return True
      else:
         return False



def right_parenthesis (num):
  num= num.strip()
  right_parenthesis1= [r'\(',
             ]

  for patter in right_parenthesis1:
      match = re.findall(patter,num)
      if len(match) != 0 :
          return True
      else:
         return False

def left_parenthesis(num):
   
  num= num.strip()
  left_parenthesis1= [r'\)',
             ]

  for patter in left_parenthesis1:
      match = re.findall(patter,num)
      if len(match) != 0 :
          return True
      else:
         return False
def function (num):
  num= num.strip()
  function1= [
             r'(sin|cos|tg|ctg|tan|cot|sinh|cosh|th|cth|tanh|coth|ln|lg|log|exp|sqrt|cbrt|abs|sign)']
  for patter in function1:
     match = re.findall(patter,num)
     if len(match)!= 0:
       k=True
     else:
        k=False
  return k



def constant (num):
  num= num.strip()
  function1= [
             r'(pi|e|sqrt2|ln2|ln10)']
  for patter in function1:
     match = re.findall(patter,num)
     if len(match)!= 0:
       k=True
     else:
        k=False
  return k



while True:
    s = int(input('Введите что хотите проверить: \n'
    '1. Формат даты\n' 
    '2. Цвета\n' 
    '3. Пароль\n' \
    '4. Токенизация математического выражения\n'\
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
    if s == 4:

        num = input('Введите токен: ')
        if operator(num) == True:
           print(r'Type: operator')
        if variable(num) == True:
           print(r'Type: variable')
        if number(num) == True:
           print(r'Type: number')
        if left_parenthesis(num) == True:
           print(r'Type: left_parenthesis')
        if right_parenthesis(num) == True:
           print(r'Type: right_parenthesis')
        if function(num) == True:
           print(r'Type: function ')
        if constant(num) == True:
           print(r'Type: constant ')
    