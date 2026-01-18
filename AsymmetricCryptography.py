from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

message = input("Digite a mensagem: ").encode()

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

public_key = private_key.public_key()

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("\nTexto criptografado: ")
print(ciphertext)

decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print("\nDescriptografado :")
print(decrypted_message.decode())
