import random
import string

def password_generator(length):
   # Generates a random password of the given length using basic characters.
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = []

    # Ensure password has at least one lowercase, uppercase, and digit
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(punctuation))

    # Fill the rest of the password with random characters
    for i in range(length - 4):
        password.append(random.choice(lowercase + uppercase + digits + punctuation))

    # Shuffle the list to avoid the first three characters always being in the same character type order
    random.shuffle(password)

    return ''.join(password)

# main program 
print("Welcome to Password Generator!")
length = int(input("Enter the length of the password (at least 8 characters): "))
password = password_generator(length)
if password:
    print("Generated Password : ", password)