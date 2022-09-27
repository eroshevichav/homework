# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

def type_of_date():
    text = [1, 'hello', ['hi'], ]
    text1 = list(filter(lambda x: isinstance(x, str), text))
    print(text1)

type_of_date()