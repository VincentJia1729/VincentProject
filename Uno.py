'''
Played with a deck of 76 cards -- there's one 0 and two of each of 1-9 in each of four colors (red, blue, yellow, green).
- Each player gets 7 cards.
- A single card from the deck is turned face up to start a discard pile.
- Each player, in turn, must play a card that matches the top card of the discard pile either in number or in color.
 (For example, if the top card is "red 4", a player could play "red 9" or "blue 4".) The played card goes on top of the pile.
- If a player can't play, they draw a card from the deck. If they can play the card just drawn, they do so; otherwise they add it to their hand.
  In either case, the player's turn is over.
- If the deck runs out, we shuffle the discard pile (except for the top card) and use it as our new deck.
- The first player to get rid of all of their cards wins.
'''

import random

class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9
      color: string'''

    def __init__(self,rank,color):
        '''UnoCard(rank,color) -> UnoCard
        creates an Uno card with the given rank and color
        color is a string
        '''
        self.rank = rank
        self.color = color

    def __str__(self):
        '''str(Unocard) -> str'''
        return(self.color + ' ' + str(self.rank))

    def is_match(self,other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        return (self.color == other.color) or (self.rank == other.rank)


class UnoDeck:

    def __init__(self):
        
        self.deck = []
        for color in ['RED','BLUE','GREEN','YELLOW']:
            self.deck.append(UnoCard(0,color))
            for i in range(2):
                for j in range(1,10):
                    self.deck.append(UnoCard(j,color))
        random.shuffle(self.deck)

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'There are ' + str(len(self.deck)) + ' cards remaining'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self,pile):
        '''UnoDeck.reset_deck(pile)
        resets the deck from the pile'''
        self.deck = pile.reset_pile()
        random.shuffle(self.deck)


class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self, deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        card = deck.deal_card()
        self.pile = [card]

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has ' + str(self.pile[-1])+ ' on top'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''
        return self.pile[-1]

    def add_card(self,card):
        '''UnoPile.add_card(card)
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        new_deck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return new_deck


class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self,name,deck):
        '''UnoPlayer(name,deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = []
        for i in range(7):
            self.hand.append(deck.deal_card())
        

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name) + ' has ' + str(len(self.hand)) + ' cards'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        s = ''
        for card in self.hand:
            s += str(card) + '\n'
        return s

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self,deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        card = deck.deal_card()
        self.hand.append(card)
        return card
        

    def play_card(self,card,pile):
        '''UnoPlayer.play_card(card,pile)
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)

    def take_turn(self,deck,pile):
        '''UnoPlayer.take_turn(deck,pile)
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''
        
        print(self.name + ", it's your turn")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
        top_card = pile.top_card()
        matches = [card for card in self.hand if card.is_match(top_card)]

        if len(matches) > 0:
            # chose card to play
            print("These cards can be played: ")
            for index in range(len(matches)):
                print(str(index + 1) + " : " + str(matches[index]))

            choice = 0
            while choice < 1 or choice > len(matches):
                choice_str = input("Which card do you want to play? ")
                if choice_str.isdigit():
                    choice = int(choice_str)
                    self.play_card(matches[index - 1], pile)
                    
        else:
            # draw card. play it if you can
            # check is deck is empty
            if deck.is_empty():
                deck.reset_deck(pile)
            new_card = self.draw_card(deck)
            print("You drew: " + str(new_card))
            if new_card.is_match(top_card):
                print("You can play that")
                self.play_card(new_card , pile)
            else:
                print("You still can't play")
            input("Press enter to continue")
                

def play_uno():
    deck = UnoDeck()
    pile = UnoPile(deck)
    player_list = []

    inp = int(input("How many players are there? "))

    for i in range(inp):
        name = input("Enter a player name for player " + str(i+1) + ": ")
        player_list.append(UnoPlayer(name,deck))

    current_player = 0
    
    while True:
        print('--------')
        for i in player_list:
            print(i)
        print('---------')
        player_list[current_player].take_turn(deck,pile)

        if player_list[current_player].has_won():
            print(player_list[current_player].get_name() + ' has won!')

            break

        current_player = (current_player + 1) % inp


play_uno()
    
    

















    











    
    
