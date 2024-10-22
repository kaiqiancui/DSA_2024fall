import os

class Bitmap:
    def __init__(self, n=8, file=None):
        self.init(n)
        if file:
            self.load_from_file(file)

    def init(self, n):
        self.N = (n + 7) // 8
        #计算存储n个二进制位所需要的字节数
        self.M = bytearray(self.N)
        self._sz = 0 
        #下划线表示是类内的属性，不能从外部访问
        #表示有效/激活 设为1的位数
    def load_from_file(self, file):
        """
        从文件中加载Bitmap数据。
        参数:
        file (str): 要加载的文件路径
        """
        # 以二进制读取模式打开文件
        with open(file, 'rb') as f:
            # 读取指定数量的字节并创建bytearray
            # self.N 是Bitmap所需的字节数
            # f.read(self.N) 读取self.N个字节
            # bytearray() 将读取的字节转换为可变字节数组
            self.M = bytearray(f.read(self.N))

        # 重新计算设置为1的位的数量
        # range(len(self.M) * 8) 生成一个范围，覆盖所有可能的位索引
        # self.test(k) 检查索引k处的位是否被设置
        # sum() 计算所有被设置位的总和
        self._sz = sum(self.test(k) for k in range(len(self.M) * 8))
    def size(self):
        return self._sz

    def reset(self):
        self.M = bytearray(self.N)
        self._sz = 0
        
    def set(self, k):
        """
        在Bitmap中设置第k位为1。

        参数:
        k (int): 要设置的位的索引

        说明:
        - 如果第k位已经是1,则直接返回
        - 否则,设置第k位为1,并更新计数器
        """
        # 检查第k位是否已经被设置
        if self.test(k):
            return
        
        # 确保Bitmap有足够的空间来设置第k位
        self.expand(k)
        
        # 增加已设置位的计数
        self._sz += 1
        # 设置第k位为1
        # k >> 3 计算字节索引（相当于 k // 8）
        # k & 0x07 计算在字节内的位索引（相当于 k % 8）
        # 0x80 >> (k & 0x07) 创建一个掩码，只有目标位为1
        # |= 执行按位或操作，设置目标位为1
        self.M[k >> 3] |= (0x80 >> (k & 0x07))

    def clear(self, k):
        """
        在Bitmap中清除第k位（设置为0）。

        参数:
        k (int): 要清除的位的索引

        说明:
        - 如果第k位已经是0，则直接返回
        - 否则，清除第k位，并更新计数器
        """
        # 检查第k位是否已经是0
        if not self.test(k):
            return
        
        # 确保Bitmap有足够的空间来操作第k位
        self.expand(k)
        
        # 减少已设置位的计数
        self._sz -= 1
        
        # 清除第k位（设置为0）
        # ~(0x80 >> (k & 0x07)) 创建一个掩码，只有目标位为0，其他位为1
        # &= 执行按位与操作，清除目标位
        self.M[k >> 3] &= ~(0x80 >> (k & 0x07))

    def test(self, k):
        """
        测试Bitmap中第k位的状态。

        参数:
        k (int): 要测试的位的索引

        返回:
        bool: 如果第k位是1返回True，否则返回False

        说明:
        - 确保Bitmap有足够的空间来测试第k位
        - 使用位操作来检查指定位的状态
        """
        # 确保Bitmap有足够的空间来测试第k位
        self.expand(k)
        
        # 测试第k位的状态
        # & 执行按位与操作
        # bool() 将结果转换为布尔值
        return bool(self.M[k >> 3] & (0x80 >> (k & 0x07)))

    def dump(self, file):
        """
        将Bitmap的内容写入文件。

        参数:
        file (str): 要写入的文件路径

        说明:
        - 以二进制写入模式打开文件
        - 将Bitmap的字节数组直接写入文件
        """
        # 以二进制写入模式打开文件
        with open(file, 'wb') as f:
            # 将Bitmap的字节数组写入文件
            f.write(self.M)

    def bits2string(self, n):
        """
        将Bitmap的前n位转换为字符串表示。

        参数:
        n (int): 要转换的位数

        返回:
        str: 由'0'和'1'组成的字符串，表示Bitmap的状态

        说明:
        - 确保Bitmap有足够的空间来表示前n位
        - 使用生成器表达式和join方法创建字符串
        """
        # 确保Bitmap有足够的空间来表示前n位
        self.expand(n - 1)
        
        # 使用生成器表达式创建字符串
        # 对于每一位，如果被设置则用'1'表示，否则用'0'表示
        return ''.join('1' if self.test(i) else '0' for i in range(n))

    def expand(self, k):
        """
        如果需要，扩展Bitmap的大小以容纳第k位。

        参数:
        k (int): 需要容纳的位索引

        说明:
        - 如果当前大小足够，直接返回
        - 否则，创建一个新的、更大的Bitmap，并复制旧数据
        """
        # 检查当前大小是否足够
        if k < 8 * self.N:
            return
        
        # 保存旧的大小和数据
        old_N = self.N
        old_M = self.M
        
        # 创建一个新的、更大的Bitmap
        # 新大小是原来的两倍，但至少要能容纳k
        self.init(2 * k)
        
        # 将旧数据复制到新的Bitmap中
        self.M[:old_N] = old_M
