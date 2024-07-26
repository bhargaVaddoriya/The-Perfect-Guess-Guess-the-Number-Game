#Number Guessing Game Objectives:
import random
from art import logo


# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(logo)
print("\nWelcome To Number Guess Game")
print("\n I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt =0
if level == "easy":
  attempt = 10
elif level == "hard":
  attempt = 5
else:
  print("incoorect input")

goal_number = random.randint(1,100)
is_game = False
print(f"passt number is {goal_number} ")
while not is_game:
  guessing_number = int(input(f"Guess a number. Remember You have left {attempt} attempt : "))
   
  if guessing_number < goal_number:
    print("To Low")
    attempt -= 1
  elif guessing_number == goal_number:
    print("Yes You win a game") 
    is_game = True
  else:
    print("To High")
  
  if attempt == 0:
    print("You Lose a game")
    is_game = True