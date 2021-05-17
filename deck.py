import constanats as const
import card

class Deck:
	def __init__(self, packs):
		self.packs = packs
		self.cards = []
		self.joker = None

		# Create all cards in the Deck
		for i in range(packs):
			for s in const.SUIT:
				for r in const.RANK:
					self.cards.append(card.Card(r, s))

	def shuffle(self):
		const.random.shuffle(self.cards)

	def draw_card(self):
		a = self.cards[0]
		self.cards.pop(0)
		return a

	def set_joker(self):
		self.joker = const.random.choice(self.cards)
		
		# remove the Joker from Deck and display on Table for Players to see
		self.cards.remove(self.joker)

		for card in self.cards:
			if self.joker.rank == card.rank:
				card.isjoker = True
