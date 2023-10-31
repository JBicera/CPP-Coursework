from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import sys

# Load public key (to check signature)
with open('myPublicKey.pem', 'rb') as publicKeyFile:
    publicKey = serialization.load_pem_public_key(publicKeyFile.read())

# Load private key (to decrypt message)
with open('myPrivateKey.pem', 'rb') as privateKeyFile:
    privateKey = serialization.load_pem_private_key(
        privateKeyFile.read(),
        password='password'.encode('utf-8')  # If the private key has a passphrase, provide it here
    )

# Load the email with the signature and encrypted message
with open('ciphertext.txt', 'rb') as emailFile:
    emailContent = emailFile.read().decode('utf-8')

# Separate signature & ciphertext
encodedSignature, encodedCiphertext = emailContent.split('\n', 1)

# Decode from Base64
signature = base64.b64decode(encodedSignature)
ciphertext = base64.b64decode(encodedCiphertext)

# Verify signature
try:
    publicKey.verify(
        signature,
        ciphertext,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified.")
except Exception as e:
    print(e)
    sys.exit(1)

# Decrypt the encrypted message with the recipient's private key
try:
    plaintext = privateKey.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Decrypted Email:\n{plaintext.decode('utf-8')}")
except Exception as e:
    print(e)
    sys.exit(1)
