import numpy as np
with open('./Day8/input.txt') as f:
	lines = [[int(x) for x in l.strip()] for l in f.readlines()]
	lines = np.array(lines)

# print(lines)


visible_count = 0
visible_count += len(lines) * 4 - 4 # top + bot + left - 2 + right - 2

# vr = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
vr = np.zeros((len(lines), len(lines)))

def left(lines, vr):

	for i in range(len(lines)):
		r = lines[i]
		for j in range(len(r)):
			left_elements = [r[k] for k in range(j)]
			left_max = max(left_elements) if len(left_elements) > 0 else -1
			if r[j] > left_max:
				vr[i][j] = 1
	return vr

'''
3 []
0 [3]
3 [3 0
'''
vr = left(lines, vr)
vr = left(np.rot90(lines), np.rot90(vr))
vr = left(np.rot90(lines, 2), np.rot90(vr, 1))
vr = left(np.rot90(lines, 3), np.rot90(vr, 1))
#
# print(vr)
print(vr.sum())
'''
1 [0]
2 [0, 1]
3 [0, 1, 2]
4 [0, 1, 2, 3]
5 [0, 1, 2, 3, 4]
'''








