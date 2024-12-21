def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


n_terms = 10
print("Fibonacci series:")
print(" ".join(map(str, fibonacci_iterative(n_terms))))
