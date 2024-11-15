# Prompt the user for a 5-digit number
number = input("Enter a 5-digit number: ")

# Convert each character to an integer and sum them up
digit_sum = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]) + int(number[4])

# Print the result
print("{number[0]} + {number[1]} + {number[2]} + {number[3]} + {number[4]} = {digit_sum}")
