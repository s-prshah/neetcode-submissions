class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        to_return = right
        print(right)

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for i in piles:
                totalTime += math.ceil(float(i) / mid)
            if totalTime <= h:
                to_return = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return to_return