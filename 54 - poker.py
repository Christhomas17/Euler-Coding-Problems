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
#pair, three of a kind etc
def card_counts(hand):
	values = []
	for card in hand:
		values.append(get_value(card))
	print(values)

	vals = {}

	for val in set(values):
		vals[val] = values.count(val)

	return(vals)

#straight
def is_straight(hand):
	faces = {'J':10, 'Q':11, 'K':12, 'A':13}
	values = []
	for card in hand:
		values.append(get_value(card))

	if len(set(values)) == 5:

		if '2' in values and 'A' in values:
			faces = {'T':'10','J':'11', 'Q':'12', 'K':'13', 'A':'1'}
		else:
			faces = {'T':'10','J':'11', 'Q':'12', 'K':'13', 'A':'14'}
		print(values)
		values = [int(faces[card]) if card in faces else int(card) for card in values]
		print(values)
		values = sorted(values)
		print(values)
		
		if int(values[0]) + 4 == int(values[-1]):
			return(True)

	return(False)

def is_royal(hand):
	








three = data.iloc[6,:5]
print(three)

print(is_straight(three))

# for i in range(len(data)):
# 	hand = data.iloc[i,:5]
# 	if is_flush(hand):
# 		print(hand)
# 		print(i)
# print(card_counts(hand))
# print(hand)

# print(is_pair(hand)) 
