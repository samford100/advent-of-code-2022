game_score = {
	'X': 0,
	'Y': 3,
	'Z': 6
}

move_score = {
	'AX': 3,
	'AY': 1,
	'AZ': 2,
	'BX': 1,
	'BY': 2,
	'BZ': 3,
	'CX': 2,
	'CY': 3,
	'CZ': 1
}

# XYZ ->WLT


def game(them, outcome):
	return game_score[outcome] + move_score[them+outcome]


total_score = 0
with open('./Day2/input.txt') as f:
	while l := f.readline():
		them, me = l.strip().split(' ')
		total_score += game(them, me)

print(total_score)









