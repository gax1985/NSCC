
import random

def main():
    

    number_to_guess = random.randit(1,100)

    number_guess = 0 # Pick a number outside of the range of the randomized number

    while user_guess != number_to_guess:

            
            user_guess = int(input("Please Guess a Number from 1 to 100 :  "))

            if number_to_guess < user_guess:
                print(f"The number is lower than {user_guess}")

            elif number_to_guess > user_guess:
            
                print(f"The Number is higher than {user_guess}")

    print(f"You got it! The number is {number_to_guess})    

# In FOR loops, variable used to control FOR loops can be decaled in the FOR loop itself. Here we have to initialize it. 
        


    
if __name__ == "__main__":
    main()