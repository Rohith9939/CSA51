# Define the key matrix
key_matrix = np.array([[9, 4], [5, 7]])

def prepare_message(message, key_size):
    # Remove spaces and convert message to uppercase
    message = message.replace(" ", "").upper()
    
    # Append 'X' to the message if its length is not a multiple of key_size
    while len(message) % key_size != 0:
        message += 'X'
    
    return message

def encrypt_block(block, key_matrix):
    block_matrix = np.array([[ord(c) - ord('A') for c in block]])
    encrypted_matrix = np.mod(np.dot(block_matrix, key_matrix), 26)
    encrypted_block = "".join(chr(c + ord('A')) for c in encrypted_matrix[0])
    return encrypted_block

def encrypt_message(message, key_matrix):
    encrypted_message = ""
    key_size = key_matrix.shape[0]
    prepared_message = prepare_message(message, key_size)
    
    for i in range(0, len(prepared_message), key_size):
        block = prepared_message[i:i+key_size]
        encrypted_block = encrypt_block(block, key_matrix)
        encrypted_message += encrypted_block
    
    return encrypted_message

def main():
    message = "meet me at the usual place at ten rather than eight oclock"
    encrypted_message = encrypt_message(message, key_matrix)
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)

if __name__ == "__main__":
    main()
