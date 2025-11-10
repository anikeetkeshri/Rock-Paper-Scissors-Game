import random

print("Welcome to the Rock Paper Scissors Game! 👊🏻✋🏻✌🏻  | First to 3 points wins!")

while True:
    userscore = 0
    compscore = 0

    while userscore < 3 and compscore < 3:
        compchoice = random.choice(["rock", "paper", "scissor"]).lower()
        userchoice = input("Your action (rock, paper, scissor): ").lower().strip()

        if userchoice not in ["rock", "paper", "scissor"]:
            print("❌ Invalid choice, try again!")
            continue

        print(f"You chose {userchoice}, computer chose {compchoice}.")

        if compchoice == userchoice:
            print("It's a tie!")
        elif compchoice == "rock" and userchoice == "paper":
            userscore += 1
            print("You win this round! 🎉")
        elif compchoice == "rock" and userchoice == "scissor":
            compscore += 1
            print("Computer wins this round!")
        elif compchoice == "paper" and userchoice == "scissor":
            userscore += 1
            print("You win this round! 🎉")
        elif compchoice == "paper" and userchoice == "rock":
            compscore += 1
            print("Computer wins this round!")
        elif compchoice == "scissor" and userchoice == "rock":
            userscore += 1
            print("You win this round! 🎉")
        else:
            compscore += 1
            print("Computer wins this round!")

        print(f"🏁 Score: You {userscore} - Computer {compscore}\n")

    if userscore == 3:
        print("🎊 You won the game! 🥳")
    else:
        print("💻 Computer wins the game! ☹️")

    replay = input("Play again? (yes/no): ").lower().strip()
    if replay != "yes":
        print("Thanks for playing! 👋 Goodbye!")
        break