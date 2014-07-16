Objective:
This project tests your ability to use sequences.

Create a new Python source file named word_list.py.
Make the program read a string from the user and create a list of words from the input.
Create two lists, one containing the words that contain at least one upper-case letter and one of the words that don't contain any upper-case letters.
Use a single for loop to print out the words with upper-case letters in them, followed by the words with no upper-case letters in them, one word per line.
Verify that your program works correctly, and hand it in.
Below is an example of output from running the program.

Input your text: Python and Perl are both programming languages
Python
Perl
and
are
both
programming
languages


#############################################################################################################################################################################

quote = input("Please type your text here: ")
words = quote.split()
UC = []
LC=[]

for word in words:
	isUpperCaseExist=0
	for letter in word:
		if letter.isupper():
			isUpperCaseExist=1
			break
		else:
			isUpperCaseExist=0
	if isUpperCaseExist==1:		
		UC.append(word)	
	else:
		LC.append(word)
for words in UC+LC:
	print (words)
		
