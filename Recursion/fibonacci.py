def fibonacci(n):
    assert n>=0 and int(n)==n, 'Fibonacci number must be positive integer number.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))