def fibonacci_n_terms(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence with {n} terms: {fibonacci_n_terms(n)}")