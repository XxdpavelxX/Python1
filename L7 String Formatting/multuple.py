Objective:
This project tests your ability to handle string formatting.

Create a new Python source file named multuple.py.
Write a program that takes as data a tuple of two-element tuples, such as ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98)).  This and/or similar data should be hard-coded (no need for user input).
Loop over the tuple and print out the results of multiplying the two numbers together, and use string formatting to display nicely.
Below is an example of output from running the program with the sample data above. Preserve the spacing, assuming that no input number is greater than 99.

   1 =  1 x  1
   4 =  2 x  2
 156 = 12 x 13
  16 =  4 x  4
9702 = 99 x 98

###################################################################################################################################################################################################################

data=[(1,1),(2,2),(12,13),(4,4),(99,98)]
for count in range(0,5):	
	x,y=data[count]

    	
for values in data:
	formated_values = values[0]*values[1],values[0],values[1]	
	print ("{0[0]:>10d} = {0[1]:2d} x {0[2]:2d}".format(formated_values))
