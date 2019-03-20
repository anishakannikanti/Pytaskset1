'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''
	
num = int(input("Enter a number: "))
try:
 even_odd = num/2
 if even_odd ==int(even_odd):
  print("You have enter an even number")
 else:
  print("You have enter an odd number")
except: 
 print("You have entered a string. Please enter a number.")

