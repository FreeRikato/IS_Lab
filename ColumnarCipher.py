def encrypt(text, key):
    """
    Encrypt the text using a columnar transposition cipher.
    
    text: string to be encrypted (plaintext).
    key: integer that represents the number of columns for the cipher.
    """
    # Remove spaces from the text for encryption
    text = text.replace(" ", "")
    
    # Create a list to hold the text columns
    columns = [''] * key
    
    # Distribute the characters in the text across the columns
    for i in range(len(text)):
        col = i % key
        columns[col] += text[i]
    
    # Combine columns to get the encrypted text
    encrypted_text = ''.join(columns)
    return encrypted_text

def decrypt(encrypted_text, key):
    """
    Decrypt the text using a columnar transposition cipher.
    
    encrypted_text: string to be decrypted (ciphertext).
    key: integer that represents the number of columns used during encryption.
    """
    # Calculate the number of rows that will be in the grid
    rows = len(encrypted_text) // key
    # If there's a remainder, add another row for the uneven distribution
    remainder = len(encrypted_text) % key
    
    # Create a list to hold the text rows
    plaintext = [''] * rows
    
    # Variables to keep track of the column and row being filled
    col = 0
    row = 0
    
    # Distribute the characters in the encrypted text across the grid
    for symbol in encrypted_text:
        plaintext[row] += symbol
        row += 1
        # If we hit the last row, or hit the short column, reset row to 0 and move to next column
        if (row == rows and col >= remainder) or (row == rows + 1):
            row = 0
            col += 1
    
    # Combine rows to get the decrypted text
    decrypted_text = ''.join(plaintext)
    return decrypted_text

# Example usage
plaintext = "The bird has flown at midnight"
key = 5

encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)