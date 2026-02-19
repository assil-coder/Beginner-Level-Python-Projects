import random
import string

while True:
    
    print("========= PASSWORD GENERATOR =========")

    password_length=int(input("Enter the length of your password: "))
    uppercase_letters=input("Do you want to include uppercase (y/n)? ")
    numbers=input("Do you want to include numbers (y/n)? ")
    symbols=input("Do you want to include symbols (y/n)? ")

    characters=string.ascii_lowercase

    if uppercase_letters=="y":
        characters += string.ascii_uppercase
    
    if numbers== "y":
        characters += string.digits

    if symbols== "y":
        characters += string.punctuation
    
    password=""
    for i in range(password_length):
        password += random.choice(characters)


    print(f"Your password is {password}")

    another=input("Do you want to generate another password (y/n)? ")
    if another !="y":
        print("goodbye!")
        break