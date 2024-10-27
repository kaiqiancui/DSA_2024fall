class Trie:
    class TrieNode:
        """
        Trie树的节点类
        使用字典存储子节点，支持任意字符
        """
        def __init__(self):
            """
                children: 存储子节点的字典
                is_end: 标记该节点是否是一个单词的结尾
                count: 经过该节点的单词数量
            """
            self.children = {}  # 子节点字典
            self.is_end = False  # 是否是单词结尾
            self.count = 0  # 统计经过该节点的单词数量
            self.word_count = 0  # 以该节点结尾的单词数量
    def __init__(self):
        self.root = self.TrieNode()
        self.total_word = 0 #总单词
    def insert(self, word:str) -> None:
        if not word:
            return
        #node遍历标识
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            
            node = node.children[char]
            node.count+= 1
        node.is_end = True
        node.word_count += 1
        self.total_word += 1
    
    def _find_node(self, prefix:str) ->TrieNode:
        """查找到达指定前缀的最后一个节点"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char] #继续深入
        return node #node包含prefix的最后一个节点
    
    def search(self, word:str) -> bool:
        #返回值表示是否匹配
        node = self._find_node(word)
        # if not node:
        #     return False
        # else:
        #     return node.is_end
        return node is not None and node.is_end
    def starts_with(self, prefix: str) -> bool:
        """
        检查是否存在以给定前缀开始的字符串
        """
        return self._find_node(prefix) is not None
    def count_prefix(self, prefix: str) -> int:
        """
        统计以指定前缀开始的字符串数量
        """
        node = self._find_node(prefix)
        return node.count if node else 0
    def delete(self, word: str) -> bool:
        """
        从字典树中删除一个单词
        """
        def _delete_helper(node: Trie.TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                node.word_count -= 1
                return True

            char = word[depth]
            if char not in node.children:
                return False

            deleted = _delete_helper(node.children[char], word, depth + 1)
            if deleted:
                node.children[char].count -= 1
                if node.children[char].count == 0:
                    del node.children[char]
            return deleted

        if _delete_helper(self.root, word, 0):
            self.total_words -= 1
            return True
        return False
