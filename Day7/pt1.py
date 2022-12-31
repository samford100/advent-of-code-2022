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

frontier = [head]
max_val = 100000
sum_ = 0
print('Running')
while len(frontier) > 0:
	e = frontier.pop()
	if e.size < max_val:
		sum_ += e.size
	frontier += e.child_dirs

print('------')
print(sum_)
