
import random

card_list = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts',
         '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts',
         'Queen of Hearts', 'Jack of Hearts',
         
         '10 of Diamonds','9 of Diamonds', '8 of Diamonds', '7 of Diamonds','6 of Diamonds',
         '5 of Diamonds', '4 of Diamonds','3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds',
         'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds',
         
         '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs','6 of Clubs',
         '5 of Clubs', '4 of Clubs', '3 of Clubs','2 of Clubs', 'Ace of Clubs',
         'King of Clubs', 'Queen of Clubs', 'Jack of Clubs',
         
         '10 of Spades', '9 of Spades', '8 of Spades','7 of Spades', '6 of Spades',
         '5 of Spades', '4 of Spades','3 of Spades', '2 of Spades', 'Ace of Spades',
         'King of Spades', 'Queen of Spades', 'Jack of Spades']


# mirrored values
value_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 
          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10,
          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10,
          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

# 10s are 10
# Ace are 1
# Face cards are 10

player_hand = []
player_hand_values = []
computer_hand = []
computer_hand_values = []

# add two cards to player_hand
# add two values to player_hand_values

for i in range(2):
    index = random.randint(0,len(card_list)-1)
    
    current_card = card_list.pop(index)
    current_value = value_list.pop(index)
    
    player_hand.append(current_card)
    player_hand_values.append(current_value)


print(player_hand, player_hand_values)
