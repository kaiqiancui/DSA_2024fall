#归并排序
def merge(arr, low, mid, high):
    #合并arr[low..mid] arr[mid+1..high]
    B = arr.copy()
    i = low #两个数组的指针
    j = mid + 1
    k = low #结果数组当前位置
    
    while i <= mid and j <= high:
        if B[i] <= B[j]:
            arr[k] = B[i]
            i += 1
        else:
            arr[k] = B[j]
            j += 1
        k += 1
    #左半剩余
    while i <= mid:
        arr[k] = B[i]
        i += 1
        k += 1
    while j <= high:
        arr[k] = B[j]
        j += 1
        k += 1
def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid ,high)
