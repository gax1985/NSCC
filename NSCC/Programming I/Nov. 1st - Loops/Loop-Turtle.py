import turtle

def drawLine():
        
    turtle.forward(100)
    turtle.right(90)
    
    
def imbedded_drawing():
    turtle.forward(50)
    turtle.right(90)


def main():

    for counter in range(4):  # We can name counter to anything we like!
        drawLine()
        for counters in range(4):  # We can name counter to anything we like!
            imbedded_drawing()

    
    # turtle.forward(100)  # When it is run, a line will be drawn, with a cursor pointing down
    # turtle.right(90) # the pointer points left now, due to the 90 degree angle
    
    
    # turtle.forward(100)
    # turtle.right(90)
    
    
    # turtle.forward(100)
    # turtle.right(90)
    
    # turtle.forward(100)
    # turtle.right(90)
    
    
    # turtle.done()
    
    
if __name__ == "__main__":
	main()
    