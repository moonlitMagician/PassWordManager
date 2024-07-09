from clearScreen import clearScreen  # Import clearScreen function from clearScreen module
from cryptography.fernet import Fernet
import encryptionKey




def accessPassword():
    while True:
        print("Accessing Passwords...\n")
        fileName = input("Enter the password you want to access (without .txt extension): ")

        try:
            with open(f'generatedPasswords/{fileName}.txt', 'rb') as f:
                clearScreen()
                encrypted_password = f.read()
                key = encryptionKey.load_key()


                decrypted_password = encryptionKey.decrypt_message(encrypted_password, key)
                print("Your Password is: " + decrypted_password + "\n\n")
                terminate = input("input 'xxx' to return to the main menu: ")
                if terminate.lower() == 'xxx':
                    clearScreen()
                    return
                break  # Exit the loop if password is found

        except FileNotFoundError:
            print(f"A password '{fileName}' was not found.")
            reset = input("Input 'x' to search for another password or 'y' to return to the main menu: ")

            if reset.lower() == 'x':
                clearScreen()  # Clear the screen before searching again
                continue  # Restart the loop to search for another password

            elif reset.lower() == 'y':
                clearScreen()  # Clear the screen before returning to main menu
                return  # Exit the function and return to the main program flow

        #except Exception as e:
         #   print(f"An error occurred: {e}")
         #   return  # Exit the function and return to the main program flow

# Example usage to generate and save a key


        