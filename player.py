import constanats as const
import card as Card
import utils
class Player:

	def __init__(self, name, deck, game):
		
		self.stash = []
		self.name = name
		self.deck = deck
		self.game = game

	def deal_card(self, card):
		try:
			self.stash.append(card)
			if len(self.stash) > 14:
				raise ValueError('ERROR: Player cannot have more than 14 cards during turn')
		except ValueError as err:
			print(err.args)

	def drop_card(self, card):
		card = utils.get_object(self.stash, card)
		if card not in self.stash:
			return False

		self.stash.remove(card)
		self.game.add_pile(card)

		return True


	def close_game(self):
		set_array = [self.stash[:3], self.stash[3:6], self.stash[6:9], self.stash[9:]]
		count = 0
		for s in set_array:
			if utils.is_valid_run(s):
				count += 1
		if count == 0:
			return False
		for s in set_array:
			if utils.is_valid_run(s) == False and utils.is_valid_book(s) == False and utils.is_valid_run_joker(s) == False:
				return False

		return True

	def play(self):

		while True:
			print(chr(27)+"[2J")
			print("***",self.name,"your cards are:")
			print(utils.print_cards(self.stash))
			self.game.display_pile()

			# Get Player Action
			action = input("*** " + self.name + ", What would you like to do? ***, \n(M)ove Cards, (P)ick from pile, (T)ake from deck, (D)rop, (S)ort, (C)lose Game, (R)ules: ")

			# Move or Rearrange Cards in the stash
			if action == 'M' or action == 'm':
				# Get the Card that needs to moved.
				move_what = input("Enter which card you want to move. \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
				move_what.strip()
				if utils.get_object(self.stash, move_what.upper()) not in self.stash:
					input("ERROR: That card is not in your stash.  Enter to continue")
					continue

				# Get the Card where the move_what needs to moved.
				move_where = input("Enter where you want move card to (which card the moving card will go before) Enter Space to move to end \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts):" )
				move_where.strip()
				if move_where != "" and utils.get_object(self.stash, move_where.upper()) not in self.stash:
					input("ERROR: This is an invalid location.  Enter to continue")
					continue

				# Perform the Move Operation
				move_what = utils.get_object(self.stash, move_what.upper())
				if move_where != "":
					move_where = utils.get_object(self.stash, move_where.upper())
					location = self.stash.index(move_where)
					if location > self.stash.index(move_what):
						location = location - 1
					self.stash.remove(move_what)
					self.stash.insert(location, move_what)
				else:
					# If the move_where was not specified by the User then,
					#		the card to the end of the stash
					self.stash.remove(move_what)
					self.stash.append(move_what)

			# Pick card from Pile
			if action == 'P' or action == 'p':
				if len(self.stash) < 14:
					c = self.game.draw_pile()
					self.stash.append(c)
				else:
					input("ERROR: You have " + str(len(self.stash)) + " cards. Cannot pick anymore. Enter to continue")

			# Take Card from Deck
			if action == 'T' or action == 't':
				if len(self.stash) < 14:
					c = self.deck.draw_card()
					self.stash.append(c)
				else:
					input("ERROR: You have " + str(len(self.stash)) + " cards. Cannot take anymore. Enter to continue")

			# Drop card to Pile
			if action == 'D' or action == 'd':
				if len(self.stash) == 14:
					drop = input("Which card would you like to drop? \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
					drop = drop.strip()
					drop = drop.upper()
					if self.drop_card(drop):
						# return False because Drop Card does not end the game
						return False
					else:
						input("ERROR: Not a valid card, Enter to continue")
				else:
					input("ERROR: Cannot drop a card. Player must have 13 cards total. Enter to continue")

			# Sort cards in the stash
			if action == 'S' or action == 's':
				utils.sort_sequence(self.stash)

			# Close the Game
			if action == 'C' or action == 'c':

				if len(self.stash) == 14:
					drop = input("Which card would you like to drop? \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
					drop = drop.strip()
					drop = drop.upper()
					if self.drop_card(drop):
						if self.close_game():
							print(utils.print_cards(self.stash))
							# Return True because Close ends the Game.
							return True
						else:
							input("ERROR: The game is not over. Enter to Continue playing.")
							# if this Close was false alarm then discarded Card will
							#		have to be put back into the stash for the Player to continue.
							self.stash.append(self.game.draw_pile())
					else:
						input("ERROR: Not a valid card, Enter to continue")
				else:
					input("ERROR: You do not have enough cards to close the game. Enter to Continue playing.")

			# Show Rules of the game
			if action == 'R' or action == 'r':
				print("------------------ Rules --------------------",
					"\n- Rummy is a card game based on making sets.",
					"\n- From a stash of 13 cards, 4 sets must be created (3 sets of 3, 1 set of 4).",
					"\n- The set of 4 must always be at the end"
					"\n- A valid set can either be a run or a book.",
					"\n- One set must be a run WITHOUT using a joker."
					"\n- A run is a sequence of numbers in a row, all with the same suit. ",
					"\n \tFor example: 4 of Hearts, 5 of Hearts, and 6 of Hearts",
					"\n- A book of cards must have the same rank but may have different suits.",
					"\n \tFor example: 3 of Diamonds, 3 of Spades, 3 of Clubs",
					"\n- Jokers are randomly picked from the deck at the start of the game.",
					"\n- Joker is denoted by '-J' and can be used to complete sets.",
					"\n- During each turn, the player may take a card from the pile or from the deck.",
					"Immediately after, the player must drop any one card into the pile so as not go over the 13 card limit.",
					"\n- When a player has created all the sets, select Close Game option and drop the excess card into the pile.",
					"\n- Card with Rank 10 is represented as Rank T"
					"\n--------------------------------------------" )
				input("Enter to continue ....")
