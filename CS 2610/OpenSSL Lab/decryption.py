from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import sys

# Private Key
privateKeyFile = "biceraPrivateKey.pem"
passphrase = "helloworld"

# Ciphertext file (input)
ciphertextFile = "toBiceraCipherText.txt"

# Plaintext file (output)
plaintextFile = "toBiceraPlainText.txt"

def decrypt_file(ciphertextFile, privateKeyFile, passphrase, plaintextFile):
    # Load private key
    with open(privateKeyFile, "rb") as inputFile:
        privateKey = serialization.load_pem_private_key(
            inputFile.read(),
            password=passphrase.encode(),
            backend=default_backend()
        )

    # Read ciphertext file
    with open(ciphertextFile, "r") as cipherFile:
        ciphertextB64 = cipherFile.read()

    # Decode from base64
    ciphertext = base64.b64decode(ciphertextB64)

    # Decrypt
    try:
        plaintext = privateKey.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except Exception as e:
        print(e)
        sys.exit(1)

    # Write to output file
    with open(plaintextFile, "wb") as outputFile:
        outputFile.write(plaintext)

# Final Output
decrypt_file(ciphertextFile, privateKeyFile, passphrase, plaintextFile)
print(f"{plaintextFile} generated.")
