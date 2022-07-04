class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        nextSmallerElement,previousSmallerElement = [0]*(len(heights)) , [0]*(len(heights))
        n = len(heights)
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            nextSmallerElement[i] = stack[-1] if len(stack) != 0 else n
            stack.append(i)
        
        
        stack = []
        
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]]>=heights[i] :
                stack.pop()
            previousSmallerElement[i] = stack[-1] if len(stack) != 0 else -1
            stack.append(i)
        
        ans =  0 
        # print(nextSmallerElement)
        # print(previousSmallerElement)
        ans = max(ans, nextSmallerElement[0]* heights[0])
        # print(ans)
        for i in range(1,n-1):
            area =  (nextSmallerElement[i] - previousSmallerElement[i] -1 )*(heights[i])
            ans = max(ans, area)
            # print(area,i,ans)
            
        ans = max(ans,(n -1 - previousSmallerElement[n-1]) * heights[-1])
        # print(ans)
        return ans