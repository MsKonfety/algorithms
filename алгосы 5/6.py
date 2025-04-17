def merge_and_count(arr, addit_arr, left, mid, right):
    i = left  
    j = mid + 1
    k = left 
    inversions = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            addit_arr[k] = arr[i]
            i += 1
        else:
            addit_arr[k] = arr[j]
            inversions += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        addit_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        addit_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = addit_arr[i]

    return inversions

def sort_and_count(arr, addit_arr, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2

        inversions += sort_and_count(arr, addit_arr, left, mid)
        inversions += sort_and_count(arr, addit_arr, mid + 1, right)
        inversions += merge_and_count(arr, addit_arr, left, mid, right)

    return inversions

arr = [3, 2, 2]
arr_size = len(arr)
print(sort_and_count(arr, [0] * arr_size, 0, arr_size - 1))