import random

# main routine goes here
tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

# Testing loop to generate 20 tokens
for item in range(0, 20):
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "Horse" or chosen == "Zebra":
        balance -= 0.5
    else:

        balance -= 1

    # output
    print("Token: {} , Balance: ${}".format(chosen, balance))

