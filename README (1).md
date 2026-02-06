# SDEV 1001 - Assignment 1

This assignment covers introduction to programming, pushing code changes to GitHub and making decisions.


## Instructions

### Part 1: Simple Dice Game

You will create a simple betting game. Prompt the user for the bet amount, and prompt for a guess of a number rolled on a 6 sided die. If the guess is correct
they win if not they lose. More details below.

1. First ask if the user wants to play based on a `"yes"` or `"no"` input.
    - If user enters `"yes"` then continue (see info in 2. and 3.)
    - If the user enters `"no"` display `"Okay you don't want to play. Game Over."`
    - If the user enters anything else display `"Invalid input. Game Over."`

2. If user plays the game prompt for two inputs and immediately convert them to integers.
    - betting amount prompt, use the following string in your code: `"How much would you like to bet? (enter an integer less than or equal to 100) "`
    - guess number rolled prompt,  `"A six sided die will be rolled. Guess the number? (1-6) 2"`
    - Note: the die roll result is given to you as the variable `first_dice_roll` in the file.

3. The game only works when the bet is **less than or equal to 100**, if they **guess the die roll then they will win two times the amount of the bet**. If they lose they will lose the bet. Use the following strings in the program. (Example strings for a bet too much and for a bet of 50)
    - "Sorry, bet is too much. Game Over."
    - "Congratulations, you won 100"
    - "Sorry, you lost 50"

Note: Refer to the `Desired output` section

Note: Complete the `Analysis` part below by replacing `"Your Answer Here"` with your answer.

#### Analysis
What error occurs if you put the string `"five"` when you prompt the user for the bet and guess

Error Type that occurs: ValueError

Why Does it occur? Because Python cannot convert a string like "five" into an integer using int().

#### Desired Output

- user doesn't want to play the game.
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) no
Okay you don't want to play. Game Over.
```
- invalid input
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) y
Invalid input. Game Over.
```
- valid bet and incorrect guess
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 2
Sorry, you lost 50
```
- valid bet, and correct guess
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 1
Congratulations, you won 100
```
- invalid bet
```
$ python simple_dice_game.py
Welcome to the Dice Game
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal 100) 9001
Sorry, bet is too much. Game Over.
```

### Part 2: Dice Game Double play

The modified program will allow the user the option of playing twice.

1. Copy your code from `simple_dice_game.py` and put in the proper location of `dice_game_double_play.py` i.e. below the comment `# YOUR CODE BELOW`

2. Keep track of the winnings or losses from the Part 1.  (i.e. positive if the user won and negative if they lost.)

3. Prompt to see if the user wants to play again.
    - The bet is automatically double the bet from previous game (whether they won or not).
    - Use the following string (displayed for a bet of 50 originally) `"We can play again if you bet 100? (yes/no) "`
    - If they don't want to bet and want to stop playing display `"Fine! You won 100"`

4. If they want to play prompt them for a guess and immediately convert it to an integer.
    - Use the following string `"You know the game, guess the die number? (1-6) "`
    - Note: the die roll for the 2nd guess is given to you as the variable `second_dice_roll` in the file.

5. Handle the various outcomes of playing twice
   - Betting results of two games are: (Win, Win)(Lose, Win)(Lose, Lose)(Win, Lose)
   - Use the following display prompts (for a bet of 50):
     - `"Lucky you, two wins! Total winnings 300"`
     - `"Lost first bet, but won second bet! Total winnings 150"`
     - `"You lost both bets. Total loss 150"`
     - `"Won first bet, but lost second bet. You are even."`
     

#### Desired Output

- won first, didn't want to play the double
```
Welcome to the Dice Game, you can choose to play twice!
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 1
Congratulations, you won 100

We can play again if you bet 100? (yes/no) no
Fine! You won 100
```
- lost first, didn't want to play the double
```
Welcome to the Dice Game, you can choose to play twice!
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 1
You lost 50

We can play again if you bet 100? (yes/no) no
Fine! You lost 50
```
- won original bet, won second bet
```
Welcome to the Dice Game, you can choose to play twice!
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 1
Congratulations, you won 100

We can play again if you bet 100? (yes/no) yes
You know the game, guess the die number? (1-6) 1
Lucky you, two wins! Total winnings 300
```
- won first, lost second
```
Welcome to the Dice Game, you can choose to play twice!
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 1
Congratulations, you won 100

We can play again if you bet 100? (yes/no) yes
You know the game, guess the die number? (1-6) 2
Won first bet, but lost second bet. You are even.
```
- lost first, won second
```
Welcome to the Dice Game, you can choose to play twice!
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal 100) 100
If you guess correctly you win 200
A six sided die will be rolled. Guess the number? (1-6) 2
You lost 100

We can play again if you bet 200? (yes/no) yes
You know the game, guess the die number? (1-6) 1
Lost first bet, but won second bet! Total winnings 300
```
- lost both bets
```
Welcome to the Dice Game, you can choose to play twice!
Would you like to play? (yes/no) yes
How much would you like to bet? (enter an integer less than or equal to 100) 50
If you guess correctly you win 100
A six sided die will be rolled. Guess the number? (1-6) 2
You lost 50

We can play again if you bet 100? (yes/no) yes
You know the game, guess the die number? (1-6) 2
You lost both bets. Total loss 150
```


#### Desired Output

## Marking Key

#### 2 points - Parts 1 - Analysis

| Level             | Feedback Description                         |
| ----------------- | -------------------------------------------- |
| Correct           | Values are correct. Explanation Makes sense. |
| Partially Correct | One of the two answers makes sense.          |
| Missing/Incorrect | Not Correct, no marks                        |

#### 6 points - Part 1 - Code

| Level                | Feedback Description                                                                   |
| -------------------- | -------------------------------------------------------------------------------------- |
| Excellent            | Code looks like desirable output, code is formatted correctly.                         |
| Satisfactory         | Code looks like desirable output but code formatted incorrectly.                       |
| Incomplete/Incorrect | Code does not behave like desirable output but the program works somewhat.             |
| Poor                 | Code does not behave like desirable output don't, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                                                 |

#### 8 Points - Part 2 - Code

| Level                | Feedback Description                                                                               |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| Excellent            | Code looks like desirable output, code is formatted correctly.                                     |
| Satisfactory         | Code looks like desirable output but code formatted incorrectly one test may not for this section. |
| Incomplete/Incorrect | Code does not behave like desirable output but the program works somewhat.                         |
| Poor                 | Code does not behave like desirable output don't, program does not use best practices.             |
| Missing              | Broken/Missing/Way Off                                                                             |

## Academic Integrity Note.

You must demonstrate incremental development of your solution. This means that you must begin work on your solution as soon as possible and commit often to the assignment repository. Each commit must demonstrate functional improvements to the solution. Failure to show incremental work during the assignment period will result in loss of marks of up to 20%.

Additionally, you are encouraged to use external resources to help you learn what is needed for the assignment. However, if you submit code that differs greatly from what was demonstrated in class it must be documented (e.g. comments, citations, etc.) and you may be asked to provide a verbal explanation of how the code works to your instructor. Failure to explain any code you submitted will be considered as potential evidence of academic misconduct and may trigger an investigation, potentially resulting in further consequences.