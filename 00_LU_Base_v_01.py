import random


def statement_generator(statement, decoration, side_text):

    sides = decoration * 3
    greeting = "{} {} {}".format(sides, statement, sides)

    sides_length = side_text * len(greeting)

    print(sides_length)
    print(greeting)
    print(sides_length)

    return ""
# Functions go here...


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print()
    statement_generator("How to play", "*", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10). ")
    print()
    print("Then press <enter> to play. "
          "You will get either a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs $1 per round. Depending on your prize you might win some "
          "of the money back. Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.50 (balance decreases by $0.50)")
    print()
    print("Can you avoid the donkeys, get the unicorns and walk home with the money?")
    print()
    print("Hint: To quit while playing the game, type 'xxx' instead of pressing <enter>")
    print()
    statement_generator("Let's get Started", "=", "*")
    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10 \n"

    while True:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here...

statement_generator("Welcome to Lucky Unicorn", "*", "=")
print()
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to input
how_much = num_check("How much would you like to play with? ", 0, 10)
print("You will be spending ${} ".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
print()
while play_again == "":

    # Increase # of rounds played
    rounds_played += 1

    # Print round number
    statement_generator("*** Round #{} ***".format(rounds_played), "#", "=")

    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        decoration = "#"
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "="
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
            decoration = "*"
        balance -= 0.5
    print()
    statement_generator("You got a {}.  Your balance is ${:.2f}".
                        format(chosen, balance), decoration, decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money...")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")
    print()
if play_again == 'xxx':
    statement_generator("Results", "=", "=")
    print("Final balance ${} ".format(balance))
    print("Thank you for playing Lucky Unicorn!")

