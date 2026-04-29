class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        lower = [0] * n
        upper = [0] * n

        lower[0] = height[0]
        upper[n-1] = height[n-1]

        for i in range(1, n):
            lower[i] = max(lower[i-1], height[i])
        
        for i in range(n - 2, -1, -1):
            upper[i] = max(upper[i+1], height[i])
        
        print(lower)
        print(upper)

        to_return = 0

        for i in range(n):
            to_return += min(lower[i], upper[i]) - height[i]

        return to_return
