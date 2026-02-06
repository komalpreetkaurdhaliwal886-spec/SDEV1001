import random

# first dice roll is an int
first_dice_roll = random.randint(1,6)

# second dice roll is an int
second_dice_roll = random.randint(1,6)

# YOUR CODE BELOW
print("Welcome to the Dice Game, you can choose to play twice!")

play = input("Would you like to play? (yes/no) ")

total = 0

if play == "yes":
    bet = int(input("How much would you like to bet? (enter an integer less than or equal to 100) "))

    if bet > 100:
        print("Sorry, bet is too much. Game Over.")
    else:
        print(f"If you guess correctly you win {bet * 2}")
        guess = int(input("A six sided die will be rolled. Guess the number? (1-6) "))

        if guess == first_dice_roll:
            print(f"Congratulations, you won {bet * 2}")
            total += bet * 2
            first_win = True
        else:
            print(f"You lost {bet}")
            total -= bet
            first_win = False

        play_again = input(f"\nWe can play again if you bet {bet * 2}? (yes/no) ")

        if play_again == "no":
            if total > 0:
                print(f"Fine! You won {total}")
            else:
                print(f"Fine! You lost {abs(total)}")

        elif play_again == "yes":
            bet = bet * 2
            guess2 = int(input("You know the game, guess the die number? (1-6) "))

            if guess2 == second_dice_roll:
                total += bet * 2
                second_win = True
            else:
                total -= bet
                second_win = False

            if first_win and second_win:
                print(f"Lucky you, two wins! Total winnings {total}")
            elif not first_win and second_win:
                print(f"Lost first bet, but won second bet! Total winnings {total}")
            elif not first_win and not second_win:
                print(f"You lost both bets. Total loss {abs(total)}")
            else:
                print("Won first bet, but lost second bet. You are even.")

elif play == "no":
    print("Okay you don't want to play. Game Over.")

else:
    print("Invalid input. Game Over.")
