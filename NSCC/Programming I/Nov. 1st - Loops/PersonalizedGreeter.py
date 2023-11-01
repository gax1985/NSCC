
# Write a program that prompts the user to enter their friends names, as many as the user likes.
# When a user prints a name, print a personalized greeting for that name 



def main():


    greeting_number = int(input("Please enter the number of people you would like to greet :  ")   # It is the number the user typed in 

    for counter in range(greeting_number) # 0 , 1 , 2 , 3 , greeting_number -1 
        person_name = input(f"Please Enter the Person {counter+1} Name  :   ")
        print(f"Hello {person_name}!") 



    
if __name__ == "__main__":
	main()
 
    