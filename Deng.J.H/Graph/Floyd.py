#全源最短路
from math import inf
from functools import cache
#会超时的递归算法    
def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
    w = [[inf for _ in range(n)] for _ in range(n)]
    for x, y, wt in edges:
        w[x][y] = w[y][x] = wt
        
    def dfs(k, i, j):
            #所有节点的编号都小于k
            #i, j 的最短路径长度
        if k < 0:
            return w[i][j]
            
        return min(dfs(k-1, i, j), dfs(k-1, i, k) + dfs(k-1, k, j))

    #记忆化搜索缩短时间
    #python可以选择使用装饰器解决缓存问题
    @cache
    def cache_dfs(k, i, j):
        if k < 0:
            return w[i][j]
        return min(dfs(k-1, i, j), dfs(k-1, i, k) + dfs(k-1, k, j))
    
    #手写记忆化搜索
    memo = {}
    def memo_dfs(k, i, j):
        key = (k, i, j)
        if key in memo:
            return memo[key]
        
        if k < 0:
            return w[i][j]
        
        result = min(dfs(k-1, i, j), dfs(k-1, i, k) + dfs(k-1, k, j))
        memo[key] = result
        
        return result
    
    #枚举做法
    f = [[[0] * n for _ in range(n)]for _ in range(n + 1)]
    f[0] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f[k + 1][i][j] = min(f[k][i][j], f[k][i][k]  + f[k][k][j])
                
    #节省空间的写法
    #根据一些复杂的推导，可以实现把第一个维度去掉？
    ans = 0
    min_cnt = inf
    for i in range(n):
        cnt = 0
        for j in range(n):
            if j != i and dfs(n - 1, i, j) <= distanceThreshold:
                cnt += 1
        if cnt <= min_cnt:  # 相等时取最大的 i
            min_cnt = cnt
            ans = i
    return ans
