def encrypt(message, key):
    cipher = ""
    for k in range(key):
        for i in range(k, len(message), key):
            cipher += message[i]
    return cipher

def decrypt(cipher, key):
    num_cols = key
    num_rows = len(cipher) // key
    extra_chars = len(cipher) % key

    decrypted = [""] * (num_rows + (1 if extra_chars else 0))
    col, pos = 0, 0

    for char in cipher:
        decrypted[col] += char
        pos += 1
        col += 1
        if col == num_rows + (1 if extra_chars and pos <= extra_chars * (num_rows + 1) else 0):
            col = 0

    return "".join(decrypted).strip()

# Example usage
message = "HELLO WORLD"
key = 4
encrypted = encrypt(message.replace(" ", ""), key)
decrypted = decrypt(encrypted, key)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
