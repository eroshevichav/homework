# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def binary_number_system(a):
    binary_numb = ''
    while a > 0:
        binary_numb = str(a % 2) + binary_numb
        a //= 2
    print(binary_numb)



binary_number_system(15)




