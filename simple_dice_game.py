import random
#TEST
# first dice roll is an int
first_dice_roll = random.randint(1,6)

# DO NOT COPY ABOVE THIS LINE FOR PART 2

# YOUR CODE BELOW
print("Welcome to the Dice Game")

play = input("Would you like to play? (yes/no) ")

if play == "yes":
    bet = int(input("How much would you like to bet? (enter an integer less than or equal to 100) "))

    if bet > 100:
        print("Sorry, bet is too much. Game Over.")
    else:
        print(f"If you guess correctly you win {bet * 2}")
        guess = int(input("A six sided die will be rolled. Guess the number? (1-6) "))

        if guess == first_dice_roll:
            print(f"Congratulations, you won {bet * 2}")
        else:
            print(f"Sorry, you lost {bet}")

elif play == "no":
    print("Okay you don't want to play. Game Over.")

else:
    print("Invalid input. Game Over.")

