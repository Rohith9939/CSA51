# Calculate the greatest common divisor (GCD) of two numbers
a = 3  #For example, you could choose values like 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, or 23 for a since these are all relatively prime to 26.
b = 26  # Using 26 for initialization, will be changed later
while b:
    a, b = b, a % b
gcd_result = a

# Get user input for A and B values
plaintext = input("Enter the text: ")
a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))


# Calculate the modular inverse of 'a' modulo 26
m = 26
mod_inv = None
for i in range(1, m):
    if (a * i) % m == 1:
        mod_inv = i
        break

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
