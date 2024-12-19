
from collections import deque
from collections import defaultdict
from math import inf
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        #求解所有路径中最长的一个
        
        #邻接矩阵
        g = [[inf for _ in range(n)] for _ in range(n)]
        for x, y, d in times:
            g[x][y] = d
        
        #初始化
        #K是初始节点
        dis = [inf] * n
        ans = dis[k] = 0
        done = [False] * n
        
        while True:
            #节点指针
            x = -1
            for i, ok in enumerate(done):
                #还没有确定最短路径的节点
                if not ok and (x < 0 or dis[i] < dis[x]):
                    #找还没确定最短路径的节点里最近的一个
                    x = i
            if x < 0:
                #所有的节点都确定了最短路径
                return ans
            
            if dis[x] == inf:
                #去不了
                return -1

            ans = dis[x]
            
            done[x] = True
            
            for y, d in enumerate(g[x]):
                #更新x的邻居的最短路
                dis[y] = min(dis[y], dis[x] + d)
                