class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = [1] * len(nums)

        for i in range(1, len(nums)):
            # prefix of current item is the product of everything before that point
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(len(nums) - 2, -1, -1):
            # suffix of a current item is the product of everything after a certain point
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            # product of a current item is the product of the prefix (product of everything before)
            # and the product of the suffix (product of everything after)
            product[i] = prefix[i] * suffix[i]

        return product

