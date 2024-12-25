#简单版本
def merge_sort_simple(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort_simple(arr[ : mid])
    right = merge_sort_simple(arr[mid : ])
    return merge_simple(left, right)

def merge_simple(left, right):
    #合并算法
    result = []
    i =  j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j] :
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #当切片操作元素越界时，会产生空列表而不是报错
    result.append(left[i:])
    result.append(right[i:])
