from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
hash_code = b"Campus Schwarzwald"
signature = private_key.sign(
    hash_code,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
base64_signature = base64.b64encode(signature).decode()
print(base64_signature)
