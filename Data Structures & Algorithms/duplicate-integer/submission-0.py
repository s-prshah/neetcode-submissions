class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracked = set()
        for i in nums:
            if i in tracked:
                return True
            tracked.add(i)
        return False
        