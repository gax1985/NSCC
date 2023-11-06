# #from tkinter import *
# import turtle

# def main():
    


#     LineLength = 0

#     Angle = 0 

#     while LineLength != 0:
#         PenColor = input("Please Enter the Desired Line Color :  ")
#         LineLength = int(input("Please Enter the Line Length :  "))
#         Angle = int(input("Please Enter the Desired Angle :  "))
#         turtle.Color(PenColor)
#         turtle.forward(LineLength)
#         turtle.right(Angle)
#     turtle.done()


        


    
# if __name__ == "__main__":
#     main()


#********************************************************************************************************************

# His Answer : 
##############

import turtle

def main():

    # # Have the user enter the pen color 

    # pen_color = input("Please Enter a Pen Color :  ")

    # # Have the user enter the line length : 
        
    # line_length = input("Please Enter the Line Length :  ")


    # # Have the user enter the angle:

    # Angle = input("Please enter the Angle :  ")


    # # Have the line drawn according to the user's specifications :   

    # turtle.color(pen_color)
    # turtle.forward(line_length)


    # turtle.done() # We need to enter this line so the drawing remains


    ##############################################################################

    line_length = -1 # Since the loop will never execute if it is actually 0. -1 cannot possibly 

    line_width = 5 # If we wish to control the Line's Width 

    turtle.width(line_width)

    while line_length != 0:

        # Have the user enter the pen color 

        pen_color = input("Please Enter a Pen Color :  ")

        # Have the user enter the line length : 
            
        line_length = float(input("Please Enter the Line Length :  ")) # It is expecting Float 


        # Have the user enter the angle:

        Angle = float(input("Please enter the Angle :  ")) # It is expecting Float as well


        # Have the line drawn according to the user's specifications :   

        turtle.color(pen_color)
        turtle.forward(line_length)


        turtle.done() # We need to enter this line so the drawing remains

if __name__ == "__main__":
        main()
