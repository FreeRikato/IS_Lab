def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def compute_shared_secret(base, secret, modulus):
    return pow(base, secret, modulus)

# Input and validation for modulus
modulus = int(input("Enter a prime modulus (p): "))
if not is_prime(modulus): print("Modulus must be a prime number.")

# Input and validation for base
base = int(input("Enter base (g): "))
if base <= 1 or base >= modulus: print("Base must be greater than 1 and less than modulus.")

# Input for user's secret
user_secret = int(input("Enter your secret number: "))
if user_secret <= 0: print("Secret number must be positive.")

# Compute user's public value
user_public = compute_shared_secret(base, user_secret, modulus)
print(f"Your public value to send to the other party: {user_public}")

# Input for the other party's public value
other_public = int(input("Enter the other party's public value: "))

# Compute shared secret
shared_secret = compute_shared_secret(other_public, user_secret, modulus)
print(f"Your shared secret is: {shared_secret}")