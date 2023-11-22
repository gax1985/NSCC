

# — Ask the  user to enter the names and
# ages of everyone attending to a party.

# — If the user enters an age that is not a
# number, handle that error gracefully and
# ask them again

# While writing the info into the csv file,
# handle the exceptions that we might
# reasonably expect to occur during the
# writing











##############################################################################################################






# Party Guest List 
# Ask the user to enter the names of everyone attending to a party.
# Then return a list of the party guests in alphabetical order.

def main():
    # create an empty guests list
    guests_list = []
    # initilize guest_name variable
    guest_name = ""

    # We create an empty age list : 

    guests_age_list = []

    # ... and a variable to store the text in, which would be added to the Guests' Age List : 

    guests_age_text = ""

    # create a loop to repeat name input until user enters 'done'
    while guest_name.lower() != 'done':
        # getting the guest name entered by the user
        guest_name = input("Enter the name of the guest (or 'done' to finish): ")
        
        #if statement to avoid adding 'done' to the list        
        if guest_name.lower() != 'done':
            # adding the current guest name to the list
            
            
            try:
                guest_age_text = int(input(f"Please enter {guest_name}'s Age : "))
                guests_list.append(guest_name)
                guests_age_list.append(guest_age_text)

            except ValueError:

                print("You have entered an invalid age. Please enter a number for the age!")

       

        for guest in guest_name:
            print(f"The Guest's Name is {guests_list(counter)})



    # remove the last element in my list ('done')  - in case there's no if statement inside the loop
    # del guests_list[-1]

    # sort the list of guests in alphabetical order
    guests_list.sort()

    # output the guests list
    print("\nThe Guest list of your party is:\n")

    # for loop to go through list and print each guest name
    for guest in guests_list:
        print(f"The Guest's Name : {guest} \n")
        for age in guests_age_list:
            print(f"Age : {age}\n \n")






if __name__ == "__main__":
    main()