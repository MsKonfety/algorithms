def find_equal(A, B):
    def binary_search(arr, target):
        left = 0
        right = 1
        while arr[right] < target and right != len(arr) - 1:
            if right ** 2 > len(arr)-1:
                right = len(arr) - 1
            else:
                right *= 2

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    result = [binary_search(A, b) for b in B]
    return result

A = [1, 2, 4, 5, 6, 8, 10]
B = [0, 3, 5, 7, 10, 12]

print(find_equal(A, B))
