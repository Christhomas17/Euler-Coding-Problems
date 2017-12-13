import pandas as pd
data = pd.read_table('Poker.txt', header = None, sep = ' ')
# print(data)

card = '8C'

def get_value(card):
	return(card[0])

def get_suit(card):
	return(card[1])

def get_color(card):
	if card[1] == 'C' or card[1] == 'S':
		return('B')
	else:
		return('R')

# def is_pair(hand):
# 	values = []
# 	for card in hand:
# 		values.append(get_value(card))
# 	print(values)
# 	return(set(values) != 5)

def is_flush(hand):
	suits = []
	for card in hand:
		suits.append(get_suit(card))

	return(len(set(suits)) == 1)

def card_counts(hand):
	values = []
	for card in hand:
		values.append(get_value(card))
	print(values)

	vals = {}

	for val in set(values):
		vals[val] = values.count(val)

	return(vals)



three = data.iloc[1,:5]
print(three)

for i in range(len(data)):
	hand = data.iloc[i,:5]
	if is_flush(hand):
		print(hand)
		print(i)
# print(card_counts(hand))
# print(hand)

# print(is_pair(hand)) 
