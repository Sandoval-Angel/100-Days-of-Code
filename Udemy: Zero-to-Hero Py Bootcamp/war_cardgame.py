# Code plays a modified version of WAR card game:

# Creates standard 52-card deck and deals half (26) to each of 2 player
# Each player reveals top card of their deck - player w/ highest value card takes both cards and puts at bottom of deck
# In the event card values are the same, WAR is triggered...
# To declare war, one must have minimum 10 cards left in their deck
# Each player places 10 cards from their deck face down on the table and reveals the last placed card
# Player with highest value card wins all cards, if same value again loop war

# A player loses the game when they have 0 cards left or are unable to declare war (10 min cards req)


from random import shuffle

game_on = True

ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.new_deck = []
        self.deck_half = []

        for rank in ranks:
            for suit in suits:
                new_card = Card(rank, suit)

                self.new_deck.append(new_card)

        shuffle(self.new_deck)

    def deal_half(self):

        self.deck_half = []

        for card in range(26):
            self.deck_half.append(self.new_deck.pop())

        return self.deck_half


class Player:

    def __init__(self, player_name, deck_name):
        self.player_name = player_name
        self.cards = deck_name.deal_half()

    def play_top(self):
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        self.cards += new_cards

        return f"{len(new_cards)} cards added to bottom of {self.player_name}'s deck.\n"

    def __str__(self):
        return f'{self.player_name} has {len(self.cards)} card(s) left in deck.'


full_deck = Deck()

p1 = Player('Angel', full_deck)
p2 = Player('John', full_deck)

while game_on:

    # Check game over; if so, state winner and break out of game loop
    if len(p1.cards) == 0:
        print(f'{p1.player_name} has run of of cards. {p2.player_name} wins!')
        break
    elif len(p2.cards) == 0:
        print(f'{p2.player_name} has run of of cards. {p1.player_name} wins!')
        break

    # Print current players' deck totals
    print(p1, p2)

    # Each player reveals top card of their deck
    p1_card = p1.play_top()
    p2_card = p2.play_top()
    print(f'{p1.player_name} reveals the {p1_card}. {p2.player_name} reveals the {p2_card}.')

    # Run comparison logic and add cards to deck of winning player
    if p1_card.value > p2_card.value:
        print(f'{p1.player_name} wins. ' + p1.add_cards([p1_card, p2_card]))
    elif p1_card.value < p2_card.value:
        print(f'{p2.player_name} wins. ' + p2.add_cards([p1_card, p2_card]))
    else:
        at_war = True
        # Tracking cards to be picked up by winner of the war
        p1_table = [p1_card]
        p2_table = [p2_card]

        # War scenario - includes loop in case of multiple wars in a row
        while at_war:
            print('\nWAR!\n')

            # Declaring war requires a minimum of 10 cards in deck; if someone can't declare warm, they lose
            if len(p1.cards) < 10:
                print(f'{p1.player_name} is unable to declare war. {p2.player_name} WINS!')
                game_on = False
                break
            elif len(p2.cards) < 10:
                print(f'{p2.player_name} is unable to declare war. {p1.player_name} WINS!')
                game_on = False
                break

            # Both players can declare war, adding top 10 of deck to their pile
            for i in range(10):
                p1_table.append(p1.play_top())
                p2_table.append(p2.play_top())

            print('Each player adds top 10 cards to pile, revealing the last card.\n'
                  f'{p1.player_name} reveals the {p1_table[-1]}. {p2.player_name} reveals the {p2_table[-1]}.')

            # Combine both piles to prep for adding to bottom of winner's deck
            full_table = p1_table + p2_table

            # Perform calc on last revealed cards from 10 added for war, granting all cards to winner
            # or looping if another war is triggered
            if p1_table[-1].value > p2_table[-1].value:
                at_war = False
                print(f'{p1.player_name} wins. ' + p1.add_cards(full_table))
            elif p1_table[-1].value < p2_table[-1].value:
                at_war = False
                print(f'{p2.player_name} wins. ' + p2.add_cards(full_table))
