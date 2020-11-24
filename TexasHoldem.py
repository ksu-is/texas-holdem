import random
import time

def linebreak(sec=2):
	print('\n' + '*'*60 + '\n' + '*'*60 + '\n' + '*'*60 + '\n')
	time.sleep(sec)

suit_list = ['clubs', 'diamonds', 'hearts', 'spades']
value_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def random_card():
	random_suit = random.choice(suit_list)
	random_value = random.choice(value_list)
	return [str(random_value), random_suit]

def getcards_value(card):
	return card[0]

def getcards_suit(card):
	return card[1]

def deal_player():
	print('\nYou are dealt five cards:')
	player_hand =[]
	i = 0
	while i < 5:
		letters_list = ['a', 'b', 'c', 'd', 'e']
		given_card = random_card()
		if given_card not in player_hand:
			print(' %s)   %s of %s' %(letters_list[i], getcards_value(given_card), getcards_suit(given_card)))
			player_hand.append(given_card)
			i = i + 1
	return player_hand

def discard_cards():
	time.sleep(3)
	print('\nYou may trade up to 3 cards for new ones.')
	print('How many cards do you wish to swap (0-3)?')
	while True:
		try:
			discard_number_cards = int(input('\n> '))
			if validdiscard_num(discard_number_cards):
				break
			else:
				print('That is not allowed. Please choose between 0 and 3 cards to discard.')
		except ValueError:
			print('Wrong command. Please choose a number between 0-3.')
	return discard_number_cards
		
def validdiscard_num(discard_num):
	if 0 <= discard_num <= 3:
		return True

def specify_discard_cards(tot_discarded_cards):
	if tot_discarded_cards == 0:
		print('\nYou choose to stick with the hand you were dealt.')
		time.sleep(1.5)
		return []
	else:
		print('The number of cards to be discarded is %s' % tot_discarded_cards)
		time.sleep(1.5)
		discard_card_list = []
		
		i = 0
		while i < tot_discarded_cards:
			print('\nType the letter of card #%s to be discarded. (a-e)' % (i+1))
			discard_card = input('> ').lower()
			if not valid_card_letter(discard_card):
				continue
			if not check_card_exists(discard_card, discard_card_list):
				continue
				
			discard_card_list.append(discard_card)
			i = i + 1
		return discard_card_list
def validcard_letter(letter_input):
	five_letter = ['a', 'b', 'c', 'd', 'e']
	if letter_input.lower() not in five_letter:
		print('thats not allowed please input a card from a-e')
		return False
	else:
		return True

def check_card_exists(letter_input, used_letters):
	if letter_input.lower() not in used_letters:
		return True
	else:
		print("You've already chosen this card already please select another")
		return False

def ident_discardcards(discard_list, player1_hand):
	cardto_remove = []
	for letter in discard_list:
		if letter =='a':
			cardto_remove.append(player1_hand[0])
		if letter =='b':
			cardto_remove.append(player1_hand[1])
		if letter =='c':
			cardto_remove.append(player1_hand[2])
		if letter =='d':
			cardto_remove.append(player1_hand[3])
		if letter =='e':
			cardto_remove.append(player1_hand[4])
	return cardto_remove

