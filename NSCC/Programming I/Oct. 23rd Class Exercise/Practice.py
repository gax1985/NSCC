def ShowMessage(in_name):  # we create in_name parameter that
                        # is comming into the function
    print("Hello, {in_name}")


# Function is going to receive a parameter, 



def main():
    print("Hi")  #  ----> Indentation indicates that this is 
                 #        part of this function.
    name = "Delano"
    ShowMessage(name)                
    ShowMessage("Delano")  # ---> We call this function
    
    #It assumes "Delano" = in_name
    
    
    # When debugging a function, we are clicking on StepInto
    #It goes to inside the function, and debugs the function with the 
    #parameter that has been passed. 
   
   # If we step over it, we are back at the main function, and 
   # we have the variable name again
   
   # 1. Create a function
   # 2. Use the debugger to see what is happening
   
   
   # If we are creating a function, it would be outside of the 
   # Main block . If we define a function inside another function,
   # it would work inside the function we created it in 
   
   
   # If we want to do something different, we can change that : 
   
def showMessage(in_name, in_greeting):
    print(f"Hello {in_name}, {in_greeting}") #if we hover over the parameter in_greeting, we see the parameter
    
# The order that the parameter are used in does not matter. Every time the function is called, the first parameter is stored in_name, and the second in in_greeting
def main():
    showMessage(name, "Hi")
    showMessage("John", "Hello")
    showMessage("Jane", "Goodbye")
    showMessage("Bye", "Mary")
    
    
    # if passing the name first, and greeting second, keep in mind how it will work in the function.
    
    
    # We should not use a function just to print something. The function should get the string to be outputted,
    # and then, we would : 
    # "return message" . Our function is receiving parameters, working with them, 
    
    
    
def showMessage(in_name, in_greeting):
    message = f"{in_greeting}, {in_name}!"
    return message

def main():
name = "Delano"
print(showMessage(name, "Hi"))
message = showMessage("John", "Hello")
print(message)
showMessage("Jane", "Goodbye")
    
    

if __name__ == "__main__"
    main()