#先用邻接表实现图的存储，然后从邻接表实现BFS
from collections import defaultdict, deque
def build_graph(edges = [(0,0), (1,1)]):
    #使用defaultdict(list)
    #他为不存储在的键自动生成一个默认值，这个地方默认是一个空list
    #edges随便给几个默认值
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
def bfs(graph, start = 0, n = 0):
    #visited 记录是否被访问过
    visited = [False] * n
    #记录父节点
    parent = {i: None for i in range(n)}
    #记录层级（距离起点的距离）
    level = {i: -1 for i in range(n)}
    
    queue = deque([(start, 0)])
    visited[start] = True #标记起点
    level[start] = 0
    
    while queue:
        #vertex 顶点
        vertex, current_level = queue.popleft()
        
        for neighbor in graph[vertex]:
            #如果邻居还没被访问过
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = vertex
                level[neighbor] = current_level + 1
                queue.append((neighbor, current_level+1))
    
    return parent, level, visited

# #使用bfs计算无权图中的顶点到顶点的最短路径
# 定理：顶点v在以s为根的BFS树中的深度d(v)等于从起始顶点s到v的最短路径长度。
# 证明：因为bfs发现顶点的顺序是按照深度的顺序发现的，BFS总是先访问比较近的顶点
# 深度是递增的

#找最长路径
#经过两次广度优先遍历：先从任意位置k出发找最远点a，然后从a出发找最远点b
#ab就是要找的最长路径
def find_diameter(edges, n):
    graph = build_graph(edges)
    #第一次
    parent1, level1, _  = bfs(graph, start=0, n = n)
    #从返回的字典里面找一下距离最远的那个顶点
    max_dist = -1
    farthest_vertex = 0
    for vertex, dist in level1.items():
        if dist > max_dist:
            max_dist = dist
            farthest_vertex = vertex
    
    #第二次BFS：从最远顶点出发
    parent2, level2, _ = bfs(graph, start=farthest_vertex, n=n)
    
    # 找到第二次BFS中的最远顶点
    diameter = -1
    end_vertex = 0
    for vertex, dist in level2.items():
        if dist > diameter:
            diameter = dist
            end_vertex = vertex

    #构建直径
    path = []
    #反向构建一下路径
    current = end_vertex
    while current is not None:
        path.append(current)
        current = parent2[current]
    
    #反转路径
    path.reverse()
    return diameter, path


#递归dfs
def dfs(graph, vertex, visited, parent, discovery_time, finish_time, time):
    #time是一个只有一个整数的列表，使用列表是为了在递归中保持引用，实现计数器的累加
    visited[vertex] = True
    time[0] += 1
    discovery_time[vertex] = time[0]
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            parent[neighbor] = vertex
            #递归访问邻居
            time = dfs(graph, vertex, visited, parent, discovery_time, finish_time, time)
    #更新完成时间
    time[0] += 1
    finish_time[vertex] = time[0]

