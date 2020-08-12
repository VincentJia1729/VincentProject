
import random

card_list = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts',
         '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts',
         'Queen of Hearts', 'Jack of Hearts']
         
         
# mirrored values
value_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10] 


# 10s are 10
# Ace are 1
# Face cards are 10

player_hand = []
player_hand_values = []
computer_hand = []
computer_hand_values = []
player_hand_value = 0 
computer_hand_value = 0
keep_playing = True

def mainMenu():
    inp = input("Do you want to (h)it or (s)tand?: ")
    return inp

# add two cards to player_hand
# add two values to player_hand_values

for i in range(2):
    index = random.randint(0,len(card_list)-1)
    
    current_card = card_list.pop(index)
    current_value = value_list.pop(index)
    
    player_hand.append(current_card)
    player_hand_values.append(current_value)


print(player_hand, player_hand_values)
#print(card_list, value_list)

for i in range(len(player_hand_values)):
    player_hand_value += player_hand_values[i]

print(player_hand_value)

choice = mainMenu()

while choice != "s":
    index = random.randint(0,len(card_list)-1)

    current_card = card_list.pop(index)
    current_value = value_list.pop(index)
    
    player_hand.append(current_card)
    player_hand_values.append(current_value)

    player_hand_value += player_hand_values[-1]
    '''
    print(player_hand_values[-1])
    print(player_hand_values)
    '''

    

    print(player_hand_value)

    # win condition check

    if player_hand_value > 21:
        print("Bust! You lose!")
        keep_playing = False
        break

    if player_hand_value == 21:
        print("Black jack! You win!")
        keep_playing = False
        break
    
    choice = mainMenu()

    
new_card_list = card_list.copy()
new_value_list = value_list.copy()

if keep_playing:
    for i in range(2):
        index = random.randint(0,len(new_card_list)-1)
        
        current_card = new_card_list.pop(index)
        current_value = new_value_list.pop(index)
        
        computer_hand.append(current_card)
        computer_hand_values.append(current_value)


    print(computer_hand, computer_hand_values)
    # print(new_card_list, new_value_list)

    for i in range(len(computer_hand_values)):
        computer_hand_value += computer_hand_values[i]

    print(computer_hand_value)

    while computer_hand_value < player_hand_value:
        
        index = random.randint(0,len(new_card_list)-1)

        current_card = new_card_list.pop(index)
        current_value = new_value_list.pop(index)
        
        computer_hand.append(current_card)
        computer_hand_values.append(current_value)

        computer_hand_value += computer_hand_values[-1]
        '''
        print(player_hand_values[-1])
        print(player_hand_values)
        '''

        print(computer_hand_value)

        if computer_hand_value > 21:
            print("Bust! Computer loses!")
            break

        if player_hand_value == 21:
            print("Black jack! Computer wins!")
            break

    if computer_hand_value > player_hand_value:
        print("Computer has more points! Computer wins!")





















