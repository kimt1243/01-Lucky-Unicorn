

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


# Main Routine goes here...
show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))

show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say no, output 'display instructions'
    # If they say yes, output 'program continues'
    if show_instructions == "yes":
        print("program continues")
        print("You chose yes")

    elif show_instructions == "no":
        print("display instructions")
        print("You chose no")


