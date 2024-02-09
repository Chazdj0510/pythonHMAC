import hmac
import hashlib
import base64

def compute_hmac(message, secret_key):
    # Choose a hash function
    hash_algorithm = hashlib.sha256
    # Compute the HMAC using the chosen hash function and the secret key
    hmac_object = hmac.new(secret_key.encode(), message.encode(), hash_algorithm)
    # Get the digest (HMAC value)
    hmac_digest = hmac_object.digest()
    # Encode the digest to Base64 or hexadecimal
    encoded_hmac = base64.b64encode(hmac_digest).decode()  # Base64 encoding
    return encoded_hmac

# Example usage
message = "Hello, HMAC!"
secret_key = "mySecretKey"

hmac_result = compute_hmac(message, secret_key)
print("HMAC:", hmac_result)

