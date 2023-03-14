
def statement_generator(statement, decoration, side_text):

    sides = decoration * 3
    greeting = "{} {} {}".format(sides, statement, sides)

    sides_length = side_text * len(greeting)

    print(sides_length)
    print(greeting)
    print(sides_length)

    return ""

# Main routine goes here


statement_generator("Welcome to the Lucky Unicorn Game", "*", "-")
print()
statement_generator("Congratulations you got a Unicorn", "!", "-")
