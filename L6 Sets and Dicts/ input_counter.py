Objective:
This project tests your ability to use sets and dicts, and your ability to follow an algorithm (recipe) exactly.

Create a new Python source file named input_counter.py.
Write a program that creates an empty set and dict.
Write a while loop that repeatedly creates a list of words from a line of input from the user.
Loop through the list of words and add each one to the set. If the set increases in size (indicating this word has not been processed before), add the word to the dict as a key with the value being the new length of the set.
Using another loop, display the list of words in the dict along with their value, which represents the order in which they were discovered by the program.
If the user presses Enter without any text, print Finished and exit.
Below is an example of output from running the program.

Enter text: how now brown cow
how 1
now 2
cow 4
brown 3
Enter text: the cow jumped over the moon
brown 3
cow 4
jumped 6
over 7
moon 8
how 1
the 5
now 2
Enter text:
Finished

#########################################################################################################################################################################################################################################################

Solution #1
freq= {}
wordSet = set()
while True:
	text=input("Write sentence: ")
	if not text:
		print ("Finished")
		break

	else:
        	
		for punc in (".,?;!"):
			text = text.replace(punc, "")
		for word in text.lower().split():
			if word not in wordSet:
				wordSet.add(word)
				Count =len(wordSet)
				freq[word] = Count
        
	for words,values in freq.items():
		print (words, values)

#########################################################################################################################################################################################################################################################


Solution #2
import string  # not required

unique = set()
first_seen = {}

while True:

    line = input("Enter text: ")
    if not line:
        print('Finished')
        break

    # Removes punctuation from words (extra feature)
    for punc in string.punctuation:  # canned string of all punc marks
        line = line.replace(punc, "")  

    words = line.split()

    for word in words:
        size = len(unique)
        unique.add(word)
        if len(unique) > size:
            first_seen[word] = len(unique)

    for word in first_seen:
        print (word, first_seen[word])
