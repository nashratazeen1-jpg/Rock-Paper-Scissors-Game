import time
import random
co_score = 0
user_score = 0
print("\n")
time.sleep(2)
print("\t\t\t\t\t>>>>>>>>>> -------------------------------------------- <<<<<<<<<<")
print("\t\t\t\t\t>>>>>>>>>> WELCOME TO NASHRA'S ROCK,PAPER,SCISSORS GAME <<<<<<<<<<")
print("\t\t\t\t\t>>>>>>>>>> -------------------------------------------- <<<<<<<<<<\n")
time.sleep(1)
print(" 🕹️  HEY user!. Let's play the Game with COMPUTER!!..🎮\n")
time.sleep(3)

print("Let me Show you the Options First..>>>📃\n")
time.sleep(2)
Options = [ "r ✊ ", "p 🖐️ ", "s ✌️ " ]
print(Options)
time.sleep(2)
for i in range(5):
    user = input("\nUser..Enter your Choice ('r'/'p'/'s'): ")
    match user:
        case 'r':
            print("\nYou Entered option - 'r ✊ '..., Now Computer's Turn\n")
            time.sleep(2)
            print("Computer is Thinking", end=" ")
            for i in range(3):
                print(".", end=" ")
                time.sleep(0.7)
            computer = random.choice(Options)
            print(f"\nComputer's Choice is: {computer}\n")
            time.sleep(3)
            if ( computer == 'r ✊ ' ):
                print("Oo!.it's A Tie..😑")
                time.sleep(2)
                print("===================================================")
                time.sleep(2)
            elif ( computer == 'p 🖐️ ' ):
                print("Computer Wins!..😁")
                time.sleep(2)
                co_score += 1
                print(f"Co_Score:{co_score}")
                print("====================================================")
                time.sleep(2)
            elif ( computer == 's ✌️ ' ):
                print("User Wins!..😉")
                time.sleep(2)
                user_score += 1
                print(f"User_Score: {user_score}")
                print("====================================================")
                time.sleep(2)
            
        case 'p':
            print("You Entered option - 'p 🖐️ '..., Now Computer's Turn\n")
            time.sleep(2)
            print("Computer is Thinking", end=" ")
            for i in range(3):
                print(".", end=" ", flush=True)
                time.sleep(0.7)
            computer = random.choice(Options)
            print(f"\nComputer's Choice is: {computer}\n")
            time.sleep(3)
            if ( computer == 'p 🖐️ ' ):
                print("Oo!.it's A Tie..😑")
                time.sleep(2)
                print("===================================================")
                time.sleep(2)
            elif ( computer == 'r ✊ ' ):
                print("User Wins!..😉")
                time.sleep(2)
                user_score += 1
                print(f"User_Score: {user_score}")
                print("===================================================")
                time.sleep(2)
            elif ( computer == 's ✌️ ' ):
                time.sleep(2)
                print("Computer Wins!..😁")
                co_score += 1
                print(f"Co_Score:{co_score}")
                time.sleep(2)
                print("===================================================")
                time.sleep(2)

        case 's':
            print("You Entered option - 's ✌️ ' ...,Now Computer's Turn\n")
            time.sleep(2)
            print("Computer is Thinking", end=" ")
            for i in range(3):
                print(".", end=" ")
                time.sleep(0.7)
            computer = random.choice(Options)
            print(f"\nComputer's Choice is: {computer}\n")
            time.sleep(3)
            if ( computer == 's ✌️ ' ):
                print("Oo!.it's A Tie..😑")
                time.sleep(2)
                print("===================================================")
                time.sleep(2)
            elif ( computer == 'r ✊ ' ):
                print("Computer Wins!..😁")
                time.sleep(2)
                co_score += 1
                print(f"Co_Score:{co_score}")
                print("===================================================")
                time.sleep(2)
            elif ( computer == 'p 🖐️ ' ):
                print("User Wins!..😉")
                time.sleep(2)
                user_score += 1
                print(f"User_Score: {user_score}")
                print("===================================================")
                time.sleep(2)
        case _:
            print("\nYou Entered Invalid Option")
            print(f"Choose between: {Options}")
            
time.sleep(2)
print(f"\nTotal Co_Score:{co_score}/5")
print(f"Total User_Score:{user_score}/5\n")
time.sleep(2)
if ( co_score > user_score ):
    print(" ✨😎 Computer Wins The R,P,S Game!!..🏆")
elif ( user_score > co_score ):
    print("✨🤩 User Wins The R,P,S Game!!..🏆")
elif ( co_score == user_score ):
    print("😓 Oops!..It is A Tie, Try Again!,...😑")
time.sleep(2)

print("\n\t\t\t\t\t\t\t\t\t>>>>> ------- <<<<<")
print("\t\t\t\t\t\t\t\t\t>>>>> THE END <<<<<")
print("\t\t\t\t\t\t\t\t\t>>>>> ------- <<<<<")
