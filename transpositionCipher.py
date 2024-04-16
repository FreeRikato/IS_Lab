def transpose(text, key, mode):
  # Remove non-alphabetic characters and convert to uppercase
  text = ''.join(char.upper() for char in text if char.isalpha())
  # Create empty list to store transposed characters
  cipher = []
  # Loop through each character based on the mode
  if mode == 'encrypt':
    # Fill columns for encryption
    for i in range(key):
      col = ''.join(text[j::key] for j in range(i, len(text), key))
      cipher.append(col)
  else:
    # Fill rows for decryption
    decrypted_len = len(text) // key  # Calculate expected row length with padding if needed
    for i in range(decrypted_len):
      row = ''.join(text[i * key: (i + 1) * key])
      cipher.append(row[:decrypted_len])  # Truncate extra characters for padding
  # Join the transposed characters and return
  return ''.join(cipher)

# Example usage
text = "HELLO WORLD"
key = 3

encrypted_text = transpose(text, key, 'encrypt')
decrypted_text = transpose(encrypted_text, key, 'decrypt')

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
