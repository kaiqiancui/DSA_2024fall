def insertsort(data):
    for i in range(1, len(data)):
        key = data[i]
        if key >= data[i-1]:
            continue
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data
#二分查找版本
def bs_insertsort(data):
    for i in range(1, len(data)):
        key = data[i]
        left, right = 0, i
        
        while left < right:
            mid = (left + right) // 2
            if data[mid] <= key:
                left = mid + 1
            else:
                right = mid
        data[left+1 : i+1] = data[left, i]
        data[left] = key



#注释版本
def insertion_sort_duplicates(arr):
    """
    优化的插入排序算法，特别处理了重复元素和已排序序列的情况
    参数:
        arr: 需要排序的列表
    返回:
        arr: 排序后的列表
    时间复杂度: 最优 O(n)，平均 O(n^2)，最差 O(n^2)
    空间复杂度: O(1)
    """
    # 从第二个元素开始遍历，因为第一个元素可以认为是已排序的
    for i in range(1, len(arr)):
        # 保存当前要插入的元素
        key = arr[i]
        
        # 优化1：检查是否已经在正确的位置
        # 如果当前元素大于或等于前一个元素，说明顺序正确，无需移动
        # 这个优化对于已经排序的序列或部分排序的序列特别有效
        if key >= arr[i-1]:
            continue
        
        # 如果需要插入，则从当前位置的前一个元素开始向前比较
        j = i - 1
        
        # 优化2：将大于key的元素向后移动
        # 当没有到达列表开头(j >= 0)且当前元素大于key时继续循环
        while j >= 0 and arr[j] > key:
            # 将较大的元素向后移动一位
            arr[j + 1] = arr[j]
            # 继续向前比较
            j -= 1
            
        # 找到了key应该插入的位置
        # j+1 的位置就是key应该在的位置，因为：
        # 1. 要么j变成了-1，说明key应该插入到最前面
        # 2. 要么找到了一个小于等于key的元素，key应该插入到其后面
        arr[j + 1] = key
    
    # 返回排序后的列表
    return arr