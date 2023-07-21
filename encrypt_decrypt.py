pattern = int(input("What is the pattern?"))

def caesar_encrypt(plaintext):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            encrypted += chr((ord(char) - ascii_offset + pattern) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            decrypted += chr((ord(char) - ascii_offset - pattern) % 26 + ascii_offset)
        else:
            decrypted += char
    return decrypted

# Implementation, will infinitely run
while 1 == 1:

    method = input("Are you trying to encrypt(e)? or decrypt(d)?").lower()
    if method == "e":
        pass
    elif method == "d":
        pass
    else:
        print("Not a valid response")
        break
# Encrypt goes forwards, decrypt goes backwards
    name = input(f"And what is the name that you're trying to {method}?")

    if method == "e":
        e = caesar_encrypt(name)
        print(f"Original Name: {name} \n Encrypted Name: {e}")
    elif method == "d":
        d = caesar_decrypt(name)
        print(f"Encrypted Name: {name} \n Decrypted Name: {d}")

