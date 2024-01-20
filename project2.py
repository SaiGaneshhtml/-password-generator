import string
import random

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")
    random.shuffle(characters)
    
    password = [random.choice(characters) for _ in range(password_length)]
    
    random.shuffle(password)
    
    password = "".join(password)
    print(password)

while True:
    option = input("Do you want to generate a password? (Yes/No): ").lower()

    if option == "yes":
        generate_password()
        input("Press Enter to generate another password...")
    elif option == "no":
        print("Program ended")
        break
    else:
        print("Invalid input, please input Yes or No")

# Keep the window open until the user presses Enter
input("Press Enter to exit...")


