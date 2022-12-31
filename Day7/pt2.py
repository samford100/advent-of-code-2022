from functools import reduce
from typing import List


class Dir:
	def __init__(self, name: str, parent):
		self.name = name
		self.parent = parent
		self.child_dirs = []
		self.child_files = []
		self.size = 0

	def find(self, name: str):
		# return the node with the name
		return list(filter(lambda x: x.name == name, self.child_dirs))[0]

	def get_size(self):
		size = sum(map(lambda file: file.size, self.child_files))
		size += sum(map(lambda dir: dir.get_size(), self.child_dirs))
		self.size = size
		return size

	def add(self, l: List[str]):
		if 'dir' in l:
			name = l[1]
			self.child_dirs.append(Dir(name, self))
		else:
			size, name = int(l[0]), l[1]
			self.child_files.append(File(name, size))

	def __str__(self):
		return f'{self.name} -> \n dirs: {list(map(lambda x: str(x), self.child_dirs))} \n files: {list(map(lambda x: str(x), self.child_files))}'


class File:
	def __init__(self, name: str, size: int):
		self.name = name
		self.size = size

	def __str__(self):
		return f'{self.name} is {self.size}'


head = Dir(None, None)
head.child_dirs = [Dir('/', head)]
cdir = head

with open('./Day7/input.txt') as f:
	lines = list(map(lambda l: l.strip().split(), f.readlines()))
	i = 0
	while i < len(lines):
		if '$' in lines[i]:
			if 'cd' in lines[i]:
				if '..' in lines[i]:
					cdir = cdir.parent
				else:
					name = lines[i][2]
					cdir = cdir.find(name)
				i += 1
			elif 'ls' in lines[i]:
				# find the next $ in the lines
				i += 1
				while i < len(lines) and '$' not in lines[i]:
					cdir.add(lines[i])
					i += 1
		else:
			print('Should not hit here')

head.get_size()
print(head.size)

disk_space = 70000000
required_space = 30000000

# 8,381,165 = 30,000,000 - (70,000,000 - 48, 381,165)

space_to_delete = required_space - (disk_space - head.size)
print(f'space to delete: {space_to_delete}')

max_val = 100000

sum_ = 0
print('Running')
candidates = []
frontier = [head]
while len(frontier) > 0:
	e = frontier.pop()
	candidates.append(e)
	frontier += e.child_dirs

print('------')
print(candidates)

smallest_surplus = 1000000000
smallest_candidate = None
for c in candidates:
	surplus = c.size - space_to_delete
	# want the smallest surplus
	if 0 < surplus < smallest_surplus:
		smallest_surplus = surplus
		smallest_candidate = c

print(smallest_candidate.size)

