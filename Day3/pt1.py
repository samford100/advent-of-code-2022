import string

sum = 0
with open('./Day3/input.txt') as f:
	while l := f.readline().strip():
		l = l.strip()
		print(l)
		# split in half
		i = len(l) // 2
		left = set(l[:i])
		right = set(l[i:])
		# take set difference
		e = list(left.intersection(right))
		print(e)
		# convert to scores
		if len(e) == 0:
			continue
		if e[0] in string.ascii_lowercase:
			v = string.ascii_lowercase.find(e[0]) + 1
			print(v)
			sum += v
		elif e[0] in string.ascii_uppercase:
			v = string.ascii_uppercase.find(e[0]) + 27
			print(v)
			sum += v


print(sum)
