def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


list_one = []
for i in range(1, 10):
    list_one.append(fib(i))
print(list_one)
