"""

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

"""

import random

num = random.randint(1,10)
i=0

print("Please try to guess a number between 1-10. Type exit if you want to quit.")
while True:
    c = int(input("Please provide your guess here: "))
    if num == c:
        i += 1
        print("Congrats your guess is correct. You made it in {} guesses!".format(i))
        break
    elif c > num:
        i += 1
        print("Try again! Too high!!")
    elif c < num:
        i += 1
        print("Try again. Too low!!")
    elif c.lower() == 'exit':
        i+=1
        print("You resign after {} guesses".format(i))
        break