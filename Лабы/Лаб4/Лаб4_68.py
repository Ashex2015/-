def int_to_roman(num):
    if not 0 < num < 4000:
        return "Число должно быть от 1 до 3999"
    
    t = ["", "M", "MM", "MMM"]
    h = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tt = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    on = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    

    f = t[num // 1000] + h[(num % 1000) // 100] + tt[(num % 100) // 10] + on[num % 10]
    return f

try:
    number = int(input("Введите число от 1 до 3999: "))
    roman = int_to_roman(number)
    print(f"{number} = {roman}")
except ValueError:
    print("Ошибка: введите целое число")