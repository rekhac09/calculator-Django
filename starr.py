def star_pyramid(n):
    """Print a star pyramid with n rows."""
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(" " * (n - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Input from user
rows = int(input("Enter the number of rows for the pyramid: "))
star_pyramid(rows)
