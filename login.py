import os
import time
import sys
import encryptionKey
# adminPass = "set Admin Password here"



def login():
  print("Login: ")
  password = input("Enter the password: ")
  if password == adminPass:
    print("Login Successful!")
    return True
  else:
    print("Login Failed!\n terminating program in 3 seconds...")
    time.sleep(3)
    sys.exit(1)

  