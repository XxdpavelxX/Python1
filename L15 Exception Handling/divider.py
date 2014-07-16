Objective:
This project tests more of your understanding of exception handling.

Create a new Python source file named divider.py.
Create a while loop, request an integer value from the user, and bind the value as an integer to a variable.
Then divide the value of 10 by your new integer and print the results.
Use a try statement followed by a series of except statements to catch ValueError and ZeroDivisionError. When those errors are caught, print response statements to the user informing them of their mistake.
Below is an example of possible output from running the program.

Dividing 10 by an integer
Provide an integer: Steve
Your input must be an integer
Provide an integer: 4
2.5
Provide an integer: 3
3.33333333333
Provide an integer: 2
5.0
Provide an integer: 1
10.0
Provide an integer: 0
Your input must not be zero (0)
Provide an integer:

#######################################################################################################################################################################################################################################################################################################################################
def div():
  while True:
	  inp = input('Input an integer here: ')
	  try:
		  print (10/int(inp))
	  except ValueError:
		  print ('Your input must be an integer')
	  except ZeroDivisionError:
		  print ('Your input must not be zero (0)')
