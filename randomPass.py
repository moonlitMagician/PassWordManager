import random
import string

def randomPass(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  random_string = ''.join(random.choices(characters, k=length))
  return random_string