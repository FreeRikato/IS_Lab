def caesar_cipher(text, shift):
    # Encrypts or decrypts text by shifting each letter by 'shift' positions in the alphabet.
    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            start = ord('a') if char.islower() else ord('A')
            # Shift character and wrap around the alphabet
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Non-alphabet characters remain the same
    return result


def keyword_cipher(text, keyword):
    # Create a cipher alphabet based on the keyword
    alphabet = ''.join(sorted(set(keyword), key=keyword.index)) + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in keyword)
    key = {chr(i): alphabet[i - ord('a')] for i in range(ord('a'), ord('z') + 1)}
    # Encrypt or decrypt by substituting based on the keyword-generated alphabet
    result = ''.join(key[char] if char in key else char for char in text.lower())
    return result


def atbash_cipher(text):
    # Encrypt or decrypt text by reversing the alphabet
    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Reverse letter's position in the alphabet
            result += chr(ord('a') + ord('z') - ord(char.lower())) if char.islower() else chr(ord('A') + ord('Z') - ord(char))
        else:
            result += char  # Non-alphabet characters remain the same
    return result

# Example usage:
text = "Hello, World!"
shift = 3
encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, -shift)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)


# Example usage:
keyword = "keyword"
text = "hello"
encrypted = keyword_cipher(text, keyword)
# Decryption would require reversing the key map
print("Encrypted:", encrypted)


# Example usage:
text = "Hello, World!"
encrypted = atbash_cipher(text)
decrypted = atbash_cipher(encrypted)  # Encryption and decryption are the same operation
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
