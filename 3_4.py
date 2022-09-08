# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
number1 = int(input())
number2 = int(input())
number3 = int(input())
total1 = (number1 > 0) + (number2 > 0) + (number3 > 0) # колич-во положит-х
total2 = 3 - total1  # максимум 3, значит отрицательных= всего - кол-во положит-х
print(total1, total2)



