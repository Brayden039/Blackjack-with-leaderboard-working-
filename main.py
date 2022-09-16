import random

choice = 0
Deck = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥"]
def leaderBoardAsk():
  leadChoice = input("Would you like to be added to the leaderboard? (Y/N)  >>").upper()
  if leadChoice == "Y":
    leaderBoardName = input("What name do you want to be shown on the leaderboard? >>  ")
    print(leaderBoardName + " " + "Saved.")
    file = open("leaderBoard.txt", "r")
    Data = file.readlines()
    file.close()
    file = open("leaderBoard.txt", "w")
    Data.append(leaderBoardName + "\n")
    file.writelines(Data)
    file.close()
  elif leadChoice == "N":
    print("You would not like to be added to the leaderboard.")
  else:
    print("Please enter Y or N.")
    leaderBoardName = input("What name do you want to be shown on the leaderboard? >>  ")
def draw(n):
    cardList = []
    for count in range(n):
        c = random.choice(Deck)
        cardList.append(c)
        Deck.remove(c)
    return cardList

def showCards(Cards):
    for char in Cards:
        print(char, end=" ")
    
def value(c):
    if c[0] == "1" or c[0] == "J" or c[0] == "Q" or c[0] == "K":
        return 10
    elif c[0] == "A":
      Ace = int(input("1 or 11 for ace: "))
      while Ace != 1 and Ace != 11:
        print("Ace must be equal to 1 or 11.")
        Ace = int(input("1 or 11 for ace: "))
        if Ace == 1 or Ace == 11:
          return Ace
      if Ace == 1 or Ace == 11:
        return Ace
    else:
        return int(c[0])

def total(Hand):
  total = 0

  for item in Hand:
    total = total + value(item)      
        
  if total > 21:
    print("You have a total of " + str(total) + ". You Lost!")
  elif total == 21:
    print("You have a total of " + str(total) + ". YOU WON!")
    leaderBoardAsk()
  else:
    print("You have a total of " + str(total))


print("Welcome to Game of 21!" + "\n")  
print("How to play: ")
print("You will start off with 2 cards. Then your value will be added up. You want to have the closest number to 21 without going over. If you go over then you lose. However if you get 21 then you win! NOTE: If you get a total of 21, you must play the cards. They will not play themselves for you." + "\n")
playerHand = draw(2)
showCards(playerHand)
print(" ")
print(" ")
total(playerHand) 
while choice != "P":
  choice = input("\n(D)raw Another Card, (P)lay, or (S)how LeaderBoard. ").upper()
  if choice == "D":
    newCard = random.choice(Deck)
    playerHand.append(newCard)
    showCards(playerHand)
    print(" " + "\n")
    total(playerHand)
  elif choice == "P":
    break
  elif choice == "S":
    file = open("leaderBoard.txt", "r")
    DataList = file.readlines()
    file.close()
    for i in range(len(DataList)):
      print(DataList[i])
    break
  else:
    print("Invalid Choice.")