from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

# Self-Signed Certificate File
certificateFile = "signedCertificate.pem"

# Open File
def load_certificate(certificateFile):
    with open(certificateFile, "rb") as cFile:
        certificateData = cFile.read()
        certificate = x509.load_pem_x509_certificate(certificateData, default_backend())
        return certificate

def display_certificate_details(certificate):
    # Get the notBefore and notAfter dates (validity period)
    start = certificate.not_valid_before
    end = certificate.not_valid_after

    # Final Output
    print("\nCertificate Details:")
    print(certificate)
    print("\nValid from:", start)
    print("Valid until:", end)

if __name__ == "__main__":
    certificate = load_certificate(certificateFile)
    display_certificate_details(certificate)
