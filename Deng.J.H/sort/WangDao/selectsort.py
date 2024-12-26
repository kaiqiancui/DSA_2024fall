#选择排序
#* 简单选择排序
def select_sort(arr):
    n = len(arr)
    for i in range(n - 1): 
        #前 i - 1 项是已经排序的序列
        #最小元素的位置
        min_idx = i
        #无论序列什么情况 都要比较 这个n^2必须要花
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                #不断的找最小的那个
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

#* 堆排序
#? 先将n个元素建成堆，然后从堆头不断的取元素，剩下的元素再上滤
def build_max_heap(arr):
    #建堆算法
    n = len(arr)
    #从最后一个非叶节点开始调整
    for i in range(n //2, -1 -1):
        head_adjust(arr, i, n)

def head_adjust(arr, k, length):
    temp = arr[k]#当前根节点的值
    #i指向k的左子节点
    i = 2 * k + 1
    while i < length:
        #如果右大于左， i指向右
        if i + 1 < length and arr[i] < arr[i + 1]:
            i += 1
        #如果根节点大于最大的子节点 结束调整
        if temp >= arr[i]:
            k = i
            i = 2 * k + 1
    arr[k] = temp

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n-1, 0, -1):
        #堆顶元素和堆低元素交换，最大的挪到最后面
        arr[0], arr[i] = arr[i], arr[0]
        head_adjust(arr, 0, i)
    return arr