from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import docx
import os

#Helper functions for reading and writing files
def readDoc(filePath):
    doc = docx.Document(filePath)
    fileStr = ""
    for paragraph in doc.paragraphs:
        fileStr += paragraph.text + "\n"
    return fileStr

def readBin(filePath):
    with open(filePath, 'rb') as file:
        data = file.read()
        return data
    
def writeText(filePath, plaintext):
    with open(filePath, 'wb') as file:
        file.write(plaintext)
        file.close()

def generateKey(filePath):
    with open(filePath, 'wb') as file:
        key = get_random_bytes(8)
        file.write(key)
        file.close()

def main():
    #Absolute directory and filenames for helper functions
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    docFileName = "Cal_Poly_Pomona_is_ranked_No_2_Best_Colleges_for_Veterans_in_the_West.docx"
    binFileName = "Bicera_DES_Key.bin"
    cipherTextFileName = "Bicera_DES_Ciphertext"
    otherBinFileName = "Wong_DES_Key.bin"
    otherCipherTextFileName = "Wong_DES_Ciphertext"

    #Generate a 64-bit (8-byte) DES key and save it to a separate file (DES_Key.bin).
    generateKey(os.path.join(scriptDirectory,binFileName))

    #Read the plaintext from the input text file
    plaintext = readDoc(os.path.join(scriptDirectory,docFileName)).encode('utf-8')

    #Encrypt the plaintext using DES_key.bin
    key = readBin(os.path.join(scriptDirectory,binFileName))
    cipher = DES.new(key, DES.MODE_ECB)
    cipherText = cipher.encrypt(plaintext)

    #Save Ciphertext to an output file
    writeText(os.path.join(scriptDirectory, cipherTextFileName),cipherText)
    #Decrypt the ciphertext using DES_key.bin
    otherKey = readBin(os.path.join(scriptDirectory, otherBinFileName))
    decipher = DES.new(otherKey,DES.MODE_ECB)
    otherCipherText = readBin(os.path.join(scriptDirectory, otherCipherTextFileName))
    decryptedText = decipher.decrypt(otherCipherText).decode('utf-8')
    print("Decrypted Cipher Text")
    print("---------------------")
    print(decryptedText)

    

main()