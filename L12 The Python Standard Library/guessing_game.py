Objective:
This project tests your ability to use modules and imports.

Create a new Python source file named guessing_game.py.
Import the random module.
Use the help() function on the random module to determine how to generate a random number between 1 and 99 inclusive.
Generate a random number between 1 and 99 and store it in a variable.
Use a while loop to accept integers from the user (don't forget--you'll need to convert the input string).
Compare the user's guess with the saved random number.
If the user successfully guesses the target number, inform them and terminate the program.
Otherwise, inform the user whether their guess was higher or lower than the saved random number and loop around to allow them to guess again.
Below is an example of possible output from running the program.

Guess a number: 25
Too low
Guess a number: 75
Too high
Guess a number: 60
Too high
Guess a number: 45
Too low
Guess a number: 53
You guessed it!

#####################################################################################################################################################################################################################3

import random
value = random.randint(1,99)
guess = 0

while guess != value:
	guess = int(input('Guess a number: '))
	if guess>value:
		print ('Too high')
	if guess<value:
		print ('Too low')
print ('You guessed it!')
