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

def throw_away_discard_cards(discard_list, player1_hand, cards_to_chuck):
	for card in cards_to_chuck:
		if card in player1_hand:
			player1_hand.remove(card)
	return player1_hand		

def receive_N_cards(num_discard_cards, player1_hand, cards_to_chuck):
	i = 0
	while i < num_discard_cards:
		received_card = random_card()
		if received_card not in player1_hand and received_card not in cards_to_chuck:
			player1_hand.append(received_card)
			i = i + 1
	linebreak()
	print('\nYour final hand is:\n')
	time.sleep(1)
	for card in player1_hand:
		print('   %s of %s' % (card[0], card[1]))
	return player1_hand
	
def order_card_values(player1_hand, value_list):
	ordered_hand = []
	for value in value_list:
		for card in player1_hand:
			try:
				if int(card[0]) == value:
					ordered_hand.append(card)
			except ValueError:
				if card[0] == value:
					ordered_hand.append(card)
	return ordered_hand

def con_player_values(ordered_hand):
	player_values = []
	for card in ordered_hand:
		player_values.append(str(card[0]))
	
	low_aces_values_str = ''.join(player_values)
	
	trailing_aces = ''
	for letter in low_aces_values_str:
		if letter == 'A':
			trailing_aces += 'A'
			
	high_aces_values_str = low_aces_values_str[len(trailing_aces):] + trailing_aces
	
	return [low_aces_values_str, high_aces_values_str]
		
def is_straight():
	ordered_values_list = con_player_values(ordered_hand)
	for string in ordered_values_list:
		if string in 'A 2 3 4 5 6 7 8 9 10 J Q K A':
			return True
	else:
		return False

def is_flush(player1_hand):
	player_hand_suit_list = []
	for card in player1_hand:
		player_hand_suit_list.append(card[1])
	if player_hand_suit_list[1:] == player_hand_suit_list[:-1]:
		return True
	else:
		return False

def check_duplicate_values(player1_hand):
	values_list = []
	for card in player1_hand:
		values_list.append(card[0])
	
	counted_values = []
	already_checked_value = []
	for value in values_list:
		if value not in already_checked_value:
			already_checked_value.append(value)
			if values_list.count(value) == 2:
				counted_values.append([value, 2])
			if values_list.count(value) == 3:
				counted_values.append([value, 3])
			if values_list.count(value) == 4:
				counted_values.append([value, 4])
	
	return counted_values

def compute_dup_values(player1_hand):
	duplicate_values_list = check_duplicate_values(player1_hand)
	
	if len(duplicate_values_list) == 0:
		return False
	
	if len(duplicate_values_list) == 1:
		for mini_list in duplicate_values_list:
			if mini_list[1] == 4:
				return 'FOUR OF A KIND'
			if mini_list[1] == 3:
				return 'THREE OF A KIND'
			if mini_list[1] == 2:
				return 'PAIR OF ' + str(mini_list [0]) + 's'
	
	if len(duplicate_values_list) == 2:
		for mini_list in duplicate_values_list:
			if mini_list[1] == 3:
				return 'FULL HOUSE'
		
		pair_list = []
		for mini_list in duplicate_values_list:
			pair = str(mini_list[0])+ 's'
			pair_list.append(pair)
		return 'TWO PAIRS OF ' + pair_list[0] + ' AND ' + pair_list[1]

def determine_hand(player1_hand):
	processed_duplicate = compute_dup_values(player1_hand)
	if is_straight() and is_flush(player1_hand):
		return 'STRAIGHT FLUSH'
	elif processed_duplicate == 'FOUR OF A KIND':
		return 'FOUR OF A KIND'
	elif processed_duplicate == 'FULL HOUSE':
		return 'FULL HOUSE'
	elif is_flush(player1_hand):
		return 'FLUSH'
	elif is_straight():
		return 'STRAIGHT'
	elif processed_duplicate == 'THREE OF A KIND':
		return 'THREE OF A KIND'
	elif processed_duplicate:
		return processed_duplicate
	else:
		return deterhigh_card(player1_hand)

def deterhigh_card(player1_hand):
	reversed_value_list = value_list[::-1]
	for value in reversed_value_list:
		for card in player1_hand:
			if card[0] == 'A':
				return 'HIGH CARD ACE'
			if card[0] == value:
				return 'HIGH CARD ' + str(value)

def opponents_hand(value_list):
	rand_num = random.randint(0, 1000)
	
	opponent_val_cards = []
	i = 0
	while i < 2:
		random_value = random.choice(value_list)
		if random_value not in opponent_val_cards:
			opponent_val_cards.append(random_value)
			i += 1
	
	if rand_num <= 300:
		opponent_val_cards[0] = str(random.choice(value_list[6:] + ['A']))
		opp_hand = 'HIGH card ' + opponent_val_cards[0]
	elif rand_num <= 700:
		opp_hand = 'PAIR of ' + str(opponent_val_cards[0]) + 's'
	elif rand_num <= 900:
		opp_hand = '2 PAIRS (' + str(opponent_val_cards[0]) + 's and ' + str(opponent_val_cards[1]) + 's)'
	elif rand_num <= 950:
		opp_hand = '3 OF A KIND (' + str(opponent_val_cards[0]) + 's)'
	elif rand_num <= 975:
		opp_hand = 'STRAIGHT'
	elif rand_num <= 987:
		opp_hand = 'FLUSH'
	elif rand_num <= 995:
		opp_hand = 'FULL HOUSE (Three ' + str(opponent_val_cards[0]) + 's AND two ' + str(opponent_val_cards[1]) + 's)'
	elif rand_num <= 999:
		opp_hand = '4 OF A KIND (' + str(opponent_val_cards[0]) + 's)'
	else:
		opp_hand = 'STRAIGHT FLUSH'
	
	return [opp_hand, opponent_val_cards]

def play_again():
	print('\nWould you care to play another round? (y/n)')
	if input('> ').lower() in ['yes', 'y']:
		return True
	else:
		return False
			
print("Mattthew Conway Poker Project")
print('\nYou play Poker against an skilled player.')
while True:
	time.sleep(2.0)
	dealt_hand = deal_player()
	
	tot_discarded_cards = discard_cards()
	discarded_cards_list = specify_discard_cards(tot_discarded_cards)
	cards_to_chuck = ident_discardcards(discarded_cards_list, dealt_hand)
	remaining_hand = throw_away_discard_cards(discarded_cards_list, dealt_hand, cards_to_chuck)
	
	new_hand = receive_N_cards(tot_discarded_cards, remaining_hand, cards_to_chuck)
	ordered_hand = order_card_values(new_hand, value_list)
	
	name_player_hand = determine_hand(ordered_hand)
	
	time.sleep(2.5)
	print('\nYou reveal your hand:\n%s' % name_player_hand)
	time.sleep(1.5)
	enemy_hand = opponents_hand(value_list)
	print('\nYour opponent reveals their hand:\n' + enemy_hand[0])
		
	if not play_again():
		print('\nThank you for playing come again')
		time.sleep(1)
		break
linebreak()
