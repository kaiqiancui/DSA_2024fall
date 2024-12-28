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


#最小生成树prim算法：
def prim(graph):    
    """
    graph: 字典的字典，表示无向图的邻接矩阵
        格式: {节点1: {节点2: 权重, 节点3: 权重, ...}, ...}
    return:
    mst: 最小生成树的边集合，格式为 [(节点1, 节点2, 权重), ...]
    """
    if not graph:
        return []
    visited = set() #保存已经加入最小生成树中的节点
    mst = [] #return
    
    node = list(graph.keys())
    n = list(node)
    
    start_node = node[0]
    visited.add(start_node)
    
    while len(visited) < n:
        min_edge = None
        min_weight = float('inf')
        min_node = None
        
        for node in visited:
            for neighbor, weight in graph[node].items():
                if neighbor not in visited and weight < min_weight:
                    min_edge = (node, neighbor)
                    min_weight = weight
                    min_node = neighbor
        if min_node:
            visited.add(min_node)
            mst.append((*min_edge, min_weight))
        else:
            #找不到最小边说明图不连通
            break
    return mst