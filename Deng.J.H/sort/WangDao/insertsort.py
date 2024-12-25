##插入排序：稳定算法
#? 直接插入排序 折半插入排序 希尔排序

#* 直接插入排序
#* 稳定算法， 复杂度 n - n^2
def A_insert_sort(A):
    n = len(A)
    A.insert(0, None) #哨兵
    
    for i in range(2, n+1):
        if A[i] < A[i - 1]:
            #复制为哨兵
            A[0] = A[i]
            #要挪动的初始位置
            j = i - 1
            
            #哨兵的作用：省略了边界检查
            while A[0] < A[j]:
                A[j+1] = A[j]
                j -= 1
            
            A[j + 1] = A[0]
    A.pop(0)
    return A

#* 折半插入排序
def B_insert_sort(A):
    n = len(A)
    for i in range(1, n):
        temp = A[i]
        #二分 终止时low > high
        #high指向最后一个小于等于temp的位置
        #low指向第一个大于temp的位置
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high) // 2
            if A[mid] > temp:
                high = mid - 1
            else:
                low = mid + 1 #在相同的数字后面进行插入，保证有序性
        #循环结束后正确的插入位置：high + 1
        for j in range(i-1, high, -1): #倒着循环
            #for j = i - 1; j >= high + 1; j--
            A[j + 1] = A[j]
        A[high + 1] = temp
    return A

#* 希尔排序 不稳定算法
def shellsort(arr):
    #为了和c保持一致，使用哨兵
    A = [0] + arr[:]
    n = len(A) - 1
    dk = n // 2 #增量序列
    
    while dk >= 1:
        for i in range(dk + 1, n + 1):
            #和自己的上一位比较(已排序好的序列)
            #如果比自己的上一位大，说明不用做插入排序，直接放进去就可以
            if A[i] < A[i - dk]:
                temp = A[i]
                j = i - dk
                while j > 0 and temp < A[j]:
                    A[j + dk] = A[j]
                    j -= dk
                #经过while循环，设应该放的位置是target
                #j = target - dk
                A[j + dk] = temp
        dk //= 2
    return A[1:]
