#众数查找算法
def findmain(arr):
    maj = None
    cont = 0
    for i in range(len(arr)):
        if cont == 0:
            maj = arr[i]
            cont = 1
        else:
            if maj == arr[i]:
                cont += 1
            else:
                cont -= 1
    #maj会是唯一可能的众数
    occur = 0
    for i in range(len(arr)):
        if arr[i] == maj:
            occur += 1
    return 2 * occur > len(arr)

#中位数合并算法，将两个有序向量的中位数合并
def median(S1, S2, lo1, lo2, n1, n2):
    if n1 > n2 : return median(S2, S1, lo2, lo1, n2, n1)
    if 2 * n1 < n2:
        return median(S1, S2, lo1, lo2 + (n2 - n1 - 1) / 2,
                    n1, n1 + 2 - (n2 - n1) % 2
                )
    # 计算中间位置
    mi1 = lo1 + n1 // 2
    mi2a = lo2 + (n1 - 1) // 2
    mi2b = lo2 + n2 - 1 - n1 // 2
    
    # 比较并递归
    if S1[mi1] > S2[mi2b]:
        # S1左半部分太大，缩小S1的范围到左半部分，扩大S2的范围到右半部分
        return median(S1, lo1, n1//2 + 1, S2, mi2a, n2 - (n1-1)//2)
    
    elif S1[mi1] < S2[mi2a]:
        # S1左半部分太小，扩大S1的范围到右半部分，缩小S2的范围到左半部分
        return median(S1, mi1, (n1+1)//2, S2, lo2, n2 - n1//2)
    
    else:
        # S1中间元素在S2的左右元素之间，保持S1不变，缩小S2的范围
        return median(S1, lo1, n1, S2, mi2a, n2 - (n1-1)//2 * 2)
