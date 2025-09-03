def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

print(list(even_numbers(10)))

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci(20)))
