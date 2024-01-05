


Due to the **Tech Check 3** not going as he has expected, we are doing practice on Conditional Statements. 


Practice : 


1. Simple Calculator : 

		Create a console based program that performs a simple mathematical operation (addition subtraction, multiplication, division based on user input ). Prompt tyhe user for two numbers and an operator and present the results. 



Added from VSCode : 


# Age Classifier


  We have a Python program that classifies a person's age into the following categories :

Neonates or newborns (birth to 1-month)
Infants (1-month to 1-year)
Child (1-year through 12-years)
Teenager (13-years through 17-years)

#   Adults (18-years and up)

#   Senior Citizens (65-years and older)

  
  

#==========================================================================================================

def main():

  
  

    EnteredAge = 0

    InvalidInput = False

  
  
  

    print("=================================================================================================\n \n")

  
  

    print("""

  

        ,----,                                                                                                                                              

      ,/   .`|                                                                                   ____                                                      

    ,`   .'  :  ,---,                         ,---,                                            ,'  , `.                          ___                        

  ;    ;     /,--.' |                        '  .' \                                        ,-+-,.' _ |                        ,--.'|_                      

.'___,/    ,' |  |  :                       /  ;    '.                                   ,-+-. ;   , ||                        |  | :,'             __  ,-.

|    :     |  :  :  :                      :  :       \     ,----._,.                   ,--.'|'   |  ;|              .--.--.   :  : ' :           ,' ,'/ /|

;    |.';  ;  :  |  |,--.   ,---.          :  |   /\   \   /   /  ' /   ,---.          |   |  ,', |  ':  ,--.--.    /  /    '.;__,'  /     ,---.  '  | |' |

`----'  |  |  |  :  '   |  /     \         |  :  ' ;.   : |   :     |  /     \         |   | /  | |  || /       \  |  :  /`./|  |   |     /     \ |  |   ,'

    '   :  ;  |  |   /' : /    /  |        |  |  ;/  \   \|   | .\  . /    /  |        '   | :  | :  |,.--.  .-. | |  :  ;_  :__,'| :    /    /  |'  :  /  

    |   |  '  '  :  | | |.    ' / |        '  :  | \  \ ,'.   ; ';  |.    ' / |        ;   . |  ; |--'  \__\/: . .  \  \    `. '  : |__ .    ' / ||  | '    

    '   :  |  |  |  ' | :'   ;   /|        |  |  '  '--'  '   .   . |'   ;   /|        |   : |  | ,     ," .--.; |   `----.   \|  | '.'|'   ;   /|;  : |    

    ;   |.'   |  :  :_:,''   |  / |        |  :  :         `---`-'| |'   |  / |        |   : '  |/     /  /  ,.  |  /  /`--'  /;  :    ;'   |  / ||  , ;    

    '---'     |  | ,'    |   :    |        |  | ,'         .'__/\_: ||   :    |        ;   | |`-'     ;  :   .'   \'--'.     / |  ,   / |   :    | ---'    

              `--''       \   \  /         `--''           |   :    : \   \  /         |   ;/         |  ,     .-./  `--'---'   ---`-'   \   \  /          

                           `----'                           \   \  /   `----'          '---'           `--`---'                           `----'            

                                                             `--`-'                                                                                        

  

    """)

  
  
  

    print("\n \n =================================================================================================\n \n")

  
  
  

    EnteredAge = input("Please enter the age (Please enter a number pertaining to the number of months or years) :  \n \n")

    EnteredUnit = input("Please enter the type of unit (either 'Y' for Years, or 'M' for Months) :  \n \n")

    if EnteredAge != int or EnteredUnit != "Y" \

        or EnteredUnit != "M":

            InvalidInput = True;

    if EnteredAge == "0":

        print("This individual is a Newborn!")

  

    elif EnteredAge == "1" and EnteredUnit == "M":

        print("This individual is a Newborn!")

    elif EnteredUnit == "M" and EnteredAge <= 12:

        print("This individual is an Infant!")    

    elif EnteredUnit == "Y" and EnteredAge <= 12 \

        and EnteredAge >= 1:

        print("This individual is an Child!")

    elif EnteredUnit == "Y" and EnteredAge <= 17 \

        and EnteredAge >= 13:

        print("This individual is an Teenager!")

  

    elif EnteredUnit == "Y" and EnteredAge >= 18:

        print("This individual is an Adult!")

  

    elif EnteredUnit == "Y" and EnteredAge >= 65:

        print("This individual is a Senior Citizen!")

    if InvalidInput == True:

        print("You have entered an incorrect entry!")

  
  
  
  

#===================================================

#### Commentary :

Newborns and infants are problematic due to the months. We will ask for the months in the first two cases: Newborns and Infants

  
  

print("welcome to the age sorter") 
age_in_years = int(input("if a newborn or an infant, please enter a zero. Please enter the age : ")) # First two are classified if the age is entered as a zero.

months = 0

  if age_in_years == 0:

months = int(input("Please enter the age in months : "))           # We ask the user to input the months

#

#       if age_in_months == 1:

#            print("This is a newborn!")

#

#       else:

#           print("Infant")

#                                                     # we are using a nested IF to see if the person is an infant

#

#   elif age_in_years <= 12:

#        print("Child!")

#

#   elif age_in_years <= 17:

#        print("Teenager")

#

#

#   elif age_in_years >= 18 and age_in_years < 65:       #this may be redundant. We can do this instead

#   elif age_in_years < 65:

#       print("Adult!")

#

#   else:                               # No need to add <= 65, since it passed by every IF statement on the way down.

  

#        print("Senior!")

  
  
  

# After debugging , we had an issue with this line when entering 0 and then 2

  

#        if age_in_months == 1:  # it should be int in months = input("Please enter the age in months : ")   so , months = int(input("Please enter the age in months : "))  

  
  

if __name__ == "__main__":

        main()





