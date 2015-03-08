# Peanut Butter Jelly Time!
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

peanut=67
bread=188
jelly=56


# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

sandwiches=bread/2
jellyserv=jelly/2

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

print "Goal 1" 

if bread>2 and peanut > 1 and jelly >= 2:
     print("You can make that sandwich!").format(min(bread/2,peanut))
else:
     print ("Looks like you're going hungry")

# To satisfy the second goal:
#		Continue from the first goal, and add:You can make {0} sandwiches"
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before

print ("Goal 2: Modify that program to tell you: if you can make a sandwich, how many you can make")

if bread>2 and peanut > 1 and jelly >= 2:
     print("You can make that sandwich! You can make {0} sandwiches").format(min(bread/2,peanut))
     print("Looks like you can make {0} PBJ's").format(min(peanut,jelly/2,bread/2))
else:
     print ("Looks like you're going hungry")

# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

print("Goal 3: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread")
# % means "not divisible by" eg 167 % 2 is 1, 
if bread % 2:
    print("Bread %2 is  {0} ").format(bread%2)

if bread>2 and peanut > 1 and jelly >= 2:
     print("You can make that sandwich! You can make {0} sandwiches").format(min(bread/2,peanut))
     print("Looks like you can make {0} PBJ's").format(min(peanut,jelly/2,bread/2))

if (bread % 2)==1:
    print("You have an extra slice and you could make an open faced sandwich with that extra slice.")
else:
     print ("Looks like you're going hungry")


# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

print("Goal 4: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches")

if bread>2 and peanut > 1 and jelly >= 2:
     print("You can make that sandwich! You can make {0} sandwiches").format(min(bread/2,peanut))
     print("Looks like you can make {0} PBJ's").format(min(peanut,jelly/2,bread/2))

     if (bread % 2)==1:
        print("You have an extra slice. You could make an open faced sandwich with that extra slice.")
     if bread/2>peanut:
        print ("Looks like you could use some more peanut butter.")
        if jelly>bread:
            print "And bread."
        else:
            print "And jelly."
     elif peanut >bread/2:
        print ("Looks like you could use some more bread.")
        if jelly/2>peanut:
            print "And peanut butter."
        else:
            print "And jelly."
     if peanut>jelly/2 and bread/2>=peanut:
         print "And since you don't have enough jelly, you can make {0} PB sandwiches.. you could use {1} more servings of jelly to make those real sandwiches".format(bread/2-min(peanut,jelly/2,bread/2),(peanut*2-jelly))
elif bread>1 and peanut>1 and jelly<2:
     print("Looks like you can make {0} PB's.. aand need to reevaluate your life since you've got no jelly.. and you need {0} servings of jelly").format(min(peanut,bread/2))
     if (bread % 2)==1:
        print("You have an extra slice, one has to be an open faced sandwich")
else:
     print ("Looks like you're going hungry")

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you have enough bread and peanut butter but no jelly, 
#         print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a 
#          certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches



print("Goal 5: odify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.")

if bread>2 and peanut > 1 and jelly >= 2:
     print("You can make that sandwich! You can make {0} sandwiches").format(min(bread/2,peanut))
     print("Looks like you can make {0} PBJ's").format(min(peanut,jelly/2,bread/2))

     if (bread % 2)==1:
	    print("You have an extra slice. You could make an open faced sandwich with that extra slice.")
     if bread/2>peanut:
     	print ("Looks like you could use some more peanut butter.")
     	if jelly>bread:
     		print "And bread."
        else:
        	print "And jelly."
     elif peanut >bread/2:
     	print ("Looks like you could use some more bread.")
        if jelly/2>peanut:
     		print "And peanut butter."
        else:
        	print "And jelly."
     if peanut>jelly/2 and bread/2>=peanut:
	     print "And since you don't have enough jelly, you can make {0} PB sandwiches.. you could use {1} more servings of jelly to make those real sandwiches".format(bread/2-min(peanut,jelly/2,bread/2),(peanut*2-jelly))
elif bread>1 and peanut>1 and jelly<2:
     print("Looks like you can make {0} PB's.. aand need to reevaluate your life since you've got no jelly.. and you need {0} servings of jelly").format(min(peanut,bread/2))
     if (bread % 2)==1:
	    print("You have an extra slice, one has to be an open faced sandwich")
else:
	 print ("Looks like you're going hungry")


