# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name = input()
age = int(input())
country = input()
print('Hello! My name is %s.I am %d years old. I am from %s.' % (name, age, country))