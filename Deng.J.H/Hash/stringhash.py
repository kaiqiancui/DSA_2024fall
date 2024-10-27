#from luogu P3370
BASE = 131 #字符串进位基数
##131 和 13331是常用的基数
PRIME = 233317
#避免哈希冲突用的质数
MOD = 212370440130137957

def string_hash(s: str) -> int:
    """
    计算字符串的哈希值
    参数:
        s: 输入的字符串
    返回:
        该字符串的哈希值
    """
    ans = 0
    #对字符串的每个字符进行哈希计算
    #公式：hash = (hash * BASE + ord(char))%MOD + PRIME
    for char in s:
        ans = (ans * BASE + ord(char)) % MOD + PRIME
    return ans

def main():
    #字符串的数量
    n = int(input())
    #存储每个字符串的hash
    hash_set = set()
    for _ in range(n):
        s = input()
        hash_set.add(string_hash(s))
    
    #计算不同的hash的数量
    diff = len(hash_set)
    print(diff)
if __name__ == "__main__":
    main()


