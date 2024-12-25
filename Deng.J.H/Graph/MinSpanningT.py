#最小生成树 kruskal 
#并查集 + 堆
import heapq
n, m = map(int, input().split())
hp = []
for _ in range(n):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    heapq.heappush(hp, (z, x, y))

parent = [range(n)]

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

sum = 0

while hp:
    z, x, y = heapq.heappop()
    x_parent = find(x)
    y_parent = find(y)
    if x_parent != y_parent:
        sum += z
        parent[x_parent] = parent[y_parent]

cont_block = 0
for i in range(n):
    if i == find(i):
        cont_block += 1

if cont_block == 1:
    print(sum)
else:
    print("orz")

