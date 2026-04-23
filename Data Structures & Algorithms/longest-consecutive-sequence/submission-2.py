class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        frequencies = set()

        for i in range(len(nums)):
            frequencies.add(nums[i])
        
        max_element = max(nums)

        i = min(nums)

        max_length = 1
        length = 1

        while i <= max_element:
            if i in frequencies and (i+1) in frequencies:
                length+=1
                print(length)
            else:
                if length > max_length:
                    max_length = length
                length = 1
            i +=1
        return max_length



        
        