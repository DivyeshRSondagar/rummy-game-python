import constanats as const

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.isjoker = False

	def __str__(self):
		if self.isjoker:
			return (self.rank + const.SUIT_SYMBOLS[self.suit] + '-J')
		return (self.rank + const.SUIT_SYMBOLS[self.suit])

	def is_joker(self):
		return self.isjoker
