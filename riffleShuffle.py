import random
from scipy.special import binom, factorial
# binom(n, k) computes "n choose k":
# factorial(n) computes n!


# creates a deck with n cards
def deck_generator(n):
    arr = []
    for i in range(0,n):
        arr.append(i)
    return arr

# simulates a top to random shuffle on a deck of cards (arr)
def top_to_random(arr):
    shuffled_arr = []
    l = len(arr)
    top_cards_new_pos = random.randint(0, l - 1)
    j = 0
    for i in range(0, l):
        if top_cards_new_pos == i:
            shuffled_arr.append(arr[0])
            continue
        else:
            j += 1
            shuffled_arr.append(arr[j])
    return shuffled_arr

# simulates an average human riffle shuffle on a deck of cards (arr)
def gsr(arr):
    first_half = []
    second_half = []
    shuffled_arr = []
    random_sequence = []
    l = len(arr)
    first_half_count = 0
    first_half_pos = 0
    second_half_pos = 0
    for i in range(0,l):
        coin = random.randint(0,1)
        random_sequence.append(coin)
        if coin == 0:
            first_half_count += 1
    for i in range(0, first_half_count):
        first_half.append(arr[i])
    for i in range(first_half_count, l):
        second_half.append(arr[i])
    for i in range(0,l):
        if random_sequence[i] == 0:
            shuffled_arr.append(first_half[first_half_pos])
            first_half_pos += 1
        elif random_sequence[i] == 1:
            shuffled_arr.append(second_half[second_half_pos])
            second_half_pos += 1
    return shuffled_arr

#tests whether the card numbered i occurs before j in the listl
def test_order(i, j, arr):
    position_of_i = 0
    position_of_j = 0
    l =  len(arr)
    for r in range(0, l):
        if arr[r] == i:
            position_of_i = r
        elif arr[r] == j:
            position_of_j = r
    if position_of_i < position_of_j:
        return 1
    elif position_of_i > position_of_j:
        return 0

# For the number of trials:
# 1 / t^0.5 = 0.01
# t = 10000
def simulate(deck_size, shuffle_type, number_of_shuffles, card_above, card_below):
    true_count = 0
    for i in range(0, 10000):
        deck = deck_generator(deck_size)
        #print(deck)
        for i in range(0, number_of_shuffles):
            if shuffle_type == 'top':
                deck = top_to_random(deck)
            elif shuffle_type == 'gsr':
                deck = gsr(deck)
            #print(deck)
        if test_order(card_above, card_below, deck) == 1:
            true_count += 1
            #print(true_count)
    return true_count/10000

print(simulate(15,'gsr',1,6,8))