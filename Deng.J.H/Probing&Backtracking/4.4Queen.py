class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x or \
            self.y == other.y or \
            self.x + self.y == other.x + other.y or\
            self.x - self.y == other.x - other.y
    def __ne__(self, value):
        return not self.__eq__(value)

def placeQueens(n):
    solu = [] #stack for solution
    q = Queen(0 ,0)
    nChack = 0 #record comparison times
    nSolu = 0 #recode the nums of solutions
    
    while True:
        if n <= solu.__len__() or n <= q.y:
            #if out of range
            if not solu:
                break
            q = solu.pop()#backtrack next line
            q.y += 1#prob next col
            #backtracking
        else:
            #begin to prob next line
            while q.y < n and q in solu:
                q.y += 1
                nChack += 1
            
            if q.y < n:
                solu.append(Queen(q.x, q.y))
                if n <= len(solu):
                    nSolu += 1
                    print(f"解 {nSolu}:", [(queen.x, queen.y) for queen in solu])
                    q.x += 1
                    q.y = 0 #prob from col = 0

        if not(0 < q.x or q.y < n):
            break

placeQueens(8)
