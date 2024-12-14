#使用邻接矩阵存储无向图，图是上半角的

class TriangularGraph:
    def __init__(self, n):
        self.n = n
        self.matrix = [0] * (n * (n - 1)//2)
    
    def _get_index(self, i, j):
        #二维坐标转一维索引
        #i：行   j:列
        #存储上半角：行序号小于列序号
        if i > j:
            i, j = j, i
        #计算索引
        #return sum(n - 1, n - 2, ... n - i) + j - i - 1
        return (i * (2 * self.n - i - 1)) // 2 + (j - i - 1)
