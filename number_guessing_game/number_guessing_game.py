
import random 


print("Welcome to the number guessing game in python :)")



computer_guess=int(random.randint(1,10))

for i in range(1,6):
    try: 
        user_guess=int(input("Enter a number between 1 to 10: "))

    
        
        if user_guess <= 10 and user_guess >= 1:
            if user_guess == computer_guess :
                 print("Your guess is right")
                 break

            elif user_guess > computer_guess:
                print(f"Your guess is a bit high \ntry again in attempt {i+1}")
               
               
            elif user_guess < computer_guess:
                print(f"Your guess is a bit low \ntry again in attempt {i+1} ")    
    except ValueError:
        print("Enter a Valid number!")
else:
    print(f"you lost the game the number was {computer_guess}")           

    