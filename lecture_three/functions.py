def sum_numbers(n, greeting="Hello"):
    print(greeting)
    sum_el = 0
    for i in range(1, n + 1):
        sum_el += i
    return sum_el


a = sum_numbers(5, "By")
print(a)


def sum_str(*args):  # Передача неограниченного кол-ва аргументов
    res = ' '
    for i in args:
        res += i
    return res


print((sum_str('q', 'e', 'l')))
