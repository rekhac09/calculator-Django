def fibonacci_series(n):
    """Generate Fibonacci series up to n terms."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Input from user
num_terms = int(input("Enter the number of terms: "))

# Validate input
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    print(fibonacci_series(num_terms))
