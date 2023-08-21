# Calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate the modular inverse of 'a' modulo 'm'
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Example usage
plaintext = "Hello, World!"
a = 5
b = 8
plaintext = input("Enter a plain text:")
key = input("Enter keyword:")
x = []  # List to store the alphabet
k = []  # List to store the characters in the keyword
c = []  # List to store the remaining characters

# Populate the alphabet list 'x' with uppercase letters from A to Z
for i in range(65, 91):
    y = chr(i)
    x.append(y)

# Store the characters from the keyword in the list 'k'
for i in range(len(key)):
    char = key[i]
    k.append(char)

# Populate the list 'c' with characters not present in the keyword
for i in range(len(x)):
    if x[i] not in k:
        char = x[i]
        c.extend(char)

# Print the three lists for visualization
print("Alphabet:", x)
print("Keyword characters:", k)
print("Remaining characters:", c)

# Calculate the modular inverse of 'a' modulo 26
mod_inv = mod_inverse(a, 26)
if mod_inv is None:
    print("Error: 'a' value is not valid (no modular inverse exists)")
else:
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((a * (ord(char) - shift) + b) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    print("Encrypted:", encrypted_text)

    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((mod_inv * ((ord(char) - shift) - b)) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    print("Decrypted:", decrypted_text)
