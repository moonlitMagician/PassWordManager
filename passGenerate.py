from randomPass import randomPass
import os
import encryptionKey

def passGenerate():
    length_of_string = int(input("Enter the length of the password: "))
    password = randomPass(length_of_string)
    file_name = input("Enter the name of the password you're setting: ")
    file_name = file_name + ".txt"

    if os.path.exists(f"generatedPasswords/{file_name}"):
        print(f"Your Password is Already saved!")
        return

    key = encryptionKey.load_key()
    encrypted_password = encryptionKey.encrypt_message(password, key)

    with open(f"generatedPasswords/{file_name}", 'wb') as file:
        file.write(encrypted_password)

    print('Password generated and encrypted!')

  # Example usage to generate and save a key
