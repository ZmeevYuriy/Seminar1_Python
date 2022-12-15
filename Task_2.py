# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите 3-х значное число :'))
a = int(100)
b = (1000)
if a < number and number < b:
    d1 = number % 10
    number = number // 10
    d2 = number % 10
    number = number // 10
 
    print("Сумма цифр числа:", number + d1 + d2)
else:
    print('error')
 