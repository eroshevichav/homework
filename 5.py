# угадай число.вводится число х, которое необходимо угадать,пользователь вводит предположение
# вывести с какой попытки польз-ль угадал

from random import randint
x = randint(1, 10)
print(x)
y = int(input())
n = 1
while y != x:
    n +=1
    y = int(input())
    if y > x:
        print('укажи меньше')
print(n)
