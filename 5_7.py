# Вводится число N, вывести первые N чисел последовательности Фибоначи

N = int(input())
numb1 = numb2 = 1
a = 2
while a < N:
    numb1, numb2 = numb2, numb1 + numb2  # этот вариант подсмотрела
    # numb1 = numb2
    # numb2 = numb1 + numb2 - почему не срабатывает этот вариант?
    a += 1
print(numb2)






