import string
from passGenerate import passGenerate
from randomPass import randomPass
from clearScreen import clearScreen
from passwordAccess import accessPassword
from customPass import customPass
from cryptography.fernet import Fernet
from login import login
import encryptionKey

def main():
  if login():
    clearScreen()
    print("Welcome to your password manager!\nSelect an option below:\n" +
          "1. Generate a random password\n" + "2. Access Paswords\n" 
          + "3. input custom password")
    userChoice = int(input("Enter your choice: "))
  
    if userChoice == 1:
      clearScreen()
      passGenerate()
      print("\n\n")
      terminate = input("input 'xxx' to return to the main menu: ")
      if terminate.lower() == 'xxx':
        clearScreen()
        main()
    elif userChoice == 2:
      clearScreen()
      accessPassword()
        
      main()
    elif userChoice == 3:
      clearScreen()
      customPass()
      print("\n\n")
      terminate = input("input 'xxx' to return to the main menu: ")
      if terminate.lower() == 'xxx':
        clearScreen()
        main()
    else:
      print("Invalid choice!")
      main()
  
  
if __name__ == "__main__":
  main()
