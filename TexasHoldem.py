import random
import time

def linebreak(sec=2):
	print('\n' + '*'*60 + '\n' + '*'*60 + '\n')
	time.sleep(sec)

suit_list = ['clubs', 'diamonds', 'hearts', 'spades']
value_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def rand_card():
	rand_suit = random.choice(suit_list)
	rand_value = random.choice(value_list)
	return [str(rand_value), rand_suit]

def get_card_value(card):
	return card[0]

def get_card_suit(card):
	return card[1]

def deal_player():
	print('\nYou are dealt the following five cards:')
	player_hand = []
	i = 0
	while i < 5:
		letters_list = ['a', 'b', 'c', 'd', 'e']
		given_card = rand_card()
		if given_card not in player_hand:
			print(' %s)   %s of %s' %(letters_list[i], get_card_value(given_card), get_card_suit(given_card)))
			player_hand.append(given_card)
			i = i + 1
	return player_hand

def discard_cards():
	time.sleep(4)
	print('\nYou may choose to discard up to 3 cards for new ones.')
	print('How many cards do you wish to swap (0-3)?')
	while True:
		try:
			discard_x_cards = int(input('\n> '))
			if valid_discard_num(discard_x_cards):
				break
			else:
				print('That is not allowed. Please choose between 0 and 3 cards to discard.')
		except ValueError:
			print('Invalid command. Input a number between 0-3.')
	return discard_x_cards
