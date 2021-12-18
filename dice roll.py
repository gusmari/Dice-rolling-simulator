from random import randint

def main ():
    print("You rolled",randint(1,6))
    repeat = input("Do you want to roll again? Type yes to roll again or no to end. \n")
    while repeat.lower() != "no" and repeat.lower() != "yes":
        print("Please type yes or no only.")
        repeat = input("Do you want to roll again? Type yes to roll again or no to end. \n")
    
    while repeat.lower() == "yes":
        print("You rolled",randint(1,6))
        repeat = input("Do you want to roll again? Type yes to roll again or no to end. \n")
        while repeat.lower() != "no" and repeat.lower() != "yes":
            print("Please type yes or no only")
            repeat = input("Do you want to roll again? Type yes to roll again or no to end. \n")

    if repeat.lower() == "no":  
            print("Thanks for playing.")
                
main()