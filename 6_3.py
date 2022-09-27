# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]


def step(n):
    numbers = [1, 2, 3, 4, 5, 6]
    for i in range(n):
        numbers.insert(0, numbers.pop())
    print(numbers)

step(2)