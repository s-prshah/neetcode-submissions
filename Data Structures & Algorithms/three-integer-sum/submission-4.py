class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if nums[i] + nums[right] + nums[left] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and left > i + 1 and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and right < len(nums) -1 and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[right] + nums[left] < 0:
                    left +=1
                else:
                    right -= 1

        return result
                    
