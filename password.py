# Basic Password Generator

# module import
import random

# ASCII Table Decimal to Characters
lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))

# initialize empty password
password = "" # Empty String
options = lowercase.copy() # We assume that our passwords will always have at least lowercase characters

# input
# Requirement 1: Set Password Length
size = int(input("Enter the size of the password: "))

# Requirement 2: Set Password Criteria
has_upper = input("Include uppercase letters? (Y/N): ")
has_digit = input("Include numbers? (Y/N): ")
has_special = input("Include special characters? (Y/N): ")

# processing
# Step 1: Add in the respective options
if has_upper in {'Y', 'y'}:
    options.extend(uppercase)

if has_digit in {'Y', 'y'}:
    options.extend(digits)

if has_special in {'Y', 'y'}:
    options.extend(special)

# Step 2:
# Until the password variable meets the desired length, randomly add in
# characters from the our list of options
while len(password) < size:
    random_char = chr(random.choice(options))
    password += random_char

# Requirement 3: Output the generated password
print(f"The randomly generated password is: {password}")