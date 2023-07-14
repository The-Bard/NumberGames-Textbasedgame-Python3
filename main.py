#Program introduces itself as a collection of number games. It then lists the games that it can play and asks the player to select one. Program will exit if the player enters ''.

print("""Hello, I am the Number Games program. 
I'm coded in python. 
I can play a collection of number games with you.""")

gameSelection = 1 #var for tracking game selection

def displayGames(): #function that displays names and descriptions of available games.
  gameList = {}

while gameSelection != '':
  print("Here is a list of games you can play.")
  