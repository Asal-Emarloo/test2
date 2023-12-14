import random
computer_number=random.randint(1,6)
for i in range(15):
    user_number=int(input("Enter your number by chance: "))

    if user_number==computer_number:
        print("Excellent")
        

    elif user_number!=computer_number:
        print("try again")
        
        
    elif user_number==6:
        import random
        for i in range(1):
            print("Well done")