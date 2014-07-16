Objective:
This project tests your ability to use file objects.

Create a new Python source file named inputter.py.
Write a program that uses a while loop to accept input from the user (if the user presses Enter, exit the program).
Save the input to a file, then print it.
Upon starting, the program will display any previous content of the file.
Below is an example of possible output from a first run of the program.

Enter text: Python is fun.
Python is fun.
Enter text: O'Reilly makes good classes.
Python is fun.O'Reilly makes good classes.
Enter text:
Below is an example of possible output from a second run of the program.

Python is fun.O'Reilly makes good classes.
Enter text: The file is saving correctly
Python is fun.O'Reilly makes good classes.The file is saving correctly
Enter text:

#############################################################################################################################################################################################################

z = 'anything'
# if file not exist
j = open("input_data2.txt", 'a')
j.close()
while z != '':
	f = open("input_data2.txt", 'r')
	line = f.read()	
	print (line)
	f.close()
	f = open("input_data2.txt",'a')
	z = input("Enter text: ")	
	f.write(z)
	f.close()
