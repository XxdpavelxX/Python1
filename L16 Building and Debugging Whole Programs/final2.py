Objective:
This project builds on the previous one.

Copy your final.py file to a file named final2.py, then modify final2.py to print a histogram of the word lengths. A histogram is a chart with columns whose heights correspond to the data they represent.

Below is an example of possible output from running the updated program with the declaration.txt file:

 
 Length    Count
       1       16
       2      267
       3      267
       4      169
       5      140
       6      112
       7       99
       8       68
       9       61
      10       56
      11       35
      12       13
      13        9
      14        7
      15        2

  400 -|                                             
       |                                             
       |                                             
       |                                             
       |                                             
  300 -|                                             
       |                                             
       |   ******                                    
       |   ******                                    
       |   ******                                    
  200 -|   ******                                    
       |   ******                                    
       |   *********                                 
       |   ************                              
       |   ************                              
  100 -|   ***************                           
       |   ******************                        
       |   ************************                  
       |   ***************************               
       |   ******************************            
    0 -+-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-
       | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

#########################################################################################################################################################################################################

'''
Created on Jul 3, 2014
@author: pdvorkin
Written with Python 3

Python1:Final Project
Analysis of files via Histogram Creation 
'''
import sys

def counter():
	#"""Counts the characters in every word in declaration.txt. Can substitute declaration.txt with another word document."""
	
	text = sys.argv[1]
	doc_file = open(text)
	f_read = doc_file.readlines()
	punct = "'.?,!:;-()~,`[]/{}><&,=%*@#$^_+|\""  
	initial_word_counts = []
     
	for line in f_read:
		d_words = line.split()
		for c_word in d_words:
			char_count = 0
			for char in c_word: #loop used to count characters in words
				if char not in punct: 
					char_count += 1
				else:                   
					continue
			if char_count != 0: #makes sure not count 0 characters.
				initial_word_counts.append(char_count)
            
	doc_file.close() 
    
	var_counts = sorted(list(set(initial_word_counts)))
	len_reps = {}
	for val in var_counts:
		val_reps = 0
		for raw_val in initial_word_counts:
			if raw_val == val:
				val_reps += 1
		len_reps.update({val: val_reps})
     
	#"""Prints the number of characters as the key( on left side), 
	#and the number of words that have that many characters as the value (on the right)"""
	
	for key in sorted(len_reps.keys()):
		print('{0} {1}'.format(key, len_reps[key]))        
	print('\n')

	#"""Prints a histogram from the data."""
	b_range = range(400, 0, -10)
	y = 400
	x = 1
	row = ""
	          
		#for key in histogram_values.keys():
		#	if count == histogram_values[key] or histogram_values[key] > count: 
		#		column_num += '***'
	while y > 0:
		while x < 16:
			if x not in len_reps.keys():
				x = x +1
				row += "   "
				continue
			if len_reps.get(x) > y:
				row += " * "
			else:
				row += "   "
			x += 1
		if (y % 100) == 0:
			print("  " + str(y) + " -|{0}".format(row))
		else:
			print("       |{0}".format(row))
		y -= 10
		x = 1
		row = ""	
        

	print("    0 -+-+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+-")   # prints x-axis
	print("       | 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16")
    


if __name__ == '__main__':   #Runs if this program is main program.
	try:
		counter()
	except UnicodeDecodeError:
		print ("""Oops! This program currently isn't compatible with that type of file or your file has non-English characters.
		Compatible file types include: .txt and .py, please convert your file to one of the compatible types 
		and make sure all characters are English""")
	except FileNotFoundError:
		print ("That file is not in the current directory, please make sure your file is in the same directory as this program")
