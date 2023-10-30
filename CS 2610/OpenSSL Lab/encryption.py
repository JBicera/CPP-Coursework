from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Public Key
publicKeyFile = "wongPublicKey.pem"
plaintextFile = "plaintext.txt"
ciphertextFile = "ciphertext.txt"

def encrypt_file(plaintextFile, publicKeyFile, ciphertextFile):
    # Load public key
    with open(publicKeyFile, "rb") as inputFile:
        publicKey = serialization.load_pem_public_key(inputFile.read(), backend=default_backend())

    # Read plaintext file
    with open(plaintextFile, "rb") as file:
        plaintext = file.read()


    # Encrypt
    ciphertext = publicKey.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Encode as base64
    cipherTextB64 = base64.b64encode(ciphertext).decode()

    # Write to output file
    with open(ciphertextFile, "w") as outputFile:
        outputFile.write(cipherTextB64)

# Final Output
encrypt_file(plaintextFile, publicKeyFile, ciphertextFile)
print(f"{ciphertextFile} generated.")
