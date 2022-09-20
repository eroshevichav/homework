# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

numb1 = int(input())
math_operation = input()
numb2 = int(input())
if math_operation == '+':
    print(numb1 + numb2)
elif math_operation == '-':
    print(numb1 - numb2)
elif math_operation == '*':
    print(numb1 * numb2)
elif math_operation == '/':
    print(numb1 / numb2)
else:
    print('enter other math_operation ')

