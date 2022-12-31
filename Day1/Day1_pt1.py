max_cals = 0
cur_cals = 0

with open('./input.txt') as f:
   while l := f.readline():
       if l == '\n':
           max_cals = max(max_cals, cur_cals)
           cur_cals = 0
           continue
       val = int(l)
       cur_cals += val

print(max_cals)






