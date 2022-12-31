ml = 14

with open('./Day6/input.txt') as f:
	l = f.readline().strip()
	q = [] # just pure sliding window
	for i, c in enumerate(l):
		q.append(c)
		if len(q) > ml:
			q = q[1:]
		if len(set(q)) == ml:
			print(i + 1)
			break







