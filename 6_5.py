# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза


numb = [1, 2, 3, 4, 5]


def reverse_numb(numb, n=0):
    if len(numb) <= 1:
        return numb
    numb[n], numb[-n - 1] = numb[-n - 1], numb[n]
    if n + 1 != int(len(numb) / 2):
        return reverse_numb(numb, n + 1)
    return numb

print(reverse_numb(numb))





