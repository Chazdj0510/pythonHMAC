import hmac
import hashlib
import base64
import json

# Secret key for HMAC
SECRET_KEY = "mySecretKey"

def compute_hmac(message, secret_key):
    hash_algorithm = hashlib.sha256
    hmac_object = hmac.new(secret_key.encode(), message.encode(), hash_algorithm)
    hmac_digest = hmac_object.digest()
    encoded_hmac = base64.b64encode(hmac_digest).decode()
    return encoded_hmac

# Define the payload
payload = {
    "data": "This is a secure message",
    "sender": "appSend"
}

# Convert payload to JSON and generate HMAC
payload_json = json.dumps(payload)
signature = compute_hmac(payload_json, SECRET_KEY)

# Save the payload and signature to a file (simulating sending)
with open("message.json", "w") as f:
    json.dump({"payload": payload_json, "signature": signature}, f)

print("✅ Message sent and saved to message.json!")
