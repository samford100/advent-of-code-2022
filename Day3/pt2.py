import string

sum = 0
with open('./Day3/input.txt') as f:
	lines = [line.strip() for line in f]
	# iterate over in chunks of 3
	chunk_size = 3
	for i in range(0, len(lines), chunk_size):
		chunk = lines[i:i + chunk_size]
		print(chunk)
		# find the letter in common
		e = list(set(chunk[0]).intersection(set(chunk[1])).intersection(set(chunk[2])))[0]
		print(e)

		if len(e) == 0:
			continue
		if e in string.ascii_lowercase:
			v = string.ascii_lowercase.find(e[0]) + 1
			print(v)
			sum += v
		elif e in string.ascii_uppercase:
			v = string.ascii_uppercase.find(e[0]) + 27
			print(v)
			sum += v

print(sum)