class PriorityDeque:
    def __init__(self):
        self._box = []
    
    def _left_child(self, i):
        left = 2 * i + 1
        return left if left < len(self._box) else -1
    
    def _right_child(self, i):
        right = 2 * i + 2
        return right if right < len(self._box) else -1
    
    def _parent(self, i):
        return (i - 1) >> 1 if i > 0 else -1
    
    def _sift_up(self, i):
        box = self._box
        val = box[i]
        while i > 0:
            parent = self._parent(i)
            if box[parent] >= val:
                break
            box[i] = box[parent]
            i = parent
        box[i] = val
    
    def _sift_down(self, i):
        box = self._box
        size = len(box)
        val = box[i]
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < size and box[left] > box[largest]:
                largest = left
            if right < size and box[right] > box[largest]:
                largest = right
                
            if largest == i:
                break
            box[i] = box[largest]
            i = largest
        box[i] = val
    
    def push(self, val):
        self._box.append(val)
        self._sift_up(len(self._box) - 1)
    
    def top(self):
        if not self._box:
            raise IndexError("Heap is empty")
        return self._box[0]
    
    def pop(self):
        if not self._box:
            raise IndexError("Heap is empty")
        
        box = self._box
        result = box[0]
        box[0] = box[-1]
        box.pop()
        if box:  # 如果堆不为空，需要进行下沉操作
            self._sift_down(0)
            
        return result
    
    def empty(self):
        return len(self._box) == 0
    
    def size(self):
        return len(self._box)
