def encrypt(message, key):
    cipher = ""
    for k in range(key):
        for i in range(k, len(message), key):
            cipher += message[i]
    return cipher

def decrypt(cipher, key):
    num_cols = key
    num_rows = len(cipher) // key
    decrypted = [""] * num_rows

    col = 0
    for char in cipher:
        decrypted[col % num_rows] += char
        col += 1

    return "".join(decrypted)

# Example usage
message = "HELLO WORLD"
key = 4
encrypted = encrypt(message.replace(" ", ""), key)
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
