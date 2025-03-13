class Solution(object):
    def largestRectangleArea(self, heights):
        
        stack = [[0, 0]]
        maximum = 0

        for i in range(len(heights)):
            if heights[i] >= heights[-1]:
                stack.append([1, heights[i]])

            else:
                while heights[i] <  stack[-1][1]:
                    stack[-2] = [stack[-2][0] + stack[-1][0], stack[-2][1]]
                    square = stack[-2][0] * stack[-2][1]
                    stack.pop(-1)
                    maximum = max(maximum, square)
                stack.append([1, heights[i]])
            maximum = max(maximum, heights[i])
        return maximum