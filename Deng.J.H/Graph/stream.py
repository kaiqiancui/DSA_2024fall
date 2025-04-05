#实现最大流问题中的标号算法
#复现离散数学中的表示
from typing import List
from collections import deque
from math import inf
def FordFulkersonLabeling(graph:List[List[int]],begin:int, end:int):
    #graph的形式：sheet[i][j] = c #表示从i到j有个c大小的流
    #sheet[j][i] = 0
    #不存在边：inf
    n = len(graph)
    dq = deque(begin)
    while 1:
        #新一轮标号开始
        sign = [False] * n
        while dq:
            i = dq.popleft()
            for j in range(n):
                if graph[i][j] != inf and not sign:
                    pass