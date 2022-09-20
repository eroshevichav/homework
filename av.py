# вводится строка,вывести уникальные символы в строке
text = input()
for i in text:
    if text.count(i) == 1:
        print(i)

