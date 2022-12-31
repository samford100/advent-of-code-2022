import string

with open('./Day5/input.txt') as f:
	stacks = []
	sc = 0
	# build stacks
	while l := f.readline().rstrip():
		# print(l)
		if '1' in l:
			break
		for i in range(1, len(l), 4):
			sn = i // 4
			if sn >= len(stacks):
				stacks.append([])
			if l[i] != ' ':
				# stacks[sn].append(l[i])
				stacks[sn] = [l[i]] + stacks[sn]

	l = f.readline().strip()

	# follow instructions
	while l := f.readline().strip():
		# pick out numbers
		# count, origin, dest =
		v = l.split(' ')
		count, origin, dest = int(v[1]), int(v[3]) - 1, int(v[5]) - 1
		# perform operation
		for c in range(count):
			o = stacks[origin]
			d = stacks[dest]
			stacks[dest].append(stacks[origin].pop())

	for s in stacks:
		print(s[-1], end='')
	print()

def ps(stack):
	print('--STACKS--')
	for s in stacks:
		print(s)
	print('-----------')
