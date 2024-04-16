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


def vigenere_encrypt(text, key):
    # Repeat the key to match the length of the text
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    # Encrypt each character by shifting it according to the key
    return ''.join(chr((ord(c) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
                   for c, k in zip(text.upper(), key.upper()) if c.isalpha())

def vigenere_decrypt(cipher_text, key):
    # Repeat the key to match the length of the ciphertext
    key = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    # Decrypt each character by reversing the shift according to the key
    return ''.join(chr((ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
                   for c, k in zip(cipher_text.upper(), key.upper()) if c.isalpha())

# Example usage:
key = [[5, 8], [17, 3]]  # Example key (must be invertible modulo 26)
text = "HELLO"
encrypted = hill_encrypt(text, key)
print("Encrypted:", encrypted)

# Example usage:
key = "KEYWORD"
text = "HELLO"
encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
