

def LeapOrNot(YearValue):
    
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