def standoffs(n, arr):
    heap = []  
    min_standoffs = 0  

    for arrival, departure in arr:
        while heap and heap[0] <= arrival:
            remote(heap[0], heap)
        insert(departure, heap)
        min_standoffs = max(min_standoffs, len(heap))

    return min_standoffs

print(standoffs(3, [[10, 20], [20, 25], [21, 30]])) 
print(standoffs(5, [[0, 10], [1, 5], [10, 15], [15, 20], [20, 30]])) 