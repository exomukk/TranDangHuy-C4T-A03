def fibonacci(n):
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("so thu 10 trong day fibonacci: ")
x = fibonacci(6)
print(x)