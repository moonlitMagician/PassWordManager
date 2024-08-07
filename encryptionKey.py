from cryptography.fernet import Fernet

    # Generate a key for encryption
def generate_key():
        return Fernet.generate_key()

    # Load the key from a file

def load_key():
        return open("secret.key", "rb").read()

    # Save the key to a file
def save_key(key):
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    # Encrypt a message

def encrypt_message(message, key):
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message

    # Decrypt a message

def decrypt_message(encrypted_message, key):
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message
        
