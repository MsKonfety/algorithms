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



def fast_sum(n, arr):
    heap = []
    min_time = 0
    
    for number in arr:
        insert(number, heap)

    while len(heap) > 1:
        first = remote(heap[0], heap)
        second = remote(heap[0], heap)

        addition_time = first + second
        min_time += addition_time
        insert(addition_time, heap)

    return min_time

print(fast_sum(5, [5, 2, 3, 4, 6]))