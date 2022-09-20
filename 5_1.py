# Вывести первые N чисел кратные M и больше K

M = int(input())
K = int(input())
N = int(input())
for i in range(K + 1, K + M * N + 1, 1):
    if i % M == 0:
        print(i)








