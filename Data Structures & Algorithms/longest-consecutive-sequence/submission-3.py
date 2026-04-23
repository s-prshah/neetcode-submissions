class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        frequencies = set()

        for i in range(len(nums)):
            frequencies.add(nums[i])
        
        max_length = 0

        for i in range(len(nums)):
            if (nums[i]-1) not in frequencies:
                length = 1
                while (nums[i] + length) in frequencies:
                    length += 1
                max_length = max(length, max_length)
        
        return max_length



        
        