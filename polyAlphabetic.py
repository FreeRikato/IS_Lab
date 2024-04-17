def hill_encrypt(text, key):
  # Remove non-alphabetic characters and convert to uppercase
  text = ''.join(char.upper() for char in text if char.isalpha())
  cipher_text = ""
  # Loop through the message two characters at a time
  for i in range(0, len(text), 2):
    block = text[i:i+2]
    # Check if there are enough characters remaining
    if len(block) < 2:
      block += 'A'  # Pad with 'A' if necessary
    # Convert characters to numerical values (A=0, B=1, ..., Z=25)
    block_num = [ord(char) - ord('A') for char in block]
    # Perform matrix multiplication with the key
    cipher_block = [(key[0][0] * block_num[0] + key[0][1] * block_num[1]) % 26,
                   (key[1][0] * block_num[0] + key[1][1] * block_num[1]) % 26]
    # Convert numerical values back to characters
    cipher_text += ''.join(chr(num + ord('A')) for num in cipher_block)
  return cipher_text


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
key = [[5, 8], [17, 3]]  # Example key (must be invertible modulo 26)
text = "HELLO"
encrypted = hill_encrypt(text, key)
print("Encrypted:", encrypted)

# Example usage
text = "HELLO WORLD"
key = "KEY"
mode = 'encrypt'

encrypted_text = vigenere_cipher(text, key, 'encrypt')
decrypted_text = vigenere_cipher(encrypted_text, key, 'decrypt')

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
