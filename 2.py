def monoalphabetic_encrypt(message, key):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

key = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm',
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O', 'J': 'P',
    'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
    'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'
}

message = "Hello, World!"
encrypted_message = ''.join([key[char] if char in key else char for char in message])

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
