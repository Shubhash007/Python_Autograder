# Define the weights for the calculation
weights = [2, 7, 6, 5, 4, 3, 2]

# Define the checksum letters for 'S' and 'F'
checksum_letters_s_f = ['J','Z','I','H','G','F','E','D','C','B','A']

# Define the checksum letters for 'T' and 'G'
checksum_letters_t_g = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H']

# Get input from the user
nric_input = input("Enter the first 7 characters of your NRIC/FIN: ").strip().upper()

# Extract the first character to determine the category
first_char = nric_input[0]

# Extract the digits from the NRIC as integers (without using map)
digits = []
for char in nric_input[1:]:
    digits.append(int(char))

# Calculate the weighted sum
weighted_sum = 0
for i in range(7):
    weighted_sum += weights[i] * digits[i]

# Adjust the sum based on the first character
if first_char == 'T' or first_char == 'G':
    weighted_sum += 4

# Find the checksum index using modulo 11
checksum_index = weighted_sum % 11

# Determine the last alphabet based on the first character
if first_char == 'S' or first_char == 'F':
    checksum_letter = checksum_letters_s_f[checksum_index]
elif first_char == 'T' or first_char == 'G':
    checksum_letter = checksum_letters_t_g[checksum_index]
else:
    print("Invalid NRIC/FIN format.")
    checksum_letter = ""

# Print the full NRIC/FIN
if checksum_letter:
    full_nric = nric_input + checksum_letter
    print("Your complete NRIC/FIN is: ", full_nric)
