# спрашивать у пользователя данные пока он не ведет число

numb = input()
while not numb.isdigit():
    numb = input('repeat')
    