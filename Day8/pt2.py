import numpy as np

with open('./Day8/input.txt') as f:
	lines = [[int(x) for x in l.strip()] for l in f.readlines()]
	lines = np.array(lines)


visible_count = 0
visible_count += len(lines) * 4 - 4  # top + bot + left - 2 + right - 2

# vr = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
vr = np.zeros((len(lines), len(lines)))

'''
[3 0 3 7 3]
[]
[0]
[0 1]
[1 1 1]
[0 0 0 0]

'''


def left(lines):
	print(lines)
	vs = np.zeros((len(lines), len(lines)))
	for i in range(len(lines)):
		r = lines[i]
		# print(r)
		# print()
		for j in range(len(r)):
			e = r[j]
			left_elements = [r[k] for k in range(j)]
			# print(f'{left_elements} | {e}')
			# create mask of elements
			# print(mask)
			count = 0
			for k in range(j-1, -1, -1):
				if r[k] < e:
					count += 1
				else:
					count += 1
					break
			# print(f'c:{count}')
			# if score
			vs[i][j] = count
			# print(vr)
			# print('~~~~~')
		# break
	print(vs)
	print('----------')
	return vs


'''
3 []
0 [3]
3 [3 0
'''
vs = left(lines)
vs2 = left(np.rot90(lines))
vs3 = left(np.rot90(lines, 2))
vs4 = left(np.rot90(lines, 3))
print('~')

vr = vs * np.rot90(vs2, 3) * np.rot90(vs3,2) * np.rot90(vs4, 1)
# print(vr)
# find max score
print(vr)
print(vr.max())
'''
1 [0]
2 [0, 1]
3 [0, 1, 2]
4 [0, 1, 2, 3]
5 [0, 1, 2, 3, 4]
'''
