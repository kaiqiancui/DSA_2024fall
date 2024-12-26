#基数排序
def redix_sort(arr):
    if not arr:
        return arr
    #从最大数确定位数
    max_num = max(arr)
    #位数计数
    exp = 1
    while max_num // exp > 0:
        conting_sort(arr, exp)
        exp *= 10
    return arr

def conting_sort(arr, exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    
    i = n - 1
    while i >= 0:
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

