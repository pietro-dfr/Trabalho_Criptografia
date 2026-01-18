from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Solicita a mensagem ao usuário e converte para bytes,
# formato exigido pelos algoritmos criptográficos
message = input("Digite a mensagem: ").encode()

# Gera uma chave secreta aleatória de 32 bytes,
# equivalente ao AES-256, padrão seguro e amplamente utilizado
key = os.urandom(32)

# Gera o vetor de inicialização (IV),
# necessário para garantir aleatoriedade no modo CBC
iv = os.urandom(16)

# Aplica padding PKCS7 para ajustar a mensagem
# ao tamanho fixo de bloco do AES (128 bits)
padder = padding.PKCS7(128).padder()
padded_message = padder.update(message) + padder.finalize()

# Cria o objeto de cifra utilizando AES no modo CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Realiza a criptografia da mensagem
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

print("===============")
print("Texto criptografado:")
print(ciphertext)

# Inicializa o processo de descriptografia
decryptor = cipher.decryptor()
decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()

# Remove o padding para recuperar a mensagem original
unpadder = padding.PKCS7(128).unpadder()
original_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

print("Descriptografado:")
print(original_message.decode())

input("...")
