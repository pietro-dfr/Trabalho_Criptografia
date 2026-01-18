from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

message = input("Digite a mensagem: ").encode()

key = os.urandom(32)
iv = os.urandom(16)

padder = padding.PKCS7(128).padder()
padded_message = padder.update(message) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

print("===============")

print("Texto criptografado:")
print(ciphertext)

decryptor = cipher.decryptor()
decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
original_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

print("Descriptografo:")
print(original_message.decode())
