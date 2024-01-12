


#import LeapOrNot from LeapYear
def LeapOrNot(in_year):     # To make a custom function, we shouldf call it a parameter 

    isLeapYear = False

    if ( in_year % 4 == 0 )  and ( in_year % 100 != 0) or ( in_year % 400 == 0 ):   # Both of these statements have to be true to make it a Leap Year!
        
        #isLeapYear = True
        return True
    
    else:
        

        #isLeapYear = False
        #return isLeapYear
        return False # There may be an arguement to avoid using two Re
    
def main():



   # We would have to test if the year is divisible by 4 , and not divisible by 100
    
    # We would have to test if the year is divisible by 400 
    
    # Since it would be a leap year if either of those conditions are true, we should use OR :  
    
    
    # We will as the user for the year
    
    
    
    
    year = int(input("Please Enter the Year : "))
    
    if LeapOrNot(year):
        
        print("The year you have entered is a leap year!")
        
        
    else: 
        
        print("The year you have entered is not a Leap Year!")



# We moved the block from the main function to check if it is a leap year.

#Improvements:
###############

# Instead of a variable
    
    
    
if __name__ == "__main__":
    main()