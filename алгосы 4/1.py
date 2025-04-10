class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  
            self.heapify(nums, i, 0) 
        return nums
    
    def heapify(self, nums, size, ind):
        l = ind
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        
        if left < size and nums[left] > nums[l]:
            l = left
        
        if right < size and nums[right] > nums[l]:
            l = right
        
        if l != ind:
            nums[ind], nums[l] = nums[l], nums[ind] 
            self.heapify(nums, size, l)