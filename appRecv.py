import hmac
import hashlib
import base64
import json

# Secret key for HMAC (must be the same as sender's)
SECRET_KEY = "mySecretKey"

def verify_hmac(message, received_signature, secret_key):
    expected_signature = base64.b64encode(
        hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).digest()
    ).decode()
    return hmac.compare_digest(expected_signature, received_signature)

# Read the message file (simulating receiving)
with open("message.json", "r") as f:
    message_data = json.load(f)

payload_json = message_data["payload"]
received_signature = message_data["signature"]

# Verify the signature
if verify_hmac(payload_json, received_signature, SECRET_KEY):
    print("✅ Message verified successfully!")
else:
    print("❌ Message verification failed! Possible tampering detected.")
