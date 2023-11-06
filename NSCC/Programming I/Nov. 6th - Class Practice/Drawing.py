#from tkinter import *
import turtle

def main():
    


    LineLength = 0

    Angle = 0 

    while LineLength != 0:
        PenColor = input("Please Enter the Desired Line Color :  ")
        LineLength = int(input("Please Enter the Line Length :  "))
        Angle = int(input("Please Enter the Desired Angle :  "))
        turtle.Color(PenColor)
        turtle.forward(LineLength)
        turtle.right(Angle)
    turtle.done()


        


    
if __name__ == "__main__":
    main()