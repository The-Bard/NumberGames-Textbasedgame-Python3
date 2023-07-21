#Program introduces itself as a collection of number games. It then lists the games that it can play and asks the player to select one. Program will exit if the player enters ''. 

#Definitions for all games contained under this comment
def hilo():
  import random
  USER_SCORE = 0 
  
  #generate_number function handles the number guessing gameplay and score.
  def generate_number():
      global USER_SCORE
      random_number = random.randint(1,10)
      
      print("The number generated is: ",str(random_number))
      user_guess = int(input("Will the next number be higher (type '1') or lower (type '0')? "))
      
      while user_guess != 0 and user_guess != 1: 
          print(str(user_guess), "is an invalid input. Enter '1' for higher or '0' for lower. ")
          user_guess = int(input())
          
      second_number = random.randint(1,10)
      print("The number generated is: ",str(second_number))
      
      if second_number > random_number:
          num_comparison = 1 #1 means higher
      if second_number < random_number:
          num_comparison = 0 #0 means lower
      if second_number == random_number:
          num_comparison = 2 #tie, player default wins but receives special printout
      if num_comparison == 2:
          print("The two numbers were tied. You gain a point regardless of your guess. How lucky!")
          USER_SCORE = USER_SCORE+1
          print(str(USER_SCORE), "is your current score.")
          print()
  
      elif user_guess == num_comparison:
          print("You guessed correctly! Gain a point!")
          USER_SCORE = USER_SCORE+1
          print(str(USER_SCORE), "is your current score.")
          print()
          
      else:
          print("Sorry, you guessed incorrectly. Lose a point.")
          USER_SCORE = USER_SCORE-1
          print(str(USER_SCORE), "is your current score.")
          print()
  
  #main process of hi-lo game.
  print("This is the number guessing game.")
  print("I will give you number between 1 and 10 and you will guess if the next number higher of lower.")
  print("You win if you get 10 points.")
  print()
  while USER_SCORE < 10 and USER_SCORE > -3:
      generate_number()
  if USER_SCORE >= 10:
      print("Good job, you've reached a score of 10! You Win!")
  else:
      print("Oh, you've fallen to a score of negative 3. Sorry, you lose.")

#Program introduces itself and then lists games to play.
print("""Hello, I am the Number Games program. 
I'm coded in python. 
I can play a small collection of number games with you.""")

gameSelection = 1 #var for tracking game selection

def displayGames(): #function that displays names and descriptions of available games.
  gameList = {
    'HILO': 'Generate a number and then guess if the next number will be higher or lower than the first.'
  }
  for k,v in gameList.items():
    print(k, ' --> ', v)
    print('')
  
while gameSelection != '':
  print("Here is a list of games you can play:\n")
  displayGames()
  gameSelection = (input('Enter the name of the game that you want to play. \n Hit enter to exit this program.').upper()
  