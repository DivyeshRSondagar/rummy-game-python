import player

class Game:

	def __init__(self, hands, deck):

		self.pile = []
		self.players = []

		for i in range(hands):
			name = input("Enter name of Player " + str(i) + ": ")
			self.players.append(player.Player(name, deck, self))

	def display_pile(self):
		if len(self.pile) == 0:
			print("Empty pile.")
		else:
			print("The card at the top of the pile is: ", self.pile[0])

	def add_pile(self, card):

		self.pile.insert(0, card)

	def draw_pile(self):
		if len(self.pile) != 0:
			return self.pile.pop(0)
		else:
			return None

	def play(self):
		i = 0
		while self.players[i].play() == False:
			print(chr(27)+"[2J")
			i += 1
			if i == len(self.players):
				i = 0
			print("***", self.players[i].name, "to play now.")
			input(self.players[i].name + " hit enter to continue...")

		# Game Over
		print("*** GAME OVER ***")
		print("*** ", self.players[i].name, " Won the game ***")

