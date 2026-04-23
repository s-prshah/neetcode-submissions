class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_vals = {}

        for i in range(len(nums)):
            possible_vals[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in possible_vals and i != possible_vals[difference]:
                smaller_index = min(i, possible_vals[difference])
                larger_index = max(i, possible_vals[difference])
                return [smaller_index, larger_index]

        