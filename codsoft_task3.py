import random
import string

print("PASSWORD GENERATOR")

length = int(input("Enter password length: "))

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password = password + random.choice(all_characters)

print("Generated Password is:")
print(password)
