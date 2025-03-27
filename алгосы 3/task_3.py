def down(elem, arr):
    ind = arr.index(elem)
    while ind*2 + 1 < len(arr):
        left = 2 * ind + 1
        right =  2 * ind + 2

        smallest_ind = left
        if right < len(arr) and arr[right] < arr[left]:
            smallest_ind = right

        if arr[ind] > arr[smallest_ind]:
            arr[ind], arr[smallest_ind] = arr[smallest_ind], arr[ind]
            ind = smallest_ind
        else:
            break
            
def up(elem, arr):
    ind = arr.index(elem)
    while ind != 0 and arr[ind] < arr[(ind - 1) // 2]: 
        arr[ind], arr[(ind - 1) // 2] = arr[(ind - 1) // 2], arr[ind]
        ind = (ind - 1) // 2

def insert(val, arr):
    arr.append(val)
    up(val, arr)
    

def remote(val, arr):
    ind = arr.index(val)
    arr[ind], arr[-1] = arr[-1], arr[ind]
    arr.pop(-1)
    if ind < len(arr):
        down(arr[ind], arr)
    return val

def sliding_max(n ,arr, k):
    heap = []
    for elem in arr[: k]:
        insert(elem, heap)
    
    maximums = [heap[0]]
    
    for i in range(k, n):
        insert(arr[i], heap)
        remote(arr[i-k], heap)

        maximums.append(heap[0])
    
    return maximums

print(sliding_max(9, [0, 7, 3, 8, 4, 5, 10, 4, 6], 4))


