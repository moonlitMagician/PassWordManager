import os
from cryptography.fernet import Fernet
import encryptionKey
key = encryptionKey.load_key()

def customPass():
  print("Enter Your Custom Password to be saved!: ")
  userPass = input("Enter your password: ")
  encrypted_password = encryptionKey.encrypt_message(userPass, key)
  file_name = input("Enter the name of the password you're setting: ")
  file_name = file_name+".txt"
  if os.path.exists(f"generatedPasswords/{file_name}"):
    print(f"Your Password is Already saved!")
    return

  with open(f"generatedPasswords/{file_name}", 'wb') as file:
    file.write(encrypted_password)
  print('password generated!')