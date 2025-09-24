from random import randint
while True:

    num = randint(1, 100)
    choice = 10

    while choice >= 0:
        try:
            user = int(input("Enter Guess: "))
        
            if user == num:
                print("Guessed it!!")
                break
            else:
                choice -= 1
                if user > num:
                    print("High!")
                else:
                    print("Low!")
                print(f"Choices left: {choice}")
    
        except ValueError:
            print("Invalid Input")

    playAgain = input("Want to play again (Yes/No): ").lower().strip()
    if playAgain == "no":
        break
