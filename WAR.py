player1 = raw_input("What is player 1's name?")
player2 = raw_input("What is player 2's name?")

player1_score = 0
player2_score = 0

import random
def shuffled_deck():
    basic_deck = range(2,15) * 4
    random.shuffle(basic_deck)
    return basic_deck
deck = shuffled_deck()

def player_turn(player_name):
    card = deck.pop()
    print player_name, 'drew card', card
    return card
player_turn(player1)
player_turn(player2)

def compare_scores(card):
    if player1 > player2:
        player1_score = 0 + 1
        print player1_score
    else:
        player2_score = 0 + 1
        print player2_score
