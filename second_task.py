def can_jump(n, k, a, max_jump):
    jumps = 0
    cur = 0
    while cur < n - 1:
        next_pos = min(cur + max_jump, n - 1)
        while next_pos > cur and a[next_pos] == "0":
            next_pos -= 1
        if next_pos == cur:
            return False
        cur = next_pos
        jumps += 1
        if jumps > k:
            return False
    return True

def min_jump(n, k, a):
    left = 1
    right = n - 1
    answer = n - 1
    while left <= right:
        mid = (left + right) // 2
        if can_jump(n, k, a, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
