from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Private Key passphrase
passphrase = b'helloWorld'

# Read the Private Key
with open('biceraPrivateKey.pem', 'rb') as privatekeyFile:
    privateKey = serialization.load_pem_private_key(privatekeyFile.read(), password = passphrase)

# Extract the public key
publicKey = privateKey.public_key()

# Convert to PEM format
formattedPublicKey = publicKey.public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save Public Key to a file
with open('biceraPublicKey.pem', 'wb') as publicKeyFile:
    publicKeyFile.write(formattedPublicKey)
