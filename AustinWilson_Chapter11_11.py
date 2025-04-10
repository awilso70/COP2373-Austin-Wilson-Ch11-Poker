import random

#Function to create a deck
def create_deck():
    #defines rank and suits for card generator and creates an empty deck
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck =[]
#Create one card for each rank and suit
    for rank in ranks:
        for suit in suits:
            deck.append(rank + " of " + suit) # adds each card to deck

    random.shuffle(deck) # shuffle the deck
    return deck #returns the deck shuffled
    #prints players hand
def show_hand(hand):
    print("Your hand: ")
    for i in range(len(hand)):  # loops through hand
        print(str(i + 1) + ": " +hand[i]) #print each card numbered 1-5

#main program
deck = create_deck()
hand = [] #empty hand

for i in range(5):
    card = deck.pop() #take card rom top of deck
    hand.append(card) #add to the hand

show_hand(hand) #shows the players the hand

# Asks the user what they want to replace
user_input = input("Enter the numbers of the cards you want to replace (1,3,5) or press Enter to keep hand: ")

#if user typed
if user_input != "":
    parts = user_input.split(",") #splits into list
    for part in parts:
        number = int(part.strip()) #convert each part to an int
        if 1 <= number <= 5: #check if number entered is 1-5
            hand[number -1] = deck.pop()    #replace card with a new one

print() #blank line
show_hand(hand)   #show final hand