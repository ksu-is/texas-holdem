import random
import time

def linebreak(sec=2):
	print('\n' + '*'*60 + '\n' + '*'*60 + '\n')
	time.sleep(sec)

# Lists for card variables to generate any of the possible 52 cards
suit_list = ['clubs', 'diamonds', 'hearts', 'spades']
value_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
