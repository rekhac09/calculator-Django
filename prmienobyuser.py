def generate_primes_up_to_n():
    n = int(input("Enter a number: "))  # User input
    primes = []  # List to store prime numbers
    for num in range(2, n + 1):  # Iterate from 2 to n
        is_prime = True  # Assume the number is prime
        for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of num
            if num % i == 0:  # If divisible, it's not prime
                is_prime = False
                break
        if is_prime:
            primes.append(num)  # Add prime number to the list
    return primes

# Example usage
prime_numbers = generate_primes_up_to_n()
print("Prime numbers:", prime_numbers)
