Objective:
This project tests more of your understanding of classes and objects.

Create a new Python source file named doggies.py.
Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the object to the dogs list.
Each time around the loop, print the current dogs list (the name and breed of each dog).
Below is an example of possible output from running the program.

Name: Snoopy
Breed: Beagle
DOGS
0. Snoopy:Beagle
****************************************
Name: Marmaduke
Breed: Great Dane
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
****************************************
Name: Rover
Breed: Mutt
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
2. Rover:Mutt
****************************************
Name:

#############################################################################################################################################################################################################################################

class Dog:
    def __init__(self,name,breed):	
        self.name = name	
        self.breed = breed		
dogs=[] 	
while True:	
    insert1 = input('Name: ').strip()	
    if not insert1:	
        print('Terminating..')
        break
    insert2 = input('Breed: ').strip()		
    object1 = Dog(insert1,insert2)	
    dogs.append(object1)	 	
    print('DOGS')	
    for i,object1 in enumerate(dogs):	
        print("{0}. {1}:{2}".format(i,object1.name,object1.breed))
    print('*'*40)
