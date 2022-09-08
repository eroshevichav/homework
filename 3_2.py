# Пользователь вводит 3 числа, найти среднее арифмитическое с точностью 3
number1 = float(input())
number2 = float(input())
number3 = float(input())
total = round((number1 + number2 + number3)/3, 3)
print(total)
