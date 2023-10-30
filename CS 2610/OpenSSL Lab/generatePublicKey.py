from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Private Key passphrase
passphrase = b'helloworld'

# Read the Private Key
with open('biceraPrivateKey.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password = passphrase)

# Extract the public key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_pem = public_key.public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save Public Key to a file
with open('biceraPublicKey.pem', 'wb') as public_key_file:
    public_key_file.write(public_pem)
