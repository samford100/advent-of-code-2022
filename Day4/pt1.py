count = 0
with open('./Day4/input.txt') as f:
	while l := f.readline():
		l = l.strip()
		first, second = l.split(',')
		# check if first is contained within second or vice versa
		f1, f2 = first.split('-')
		s1, s2 = second.split('-')
		f1,f2,s1,s2 = int(f1), int(f2), int(s1), int(s2)
		if f1 >= s1 and f2 <= s2:
			count +=1
		elif s1 >= f1 and s2 <= f2:
			count +=1

print(count)

