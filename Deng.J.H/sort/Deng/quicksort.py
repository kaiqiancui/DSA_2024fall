def partition_simple(arr, lo, hi):
    #快速划分算法的基础实现
    import random
    rand_idx = random.randint(lo, hi)
    #将随机选取的元素与首元素进行交换
    arr[lo], arr[rand_idx] = arr[rand_idx], arr[lo]
    #备份轴点
    pivot = arr[lo]
    
    #扫描
    while lo < hi:
        #右到左
        while lo < hi and pivot <= arr[hi]:
            hi -= 1
        arr[lo] = arr[hi]
        #左到右
        while lo < hi and arr[lo] <= pivot:
            lo += 1
        arr[hi] = arr[lo]
    
    #lo = hi 是轴点的最终位置
    arr[lo] = pivot
    return lo

