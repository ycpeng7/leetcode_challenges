def fibonacci(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(4) == 3
print(fibonacci(100))