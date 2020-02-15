import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def shuffleDeck():
    global deck
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']*4

    random.shuffle(deck)
shuffleDeck()

def playWar():
    hand_1 = deck[:26]
    hand_2 = deck[26:]

    pile_1 = []
    pile_2 = []

    card_value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
    turn = 1

    while hand_1 and hand_2:
        player_1 = hand_1.pop()
        player_2 = hand_2.pop()

        if player_1 == player_2:
            print(color.BOLD + '\nThe cards are equal!!' + color.END)
            pile_1.extend([player_1] + hand_1[-3:])
            hand_1 = hand_1[:-3]
            hand_1.append(pile_1.pop())

            pile_2.extend([player_2] + hand_2[-3:])
            hand_2 = hand_2[:-3]
            hand_2.append(pile_2.pop())

        elif player_1 > player_2:
            print(color.BOLD + color.GREEN + '\nPlayer 1 Wins!' + color.END)
            hand_1 = [player_1, player_2] + pile_1 + pile_2 + hand_1
            pile_1 = []
            pile_2 = []

        elif player_1 < player_2:
            print(color.BOLD + color.RED + '\nPlayer 2 Wins!'+ color.END)
            hand_2 = [player_2, player_1] + pile_2 + pile_1 + hand_2
            pile_1 = []
            pile_2 = []

        hand_1_string = len(hand_1)
        hand_2_string = len(hand_2)

        print(color.UNDERLINE + '\nTurn # ' + str(turn) + color.END)
        print('Player 1 plays ' + str(player_1))
        print('Player 2 plays ' + str(player_2))
        print('\nPlayer 1 remaining cards: ' + str(hand_1_string))
        print('Player 2 remaining cards: ' + str(hand_2_string))

        turn += 1

    if hand_1_string == 1:
        print(color.BOLD + color.GREEN + '\n\nPLAYER 1 IS VICTORIOUS!' + color.END)
    elif hand_2_string == 1:
        print(color.BOLD + color.GREEN + '\n\nPLAYER 2 IS VICTORIOUS!' + color.END)

playWar()