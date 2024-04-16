def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def find_e(phi):
    """Find an integer e such that e is coprime to phi."""
    e = 2
    while e < phi and gcd(e, phi) != 1:
        e += 1
    return e

# Constants for the RSA setup
p = 3
q = 7
n = p * q
phi = (p - 1) * (q - 1)
e = find_e(phi)

# Generate the private key, d
k = 1  # You can vary k to find a suitable d
d = (1 + (k * phi)) // e

# Message to be encrypted
msg = 12

print("Message data:", msg)

# Encryption
c = pow(msg, e, n)
print("Encrypted data:", c)

# Decryption
m = pow(int(c), d, n)
print("Decrypted Message:", m)