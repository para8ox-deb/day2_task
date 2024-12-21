def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n_terms = 10
print("Fibonacci series:")
for i in range(n_terms):
    print(fibonacci_recursive(i), end=" ")
print()
