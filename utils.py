import constanats as const

def get_object(arr, str_card):

	if len(str_card) != 2:
		return None

	for item in arr:
		if item.rank == str_card[0] and item.suit[0] == str_card[1]:
			return item

	return None

def is_valid_run(sequence):
	const.RANK_VALUE["A"] = 1
	sort_sequence(sequence)
	for card in sequence:
		if card.suit != sequence[0].suit:
			return False

	if sequence[0].rank == "A":
		if sequence[1].rank == "Q" or sequence[1].rank == "J" or sequence[1].rank == "K":
			const.RANK_VALUE[sequence[0].rank] = 14
			sort_sequence(sequence)

	# Rank Comparison
	for i in range(1,len(sequence)):
		if const.RANK_VALUE[sequence[i].rank] != const.RANK_VALUE[(sequence[i-1].rank)]+1:
			return False

	return True

def sort_sequence(sequence):
	is_sort_complete = False

	while is_sort_complete == False:
		is_sort_complete = True
		for i in range(0, len(sequence)-1):
			if const.RANK_VALUE[sequence[i].rank] > const.RANK_VALUE[sequence[i+1].rank]:
				a = sequence[i+1]
				sequence[i+1] = sequence[i]
				sequence[i] = a
				is_sort_complete = False
	return sequence

def is_valid_book(sequence):
	while(sequence[0].isjoker == True):
		sequence.append(sequence.pop(0))

	for card in sequence:
		if card.is_joker() == True:
			continue
		if card.rank != sequence[0].rank:
			return False

	return True

def print_cards(arr):
	s = ""
	for card in arr:
		s = s + " " + str(card)
	return s

def is_valid_run_joker(sequence):
	const.RANK_VALUE["A"] = 1
	sort_sequence(sequence)
	push_joker_toend(sequence)
	joker_count = 0
	for card in sequence:
		if card.is_joker() == True:
			joker_count += 1

	for card in sequence:
		if card.is_joker() == True:
			continue
		if card.suit != sequence[0].suit:
			return False

	if sequence[0].rank == "A":
		if sequence[1].rank == "Q" or sequence[1].rank == "J" or sequence[1].rank == "K":
			const.RANK_VALUE[sequence[0].rank] = 14
			sort_sequence(sequence)
			push_joker_toend(sequence)

	rank_inc = 1
	for i in range(1,len(sequence)):
		if sequence[i].is_joker() == True:
			continue
		# Compare RANK values with accomodating for Jokers.
		while (const.RANK_VALUE[sequence[i].rank] != const.RANK_VALUE[(sequence[i-1].rank)]+rank_inc):
			# Use Joker Count for missing Cards in the run
			if joker_count > 0:
				rank_inc += 1
				joker_count -= 1
				continue
			else:
				# if No more Jokers left, then revert to regular comparison
				if const.RANK_VALUE[sequence[i].rank] != const.RANK_VALUE[(sequence[i-1].rank)]+1:
					return False
				else:
					break
	return True

def push_joker_toend(sequence):
	sort_sequence(sequence)
	joker_list = []
	for card in sequence:
		if card.is_joker()== True:
			sequence.remove(card)
			joker_list.append(card)
	sequence += joker_list
	return sequence
