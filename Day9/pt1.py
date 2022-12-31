import numpy as np

with open('./Day9/input.txt') as f:
	lines = [l.strip().split(' ') for l in f.readlines()]

h = np.array([0, 0])  # x, y
t = np.array([0, 0])  #

visited = set()

h_moves = {
	'R': np.array([1, 0]),
	'L': np.array([-1, 0]),
	'D': np.array([0, -1]),
	'U': np.array([0, 1]),
}


'''
         (x, y)
.H.H.  | (-1, 2)=LU, (1, 2)=RU
H...H  | (-2, 1)=LU, (2, 1)=RU 
..T..  | 
H...H  | (-2, -1)=LD, (2, -1)=RD
.H.H.  | (-1, -2)=LD, (1, -2)=RD

'''


t_moves_h_minus_t = {
	# non moves
	(0,0): np.array([0,0]),
	(1,0): np.array([0,0]),
	(0,1): np.array([0,0]),
	(-1,0): np.array([0,0]),
	(0,-1): np.array([0,0]),

	(1,1): np.array([0,0]),
	(-1,1): np.array([0,0]),
	(-1,-1): np.array([0,0]),
	(1,-1): np.array([0,0]),
	# non-diagonal 4 moves total
	(0, -2): h_moves['D'],
	(0, 2): h_moves['U'],
	(-2, 0): h_moves['L'],
	(2, 0): h_moves['R'],
	 # diagonal 8 moves total
	(-1, 2): h_moves['L'] + h_moves['U'],
	(-2, 1): h_moves['L'] + h_moves['U'],

	(1, 2): h_moves['R'] + h_moves['U'],
	(2, 1): h_moves['R'] + h_moves['U'],

	(-2, -1): h_moves['L'] + h_moves['D'],
	(-1, -2): h_moves['L'] + h_moves['D'],

	(2, -1): h_moves['R'] + h_moves['D'],
	(1, -2): h_moves['R'] + h_moves['D'],
}

for l in lines:
	dir, steps = l[0], int(l[1])
	for i in range(steps):
		h = h + h_moves[dir]
		t = t + t_moves_h_minus_t[tuple(h-t)]
		visited.add(tuple(t))

print(len(visited))
