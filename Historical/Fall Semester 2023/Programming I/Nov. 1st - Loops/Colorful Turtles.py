import turtle





def drawLine():
        
    turtle.forward(100)
    turtle.right(90)
    
    
def imbedded_drawing():
    turtle.forward(50)
    turtle.right(90)


def main():


    # for number in [14,27,33,84,105]:  # The FOR loop will assume a number from each of these values.
    #     #print(number)  # if we add an increment of 2, we can : print(number + 2)
    #     output = number +2 
    #     print(output)
    
    favourite_food = ["Falafel","Hummus","Vegan Kebab","Biryani"]
    
    for food in favourite_food:
        print("I love {food}")
        
        
    # for counter in range(5): # We are creating a list of five elements starting with zero : {0, 1 , 2 , 3 , 4}
    #     print(counter)
    
    # for counter in range(2 , 8): # We are creating a list of five elements starting with zero : {2 , 3 , 4 , 5 , 6 , 7}
    #     print(counter)
    
     # for counter in range(2 , 8 , 2): # We are creating a list of 3 elements starting with zero as the third parameter adds 2 (+2) : {2 , 4 , 6 }
    #     print(counter)
    
    
if __name__ == "__main__":
	main()
 
    