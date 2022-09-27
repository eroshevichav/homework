# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

numbers = [1, 5, 4, 6, 9, 10, 3]

def sort_numb(numbers):
    numbers1 = list(filter(lambda x: x % 2 == 0, numbers))
    numbers2 = list(filter(lambda x: x % 2, numbers))
    print(numbers1 + numbers2)


sort_numb(numbers)