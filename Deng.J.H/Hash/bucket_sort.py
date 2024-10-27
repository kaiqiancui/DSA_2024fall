N = 100010
w = n = 0; #W表示数组最大值，n表示数组实际的大小
a = [] * N #主数组，存储待排序的数据
bucket = [[] for i in range(N)]

def insertion_sort(A):
    #插入排序
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1;
        while(j >= 0 and A[j] > key):
            #比要插入的元素大的元素都往后移一位
            A[j+1] = A[j]
            j -= 1
        A[j + 1] = key
def bucket_sort():
    """
    桶排序算法
    使用全局变量:
        w: 数组中的最大值
        n: 数组的大小
        a: 待排序的数组
        bucket: 桶数组
    """
    bucket_size = w // n + 1
    for i in range(0, n):
        bucket[i].clear()
        
    for i in range(1, n+1):
        bucket_index = a[i] // bucket_size #计算应该放到第几个桶
        bucket[bucket_index].append(a[i]) #
    #对每个桶进行排序，将结果合并回原数组
    p = 0 #原数组写入位置
    for i in range(0, n):
        insertion_sort(bucket[i]) #对每个桶排序
        #将排序后的桶的元素写回原数组
        for j in range(0, len(bucket[i])):
            a[p] = bucket[i][j]
            p+= 1
            
    
    
    