def find_k_smallest(n, k, nums):
    result = []
    
    for num in nums:
        if len(result) < k:
            result.append(num)
        else:
            if num < max(result):
                result.remove(max(result)) 
                result.append(num) 
    return merge_sort(result)

def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:]) 
    n = m = k = 0
    empty_list = [0] * len(arr)
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            empty_list[k] = left[n]
            n += 1
        else:
            empty_list[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        empty_list[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        empty_list[k] = right[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = empty_list[i]
    return arr

print(find_k_smallest(9, 4, [3, 7, 4, 5, 6, 1, 15, 4, 2]))
