'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))#making int from user input
remaining_years = 100 - age #storing result in a variable
DOcentury = str (2019 + int(remaining_years)) #storing result in a variable
print("You will become 100 years old in the year" + " " + DOcentury)

#extras
num = int(input("Enter a number less than 10: "))
for x in (range(0, num)):
 print("You will become 100 years old in the year" + " " + DOcentury)