# Party Guest List 
# Ask the user to enter the names of everyone attending to a party.
# Then return a list of the party guests in alphabetical order.

def main():
    # create an empty guests list
    guests_list = []
    # initilize guest_name variable
    guest_name = ""
    GuestListFile = 'Guest_List.csv'
    
    AccessMode = 'w'

    GuestListFileHandler = open(GuestListFile, AccessMode)


    # create a loop to repeat name input until user enters 'done'
    while guest_name.lower() != 'done':
        # getting the guest name entered by the user
        guest_name = input("Enter the name of the guest (or 'done' to finish): ")
        
        #if statement to avoid adding 'done' to the list        
        if guest_name.lower() != 'done':
            # adding the current guest name to the file
            AccessMode = 'a' 
            GuestListFileHandler.write(guest_name + "," + "\n")

            # or ..

            # GuestListFileHandler.write(f"{guest_name}\n")


    # remove the last element in my list ('done')  - in case there's no if statement inside the loop
    # del guests_list[-1]

    # sort the list of guests in alphabetical order
    # guests_list.sort()

    # output the guests list
    print(f"\nThe Guest list of your party is located in the {GuestListFile} file.\n")
    
    GuestListFileHandler.close()
    # # for loop to go through list and print each guest name
    # for guest in guests_list:
    #     print(guest)

if __name__ == "__main__":
    main()