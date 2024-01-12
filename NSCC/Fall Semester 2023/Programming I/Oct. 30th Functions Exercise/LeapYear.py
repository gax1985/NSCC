

def LeapOrNot(YearValue):
    
    # We would have to test if the year is divisible by 4 , and not divisible by 100
    
    # We would have to test if the year is divisible by 400 
    
    # Since it would be a leap year if either of those conditions are true, we should use OR :  
    
    
    # We will as the user for the year
    
    if YearValue % 4 == 0 and YearValue % 100 != 0: 
        print("The year is a Leap Year!")
    
    elif YearValue % 400 == 0:
        print("The year is a Leap Year!")
        
    
    else:
        print("The year is an ordinary, boring year!")



def main():
    
    YearValue = int(input("Please enter the year that you would like to check if it is a Leap Year :  "))
    LeapOrNot(YearValue)
    
    

    
    
    
    
    
    
if __name__ == "__main__":
    main()