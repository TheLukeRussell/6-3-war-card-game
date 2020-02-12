import random



def shuffleDeck():
    global deck
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4

    random.shuffle(deck)
shuffleDeck()

def playWar():
    hand_1 = deck[:26]
    hand_2 = deck[26:]

    pile_1 = []
    pile_2 = []

    card_value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    round = 1

    while hand_1 and hand_2:
        player_1 = hand_1.pop()
        player_2 = hand_2.pop()
        
        if player_1 == player_2:
            print('The cards are equal')

        elif player_1 > player_2:
            print('Player1 wins')

        elif player_1 < player_2:
            print('Player2 wins')

playWar()