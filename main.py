import random

while True:
    choices=["R", "P", "S"]
    CPU = random.choice(choices)

    player= input("kindly pick an option, R, P, OR S: ").upper()

    
    if CPU == player:
        try:
            print(f"Player ({player}) : CPU ({CPU})")
            print("It's a tie")
        except:
            print("Oops! Error. Try again")

    elif CPU == "R":
        if player == "P":
            try:
                print(f"Player ({player}) : CPU ({CPU})")
                print("Rock smashes paper")
            except:
                print("Oops! Error. Try again")
        if player == "S":
            try:
                print(f"Player ({player}) : CPU ({CPU})")
                print("Rock beats scissors")
            except:
                print("Oops! Error. Try again")
    elif CPU == "P":
        if player == "R":
            try:
                print(f"Player ({player}) : CPU ({CPU})")
                print("Paper beats rock")
            except:
                print("Oops! Error. Try again")
        if player == "S":
            try:
                print(f"Player ({player}) : CPU ({CPU})")
                print("Paper knocks off scissors")
            except:
                print("Oops! Error. Try again")
    elif CPU == "S":
        if player == "P":
            try:
                print(f"Player ({player}) : CPU ({CPU})")
                print("Scissors beats paper")
            except:
                print("Oops! Error. Try again")
        if player == "R":
            try:
                print(f"Player ({player}) : CPU ({CPU})")
                print("Scissors rest on rock")
            except:
                print("Oops! Error. Try again")

    
        if player != choices:
         print("Oops! Error. Try again")


    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")