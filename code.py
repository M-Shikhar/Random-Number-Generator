def rng_number():
    
    print("Hello! I am a random number generator")
    while (1):
        print("\nWhat would you like to do?\n1.Generate random number\n2.End")
        a = input("Pick your choice number\n")
        if a == "1":
            def number():
                flag = 0
                try:
                    b = int(input("Enter Lower Limit\n"))
                    c = int(input("Enter Upper Limit\n"))
                    import random
                    print("A random number from range is : ",random.randrange(b,c))
                except:
                    print("An error occured!")
                    flag = 1
                while flag:
                    try:
                        b = int(input("Enter Valid Lower Limit\n"))
                        c = int(input("Enter Valid Upper Limit\n"))
                        import random
                        print("A random number from range is : ",random.randrange(b,c))
                        flag = 0
                    except:
                        print("An error occured again!")
                        flag = 1
                while(1):
                    d = input("Do You Want to Generate More Numbers?\nType 1 if yes\nType 2 if no")
                    while d == "1":
                        print("A random number from range is : ",random.randrange(b,c))
                        d = input("Do You Want to Generate More Numbers?\nType 1 if yes\nType 2 if no\n")
                    if d == "2":
                        return()
                    else:
                        print("That's not a valid option!")
            number()
        elif a == "2":
            print("Thankyou For Using Random Number generator!")
            return()
        else:
            print("That's not a valid option!")
    
rng_number()
