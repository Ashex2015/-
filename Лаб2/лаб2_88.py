
     
print('Дана строка, содержащая заглавные латинские буквы и телефонные номера.Телефонный номер – это последовательность цифр, расположенных между буквами. Внекоторой стране Z номер телефона состоит из 11 цифр, начинается на 7 и при этомсумма последних двух цифр номера равна сумме первых двух цифр. Определитеколичество телефонных номеров страны Z, содержащихся в строке. мне нужен только примеры ввывод и вводов')

def is_valid_number(number):
    if len(number) != 11 or not number.isdigit() or number[0] != '7':
        return False
    sum_first_two = int(number[0]) + int(number[1])
    sum_last_two = int(number[-2]) + int(number[-1])
    return sum_first_two == sum_last_two

def count_valid_numbers(input_text):
    n = len(input_text)
    valid_count = 0
    i = 0
    
    while i < n - 10:
        if input_text[i].isdigit() and input_text[i] == '7':
            possible_number = input_text[i:i+11]
            if is_valid_number(possible_number):
                valid_count += 1
                i += 11
            else:
                i += 1
        else:
            i += 1
    
    return valid_count


while True:
    user_input = input('Введите текст: ')
    if user_input.strip():
        result = count_valid_numbers(user_input)
        print(f'Количество валидных номеров: {result}')
        break
    else:
        print('Ошибка: введен пустой текст.')