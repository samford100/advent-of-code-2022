
move_score = {
	'X': 1,
	'Y': 2,
	'Z': 3
}

game_score = {
	'AX': 3,
	'AY': 6,
	'AZ': 0,
	'BX': 0,
	'BY': 3,
	'BZ': 6,
	'CX': 6,
	'CY': 0,
	'CZ': 3
}


def game(them, me):
	return game_score[them+me] + move_score[me]


total_score = 0
with open('./Day2/input.txt') as f:
	while l := f.readline():
		them, me = l.strip().split(' ')
		total_score += game(them, me)

print(total_score)









