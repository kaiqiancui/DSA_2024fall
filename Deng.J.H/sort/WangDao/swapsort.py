#* 冒泡排序 快速排序
#* 冒泡排序 稳定排序 交换的时候只交换相邻的
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        #标记是否发生了交换
        flag = False
        for j in range(n - 1, i, -1):#从后向前比较
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                flag = True
        if not flag:#提前叫停
            return arr
    return arr

#* 快速排序 不稳定算法
def quick_sort(arr, low, high):
    #递归的主函数
    if low < high:
        pivot_pos = partition(arr, low, high)
        quick_sort(arr, low, pivot_pos -1)
        quick_sort(arr, pivot_pos + 1, high)
    return arr
def partition(arr, low, high):
    pivot = arr[low] #挖空low
    while low < high:
        #从右向左找第一个小于pivot的元素
        while low < high and arr[high] > pivot:
            high -= 1
        arr[low] = arr[high]
        
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    
    arr[low] = pivot #low high合一 最终防止pivot的位置
    
    return low