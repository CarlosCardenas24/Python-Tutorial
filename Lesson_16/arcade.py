from rps import rps
from guess_number import guessnumber
import sys


def arcadegame(name="PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(f"\nPlease choose a game: \n1 = Rock Paper Scissors \n2 = Guess My Number \n\nOr press \"X\" to exit the Arcade\n")

        if playerchoice not in ["1", "2", "x", "X"]:
            print(f"{name}, please enter 1, 2, or x.")
            return arcadegame(name)
        
        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guessnumber(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experiecne"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    arcadegame(args.name)