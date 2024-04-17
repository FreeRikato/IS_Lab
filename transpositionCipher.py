def transpose(text, key, mode):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(char for char in text.upper() if char.isalpha())

    if mode == 'encrypt':
        # Encrypt by reading columns
        cipher = []
        for i in range(key):
            cipher.append(text[i::key])
        return ''.join(cipher)
    elif mode == 'decrypt':
        # Decrypt by reassembling into columns correctly
        n = len(text)
        full_columns = n // key
        short_columns = n % key
        rows = [''] * key
        start_idx = 0

        for i in range(key):
            if i < short_columns:
                # Columns that have an extra character (due to uneven division)
                rows[i] = text[start_idx:start_idx + full_columns + 1]
                start_idx += full_columns + 1
            else:
                rows[i] = text[start_idx:start_idx + full_columns]
                start_idx += full_columns

        # Reassemble by rows
        plain = []
        for i in range(full_columns + 1):  # +1 because the longest column might be one character longer
            for j in range(key):
                if i < len(rows[j]):
                    plain.append(rows[j][i])

        return ''.join(plain)

# Example usage
text = "HELLO WORLD"
key = 3

encrypted_text = transpose(text, key, 'encrypt')
decrypted_text = transpose(encrypted_text, key, 'decrypt')

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
