# Define function rng_number
def rng_number():
    
    # Intro
    print("Hello! I am a random number generator")
    
    # Loop runs infinitely unless option is 2. End
    while (1):
        
        # User picks option
        print("\nWhat would you like to do?\n1.Generate random number\n2.End")
        a = input("Pick your choice number\n")
        
        # Random number generator
        if a == "1":
            
            # Define function number
            def number():
                flag = 0
                
                # Enter lower and upper limits
                try:
                    b = int(input("\nEnter Lower Limit\n"))
                    c = int(input("Enter Upper Limit\n"))
                    import random
                    print("\nA random number from range is : ",random.randrange(b,c))
                except:
                    print("\nAn error occured!")
                    flag = 1
                while flag:
                    try:
                        b = int(input("\nEnter Valid Lower Limit\n"))
                        c = int(input("Enter Valid Upper Limit\n"))
                        import random
                        print("\nA random number from range is : ",random.randrange(b,c))
                        flag = 0
                    except:
                        print("\nAn error occured again!")
                        flag = 1
                        
                # Generate again or not
                while(1):
                    d = input("\nDo You Want to Generate More Numbers?\nType 1 if yes\nType 2 if no\n")
                    while d == "1":
                        print("\nA random number from range is : ",random.randrange(b,c))
                        d = input("\nDo You Want to Generate More Numbers?\nType 1 if yes\nType 2 if no\n")
                    if d == "2":
                        return()
                        
                    # Invalid option
                    else:
                        print("\nThat's not a valid option!")
                        
            # Call function number
            number()
            
        # End
        elif a == "2":
            print("\nThankyou For Using Random Number generator!")
            return()
        # Invalid option
        else:
            print("\nThat's not a valid option!")
            
# Call function rng_number 
rng_number()
