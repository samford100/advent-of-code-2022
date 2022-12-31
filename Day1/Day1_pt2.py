import heapq

cur_cals = 0
cal_heap = []

with open('./input.txt') as f:
   while l := f.readline():
       if l == '\n':
           # it's a minheap, so push the negative
           heapq.heappush(cal_heap, -cur_cals)
           cur_cals = 0
           continue
       val = int(l)
       cur_cals += val

total = -1 * (heapq.heappop(cal_heap) + heapq.heappop(cal_heap) + heapq.heappop(cal_heap))
print(total)






