#While Loops allow you to execute until a
#particular condition is true

def main():
    
    
    answer = 0

    while answer !=4:

        answer = int(input("What is 2 + 2? "))

    print(f"YES!!! 2 + 2 = {answer}")

if __name__ == "__main__":
    main()