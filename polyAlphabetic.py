def hill_cipher(text, key, mode='encrypt'):
    def mod_inv(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q, a, m = a // m, m, a % m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def matrix_inv(matrix, mod):
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        det_inv = mod_inv((a * d - b * c) % mod, mod)
        return [[d * det_inv % mod, -b * det_inv % mod], [-c * det_inv % mod, a * det_inv % mod]]

    if mode == 'decrypt':
        key = matrix_inv(key, 26)

    text = ''.join(filter(str.isalpha, text.upper()))
    result = ""
    for i in range(0, len(text), 2):
        block = [ord(char) - ord('A') for char in text[i:i+2].ljust(2, 'A')]
        result += ''.join(chr((key[row][0] * block[0] + key[row][1] * block[1]) % 26 + ord('A')) for row in range(2))
    return result


def vigenere_cipher(text, key, mode):
    # Adjust the key to match the length of the text by repeating it
    key = (key * ((len(text) // len(key)) + 1))[:len(text)]

    # Convert the text and key into uppercase for case insensitivity
    text = text.upper()
    key = key.upper()

    # Create the result list to store each processed character
    result = []

    # Encrypt or decrypt each character based on the mode
    for char, key_char in zip(text, key):
        if char.isalpha():  # Process only alphabetic characters
            shift = ord(key_char) - ord('A')
            if mode == 'encrypt':
                # Encrypt by shifting char to the right by key_char's position
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                # Decrypt by shifting char to the left by key_char's position
                new_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(new_char)
        else:
            # Append non-alphabetic characters unchanged (optional)
            result.append(char)

    # Join the list into a string and return it
    return ''.join(result)

# Example usage:
key = [[5, 8], [17, 3]]
text = "HELLO"
encrypted = hill_cipher(text, key, 'encrypt')
decrypted = hill_cipher(encrypted, key, 'decrypt')

print(f"Original Text: {text}")
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

# Example usage
text = "HELLO WORLD"
key = "KEY"
mode = 'encrypt'

encrypted_text = vigenere_cipher(text, key, 'encrypt')
decrypted_text = vigenere_cipher(encrypted_text, key, 'decrypt')

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
