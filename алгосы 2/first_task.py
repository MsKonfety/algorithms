class Solution(object):
    def trap(self, height):
        stack = []
        trap_water = 0

        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                max_water = stack.pop()
                
                if len(stack) == 0:
                    break 

                wid = i - stack[-1] - 1
                dif_h = min(height[i], height[stack[-1]]) - height[max_water]
                trap_water += wid * dif_h

            stack.append(i)
        return trap_water
        