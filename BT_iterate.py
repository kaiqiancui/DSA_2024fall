'''This code implements the front-middle-post order 
traversal of a binary tree using iteration 
(non-recursive implementation)'''
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
class Binary_tree:
    def __init__(self):
        self.root = None
        pass
    def insert(self,root, value):
        pass
    def pre_order(self):
        result = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current.right)
                result.append(current.value)
                current = current.left
            #current
            current = stack.pop()
        return result        
    def in_order1(self):
        '''by assistant stack'''
        result = []
        stack = []
        current = self.root
        while current or stack:
            #left
            while current:
                stack.append(current)
                current = current.left
            #current
            current = stack.pop()
            result.append(current.value)
            
            #right
            current = current.right
        return result
    
    def get_successor(self, node):
        '''search by lower_bound and upper_bound'''
        if node.right:
            current = node
            while current.left:
                current = current.left
            return current
        else:
            parent = node.parent
            while parent and parent.right == node:
                node = parent
                parent = parent.parrent
            return parent
    def in_order2(self):
        '''very similar to the first method'''
        stack = []
        res = []
        cur = self.root
        while True:
            if cur:
                stack.append(cur)

                cur = cur.left
            elif not stack:
                cur = stack.pop()
                res.append(cur.value)
                cur = cur.right
            else:
                break
        return res
    def in_order3(self):
        '''no stack, space less, but time more(for__get__successor)'''
        back_track = False
        res = []
        ''' have python done a bottom to top backtracking
            if back_track
            current node->left tree has traversed
        '''
        cur = self.root
        while True:
            if cur.left and not back_track:
                cur = cur.left
            else:
                res.append(cur.value)
            if cur.right:
                cur = cur.right
                back_track = False
            else:
                cur = self.get_successor(cur)
                if not cur:
                    break
                back_track = True
        return res
    def high_looked_virtual_leaf(self, stack):
        '''used for past_orfer_traverse'''
        cur = stack[-1]
        while cur:
            if cur.left:
                if cur.right:
                    stack.append(cur.right)
                stack.appent(cur.left)
            else:
                stack.append(cur.right)
        stack.pop()
        
    def past_order(self):
        cur = self.root
        res = []
        stack = []
        if cur:
            stack.append(cur)
        while not stack:
            if stack[-1] is not cur.parent:
                #now the top of stack is cur's right brother
                #our iterate will get into right tree
                self.high_looked_virtual_leaf(stack)
            cur = stack.pop()
            res.append(cur.value)
        return res
        