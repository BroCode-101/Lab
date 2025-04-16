from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
import base64

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

data = b"This is a sample message."

signature = private_key.sign(data, hashes.SHA256())
encoded_sig = base64.b64encode(signature)

try:
    public_key.verify(base64.b64decode(encoded_sig), data, hashes.SHA256())
    print("Signature is Valid")
except:
    print("Signature is Invalid")
