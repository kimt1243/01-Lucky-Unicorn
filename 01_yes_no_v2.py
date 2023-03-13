
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game"
            " before? ").lower()

    # If they say no, output 'display instructions'
    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")
        print("You chose yes")

    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")
        print("You chose no")

    elif show_instructions == "xxx":
        print("You chose xxx")
    else:
        print("Please answer yes / no")

