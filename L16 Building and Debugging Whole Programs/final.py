Objective:
This project tests your basic ability to build a complex program from the relatively limited amounts of Python you already know.

Create a new Python source file named final.py.
Write a program that meets the following specifications:
Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
The program reads all the input, splitting it up into words, and computes the length of each word. Punctuation marks should not be included as a part of the word, so "it's" should be counted as a three-character word, and "final." should be counted as a five-character word.
The example text includes a "word" of zero length (the "&"); your solution should handle this.
When all input has been processed ,the program should print a table showing the word count for each of the word lengths that has been encountered. Your tutor will run your code against several standardized inputs to verify the correctness of your logic.
Below is an example of output from running the program using the text in this file as input. (The text is the United States Declaration of Independence). Copy the text in this file. Create a new file and paste the copied text into it, and save it as declaration.txt in the same folder where your final.py program is located. 

Here is some sample output.

 Length Count
 1 16
 2 267
 3 267
 4 169
 5 140
 6 112
 7 99
 8 68
 9 61
 10 56
 11 35
 12 13
 13 9
 14 7
 15 2
Also, you will probably want to define a function to return the length of each word, since the built-in len() function will include punctuation characters.

##############################################################################################################################################################################################################################################################################################################################################################

import math
import sys

punct = "'.?,!:;-()[]/{}><&"    
print "This is the name of the script: ", sys.argv[0]
f_read=open(sys.argv[1],'r').readlines()                     
f_words=[]                                                          

for line in f_read:
    for word in line.split():
        for p in punct:
            if p in word:
                word=word.replace(p,"")
        f_words.append(word.lower())                                

d_words={}                                                         
while len(f_words):
    counter = 1
    c_word  = f_words.pop()                                        
    c_word_len = len(c_word)     	
    if d_words.get(c_word_len):                                    
        d_words[c_word_len]+=counter                                     
    else:       
        d_words[c_word_len]=1                                     

print('Length Count')
for k,v in d_words.items():
	if k > 0:
		print ("{0} {1}".format(k,v))
