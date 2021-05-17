import constanats
import deck as importDeck
import game

def main():
	
	# Create Deck with 2 Packs
	deck = importDeck.Deck(2)
	deck.shuffle()

	# New game with 2 players
	g = game.Game(2, deck)

	# Deal Cards
	for i in range(13):
		for hand in g.players:
			card = deck.draw_card()
			hand.deal_card(card)

	# Create Pile
	first_card = deck.draw_card()
	g.add_pile(first_card)

	# Now let the Players begin
	g.play()


if __name__ == "__main__":
    main()