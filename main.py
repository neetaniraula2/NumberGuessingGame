# Imports
import random
#end Imports

#generate a random number between 0 and 10
ComputerNumber = random.randint(0,10)

# this is an integer
GuessMax = 5

Win = False
Play = True

while Play == True:
  while GuessMax  > 0:
    print("Welcome to the number Guessing Game!")
    playerGuess = input("Enter a number between 0-10: " + "you have " + str(GuessMax) + "guesses")
    playerGuess = float(playerGuess)

    if (playerGuess < 0 or playerGuess > 10):
      print("Bad Input")
      break
    else:
      if playerGuess > ComputerNumber:
        print("too big")
        GuessMax = GuessMax -1
        print("You have " + str(GuessMax) + "guesses left")
      elif playerGuess < ComputerNumber:
        print("Too small")
        GuessMax = GuessMax - 1
        print("You have " + str(GuessMax) + "guesses left")
      else:
        print("Correct!")
        Win = True
        break
  if Win == True:
    print("Congratulations You won at " + str(4 - GuessMax) + " tries" )
  else:
    print("No more guesses left")
    print("The number was:" + str(ComputerNumber))
  answer = input("would you like to play again? Y/N ")

  if answer == "N" or answer =="n":
    print ("OK goodbye!")
    Play = False
  else:
    Win = False
    GuessMax = 5

        
    
        
