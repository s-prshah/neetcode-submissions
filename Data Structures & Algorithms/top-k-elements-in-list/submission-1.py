class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for i in range(len(nums)):
            if nums[i] in frequency_map:
                frequency_map[nums[i]] += 1
            else:
                frequency_map[nums[i]] = 1

        buckets = [[] for i in range(len(nums) + 1)]
        to_return = []
        for key, val in frequency_map.items():
            buckets[val].append(key)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                to_return.append(num)
                if len(to_return) == k:
                    return to_return



        