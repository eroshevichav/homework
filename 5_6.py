# Вводится число, посчитать факториал этого числа

A = int(input())
factorial = 1
for i in range(2, A+1):
    factorial *= i
print(factorial)

