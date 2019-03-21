'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''
  
while True:  
 player1 = str(input("Enter rock paper or scissors: "))
 player2 = str(input("Enter rock paper or scissors: "))
 options_dict = {"rock": 1, "paper": 2, "scissors": 3}

 value1 = options_dict.get(player1)
 value2 = options_dict.get(player2)
 diff = value1-value2

 if diff in [-1, 2]:
  print("Player1 won!")
  ques = str(input("Do you want to play another game? Yes or No?"))
  if ques == "Yes":
   continue
  else:
   print("End of game!")
   break
 elif diff in [1, -2]:
  print("Player2 won!")
  ques = str (input("Do you want to play another game? Yes or No?"))
  if ques == "Yes":
   continue
  else:
   print("End of game!")
   break
 else:
  print("It's a tie. please try again!")
  
'''
Alternative code
player1 = input("Enter rock paper or scissors: ")
player2 = input("Enter rock paper or scissors: ")
if player1 == player2:
 print("Its a tie! try again")
elif player1 == "rock" and player2 == "scissors":
 print ("player1" + " wins")
elif player1 == "scissors" and player2 == "paper":
 print ("player1" + " wins")
...
'''