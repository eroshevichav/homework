# Вводится строка, вывести из строки только цифры

text = input()
for i in range(len(text)):
    if text[i].isdigit():
        print(text[i])




