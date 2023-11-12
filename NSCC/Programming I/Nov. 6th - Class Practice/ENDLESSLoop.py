#While Loops allow you to execute until a
#particular condition is true

def main():
    
    
    count = 0

    while count < 100:
        
        print(count)
        #count = count + 1 (We want to repeat that after the equal sign)
        count += 1 # (We can use a count operator like * for multiplication for example)
        # It is the same as count = count + variable (if we have set that variable to a number )

        time.sleep(0.5) # To Slow it down by half a second

    print(f"The Final Count is {count}")

if __name__ == "__main__":
    main()