class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        elements = path.split('/')
        stack = []
        for elem in elements:
            if elem == '.' or elem == '':
                continue
            elif elem == '..':
                if len(stack) >= 1:
                    del stack[-1]
            else:
                stack.append(elem)
        result = '/' + '/'.join(stack) 
        return result