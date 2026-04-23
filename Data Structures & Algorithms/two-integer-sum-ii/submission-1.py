class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        all_nums = {}

        for i in range(len(numbers)):
            all_nums[numbers[i]] = i + 1
        print(all_nums)

        to_return = [0, 0]

        for i in range(len(numbers)):
            print(all_nums[numbers[i]] != (i + 1))
            if (target - numbers[i]) in all_nums and all_nums[target - numbers[i]] != (i + 1):
                to_return[0] = min(all_nums[target - numbers[i]], i + 1)
                to_return[1] = max(all_nums[target - numbers[i]], i + 1)
                return to_return