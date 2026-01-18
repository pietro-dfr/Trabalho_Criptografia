from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Solicita ao usuário uma mensagem e converte para bytes,
# pois os algoritmos criptográficos trabalham nesse formato
message = input("Digite a mensagem: ").encode()

# Gera a chave privada RSA
# O expoente 65537 é o padrão por ser seguro e eficiente
# O tamanho de 2048 bits é o mínimo recomendado atualmente
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# A chave pública é derivada diretamente da chave privada
# Ela pode ser compartilhada sem comprometer a segurança
public_key = private_key.public_key()

# Criptografa a mensagem usando a chave pública
# O padding OAEP com SHA-256 aumenta a segurança do processo
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("\nTexto criptografado:")
print(ciphertext)

# Descriptografa a mensagem usando a chave privada
# Apenas a chave privada consegue reverter o processo
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("\nDescriptografado:")
print(decrypted_message.decode())

input("...")
