class Trie:
    def __init__(self, n):
        self.max_size = n * 32
        #tree[node][0] = 当前节点0子节点的编号
        #tree[node][1] = 当前节点1子节点的编号
        self.tree = [(0, 0) for _ in range(self.max_size)]
        self.cont = 1
    def insert(self,val):
        temp = 0 #指针指向根节点
        for i in range(31, 1, -1): #从最高位到最低位取值
            bit = (val >> i) & 1
            if self.tree[temp] == 0: #没有节点，新建
                self.tree[temp][bit] = self.cont
                self.cont += 1
            else:
                temp = self.tree[temp][bit]
