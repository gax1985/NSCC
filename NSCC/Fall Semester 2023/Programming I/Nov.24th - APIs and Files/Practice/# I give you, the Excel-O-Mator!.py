#   I give you, the Excel-O-Mator!
##################################

# Here is what needs to be done for this joyous task : 
###########################################################                                                                                                        
ooooo 8               .oPYo.                      8       .oPYo.       o     o          o               
  8   8               8.                          8       8    8       8b   d8          8               
  8   8oPYo. .oPYo.   `boo   `o  o' .oPYo. .oPYo. 8       8    8       8`b d'8 .oPYo.  o8P .oPYo. oPYo. 
  8   8    8 8oooo8   .P      `bd'  8    ' 8oooo8 8 ooooo 8    8 ooooo 8 `o' 8 .oooo8   8  8    8 8  `' 
  8   8    8 8.       8       d'`b  8    . 8.     8       8    8       8     8 8    8   8  8    8 8     
  8   8    8 `Yooo'   `YooP' o'  `o `YooP' `Yooo' 8       `YooP'       8     8 `YooP8   8  `YooP' 8     
::..::..:::..:.....::::.....:..:::..:.....::.....:..:::::::.....:::::::..::::..:.....:::..::.....:..::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    
# 1. Find the Ottawa_Ball_Diamonds.csv file on
#    Brlghtspace in the Reading from Files —
#    Resources ZIP file

# 2. Write an application that reads in the data
#    from the file

# 3. Ask the user what type of fields they want to
#   list: softball, baseball, or T-Ball

# 4. List the FACILITYID( third column) and
#   FIELD_NAME (6" column) of all those ball
#   fields
# # 
# # 

def main():

    import csv

    print("""                                                                                                        
ooooo 8               .oPYo.                      8       .oPYo.       o     o          o               
  8   8               8.                          8       8    8       8b   d8          8               
  8   8oPYo. .oPYo.   `boo   `o  o' .oPYo. .oPYo. 8       8    8       8`b d'8 .oPYo.  o8P .oPYo. oPYo. 
  8   8    8 8oooo8   .P      `bd'  8    ' 8oooo8 8 ooooo 8    8 ooooo 8 `o' 8 .oooo8   8  8    8 8  `' 
  8   8    8 8.       8       d'`b  8    . 8.     8       8    8       8     8 8    8   8  8    8 8     
  8   8    8 `Yooo'   `YooP' o'  `o `YooP' `Yooo' 8       `YooP'       8     8 `YooP8   8  `YooP' 8     
::..::..:::..:.....::::.....:..:::..:.....::.....:..:::::::.....:::::::..::::..:.....:::..::.....:..::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n\n""")





    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")



        #   Let us start with declaring the variables we will use: 
        

        file_name = "Ottawa_Ball_Diamonds.csv"
        access_mode = "r"
        user_choice = ""
        is_valid_option = False

        
        #   Now for the fun part (where we indicate the .CSV file in question, indicating the access mode) :
        

        with open(file_name, access_mode) as my_csv_file:

            #   We are declaring the csv_data variable to hold the contents of the .CSV file :

            csv_data = csv.reader(my_csv_file)

            #   Let us ask the user for the type of field they would like to have : 
                

            user_choice = input("What Type of Field would you like to list (softball, baseball, or T-Ball) ? \n\n")

            

            while  not  is_valid_option:

                user_choice = input("What Type of Field would you like to list (softball, baseball, or T-Ball) ? \n\n")

                if user_choice not in valid_options:

                    print("Please Enter a Valid Field Type(Baseball, Softball, or T-Ball)?")


                else:

                    is_valid_option = True

                    for row in csv_data:
                        if row[3].lower() == user_choice.lower():
                            print(f"Facility ID : {row[2]} \t Field Name : {row[5]}")



                
    






# If you want a challenge , output the query to a separate file 
























if __name__ == "__main__":
    main()



