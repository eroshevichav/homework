# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def from_binary_system(b):
    b = str()
    b1 = b[::-1] # развернули двоичное число
    number = 0
    for i in range(len(b1)):
        c = int((b1[i]) * 2 ** i) # каждую цифру надо умножить на 2 в степени ее индекса
        number += c
        print(number)


from_binary_system(11011)