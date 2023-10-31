from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import smtplib
import ssl
import base64
import sys

# Email Server
smtpServer = 'smtp.gmail.com'   # for Gmail
smtpPort = 465                  # for SSL

# Email Account
email = ''
password = ''

# Recipient Email
recipient = ''

# Load Private Key
passphrase = 'password'
with open('myPrivateKey.pem', 'rb') as privateKeyFile:
    privateKey = serialization.load_pem_private_key(
        privateKeyFile.read(),
        password=passphrase.encode('utf-8')
    )
# Load Public Key
with open('myPublicKey.pem', 'rb') as publicKeyFile:
    publicKey = serialization.load_pem_public_key(publicKeyFile.read())

# Create a secure SSL context
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Connect to SMTP server with SSL
with smtplib.SMTP_SSL(smtpServer, smtpPort, context=context) as server:
    server.login(email, password)

    # Compose email
    plaintext = "Hello!"

    # Encrypt email content
    try:
        ciphertext = publicKey.encrypt(
            plaintext.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except Exception as e:
        print(e)
        sys.exit(1)
    
    # Sign w/ private key
    try:
        signature = privateKey.sign(
            ciphertext,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except Exception as e:
        print(e)
        sys.exit(1)
        
    
    # Encode as Base64
    encodedCiphertext = base64.b64encode(ciphertext).decode('utf-8')
    encodedSignature = base64.b64encode(signature).decode('utf-8')

    # Send email (Format: Signature/Message)
    server.sendmail(email, recipient, f'{encodedSignature}\n{encodedCiphertext}')

print('Email sent successfully.')
