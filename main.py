#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random
from replit import clear
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.


def play_game():
  number_to_guess = random.randint(1, 100)
  print(number_to_guess)
  level = input('Choose a level. type "easy" or "hard" ').lower()
  if level == 'easy':
   attempts = 10
  else:
   attempts = 5
  def compare(number_to_guess, guess):
    """This takes the number to guess and the guess and compares them """
    if guess > number_to_guess:
      print('Too high. \n Guess again')
    elif guess < number_to_guess:
      print('Too low. \n Guess again')
    else:
      print(f'You got it! The answer was {number_to_guess}') 
  is_game_over = False
  while not is_game_over:
    print(f'You have {attempts} attempts remaining to guess the number.')
    attempts -=1
    guess = int(input('Make a guess: '))
    compare(number_to_guess, guess)
    if attempts == 0 and guess != number_to_guess:
      is_game_over = True
      print(f'You did not manage to guess the correct number after {attempts} attempts')
    elif guess == number_to_guess:
      is_game_over = True
play_game()    
while input('Do you want to guess another number? Type "yes" or "no" ').lower() == 'yes':
  clear()
  play_game()

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

