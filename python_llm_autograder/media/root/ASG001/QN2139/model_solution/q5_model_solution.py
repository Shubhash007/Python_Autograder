# Model Solution: Generating the First n Terms of the Fibonacci Sequence

# Prompt the user to enter the number of terms
n_terms = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

print("Fibonacci sequence:")

# Generate and print the Fibonacci sequence
for _ in range(n_terms):
    print(a)
    a, b = b, a + b



