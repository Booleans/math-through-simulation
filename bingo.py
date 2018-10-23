import numpy as np
import random

def create_bingo_card():
    col1 = np.random.choice(range(1,16) , size=5, replace=False).reshape(5,1)
    col2 = np.random.choice(range(16,31), size=5, replace=False).reshape(5,1)
    col3 = np.random.choice(range(31,46), size=5, replace=False).reshape(5,1)
    col4 = np.random.choice(range(46,61), size=5, replace=False).reshape(5,1)
    col5 = np.random.choice(range(61,76), size=5, replace=False).reshape(5,1)
    bingo_card = np.concatenate((col1, col2, col3, col4, col5), axis=1)
    bingo_card[2,2] = 0
    return bingo_card

def check_for_bingo(bingo_card):
    col_empty = np.any(np.logical_not(np.any(bingo_card, axis=0)))
    row_empty = np.any(np.logical_not(np.any(bingo_card, axis=1)))
    diag1_empty = np.logical_not(np.any(np.diagonal(bingo_card)))
    diag2_empty = np.logical_not(np.any(np.diagonal(bingo_card[::-1])))
    
    if True in (col_empty, row_empty, diag1_empty, diag2_empty):
        return True
    else:
        return False

def generate_random_draw_order():
    nums = list(range(1,76))
    random.shuffle(nums)
    return nums

def generate_opponent_cards(n_players):
    cards = []
    for _ in range(n_players):
        cards.append(create_bingo_card())
    return cards

def main():
    name = input('Hello, what is your name? ')
    print(f'Hello {name}! Let\'s play some bingo.')
    n_opponents = int(input('How many other players are you playing against? '))
    opponent_cards = generate_opponent_cards(n_opponents)
    my_card = create_bingo_card()
    print('Alright, here\'s your card.')
    print(my_card)
    print('Here we go!')
    draw_order = generate_random_draw_order()
    
    you_won = False
    opponent_won = False
    turn = 0
    for num in draw_order:
        turn += 1
        my_card[np.where(my_card==num)] = 0
        you_won = check_for_bingo(my_card)
        for card in opponent_cards:
            card[np.where(card==num)] = 0
            if check_for_bingo(card):
                opponent_won = True
        if you_won and opponent_won:
            print(f'You won in round {turn} but so did one of your opponents.')
            print(f'The numbers drawn were {draw_order[0:turn]}.')
            break
        elif you_won:
            print(f'You won in round {turn}!')
            print(f'The numbers drawn were {draw_order[0:turn]}.')
            break
        elif opponent_won:
            print(f'You lost in round {turn}!')
            print(f'The numbers drawn were {draw_order[0:turn]}.')
            break

if __name__ == '__main__':
    main()